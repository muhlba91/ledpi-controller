"""Tests for the Server class."""
import pytest
from flask import json, Flask
from ledpi.server import Server
from unittest.mock import patch

app = Flask(__name__)


class TestServer:
    @pytest.fixture
    def ctrl(self):
        with patch("ledpi.controller.Controller") as mock_controller:
            mock_controller.is_on.return_value = True
            mock_controller.rgb_hex_color.return_value = "value"
            mock_controller.get_leds.return_value = 160
            mock_controller.brightness.return_value = 1.0
            yield mock_controller

    @pytest.fixture
    def server(self, ctrl):
        yield Server(ctrl)

    def test_init(self, server):
        assert server.controller is not None

    def test_controller_status(self, ctrl, server):
        assert server.controller_status() == {
            "state": "on",
            "rgb_color": "value",
            "leds": 160,
            "brightness": 1.0,
        }
        assert ctrl.is_on.called
        assert ctrl.rgb_hex_color.called
        assert ctrl.get_leds.called
        assert ctrl.brightness.called

    def test_status_get(self, server):
        with app.test_request_context(method="GET"):
            assert json.loads(server.status().data) == {
                "success": True,
                "state": "on",
                "rgb_color": "value",
                "leds": 160,
                "brightness": 1.0,
            }

    def test_status_post_turn_on(self, ctrl, server):
        with app.test_request_context(method="POST", json={
            "state": "on",
            "rgb_color": "#ffffff",
            "brightness": 0.5,
        }):
            server.status()
            assert ctrl.set_rgb_color.called
            assert ctrl.set_brightness.called
            assert ctrl.turn_on.called

    def test_status_post_turn_off(self, ctrl, server):
        with app.test_request_context(method="POST", json={
            "state": "off",
            "rgb_color": "#ffffff",
            "brightness": 0.5,
        }):
            server.status()
            assert ctrl.set_rgb_color.called
            assert ctrl.set_brightness.called
            assert ctrl.turn_off.called

    def test_status_post_partial(self, ctrl, server):
        with app.test_request_context(method="POST", json={
            "rgb_color": "#ffffff",
            "brightness": 0.5,
        }):
            server.status()
            assert ctrl.set_rgb_color.called
            assert ctrl.set_brightness.called
            assert not ctrl.turn_off.called
            assert not ctrl.turn_on.called

    def test_status_invalid_http_method(self, server):
        with app.test_request_context(method="OPTIONS"):
            assert json.loads(server.status().data) == {
                "success": False,
                "error": "Invalid HTTP method.",
            }
