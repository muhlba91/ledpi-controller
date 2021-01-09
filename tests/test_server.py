"""Tests for the Server class."""
import pytest
from ledpi_controller.server import Server
from unittest.mock import patch


class TestServer:
    @pytest.fixture
    def ctrl(self):
        with patch("ledpi_controller.controller.Controller") as mock_controller:
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

    def test_get_status(self, server):
        assert server.get_status() == {
            "state": "on",
            "rgb_color": "value",
            "leds": 160,
            "brightness": 1.0,
        }

    def test_set_status_turn_on(self, ctrl, server):
        server.set_status(
            {
                "state": "on",
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert ctrl.turn_on.called

    def test_set_status_turn_off(self, ctrl, server):
        server.set_status(
            {
                "state": "off",
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert ctrl.turn_off.called

    def test_set_status_partial(self, ctrl, server):
        server.set_status(
            {
                "rgb_color": "#ffffff",
                "brightness": 0.5,
            }
        )
        assert ctrl.set_rgb_color.called
        assert ctrl.set_brightness.called
        assert not ctrl.turn_off.called
        assert not ctrl.turn_on.called
