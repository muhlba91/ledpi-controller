"""Tests for the /status endpoint."""
import sys
from unittest.mock import MagicMock

sys.modules["adafruit_ws2801"] = MagicMock()
sys.modules["board"] = MagicMock()

from flask import json
import pytest
import logging
from ledpi.app import create_app

_LOGGER = logging.getLogger(__name__)


class TestIntegrationState:
    @pytest.fixture(scope="module")
    def client(self):
        yield create_app().test_client()

    def test_get(self, client):
        result = client.get("/api/v1/state")
        assert result.status_code == 200
        data = json.loads(result.data)
        assert data == {
            "brightness": 1.0,
            "leds": 160,
            "rgb_color": "#ffffff",
            "state": "off",
            "success": True
        }

    def test_post(self, client):
        result = client.post("/api/v1/state", json={
            "brightness": 0.5,
            "rgb_color": "#ffffff",
            "state": "on"
        })
        assert result.status_code == 200
        data = json.loads(result.data)
        assert data == {
            "brightness": 0.5,
            "leds": 160,
            "rgb_color": "#ffffff",
            "state": "on",
            "success": True
        }
