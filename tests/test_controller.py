"""Tests for the Controller class."""
import sys
from unittest.mock import MagicMock, patch

mock_ws2801 = MagicMock()
mock_leds = MagicMock()
mock_ws2801.WS2801.return_value = mock_leds
sys.modules["adafruit_ws2801"] = mock_ws2801
sys.modules["board"] = MagicMock()

import pytest
from ledpi_controller.const import DISABLED_RGB, WHITE_RGB
from ledpi_controller.controller import Controller
from ledpi_controller.state import State


class TestController:
    @pytest.fixture
    def mock_yaml_processor(self):
        with patch(
            "ledpi_controller.yaml_processor.StateYamlProcessor"
        ) as mock_yaml_processor:
            mock_yaml_processor.load.return_value = State()
            yield mock_yaml_processor

    @pytest.fixture
    def ctrl(self, mock_yaml_processor):
        mock_yaml_processor.load.return_value = State()
        yield Controller(mock_yaml_processor, 160)
        assert mock_yaml_processor.load.called

    def test_init(self, ctrl):
        assert ctrl.state == State()

    def test_is_on(self, ctrl):
        ctrl.state.on = True
        assert ctrl.is_on()

    def test_turn_on(self, mock_yaml_processor, ctrl):
        ctrl.turn_on()
        assert ctrl.is_on()
        assert mock_yaml_processor.write.called
        mock_leds.fill.assert_called_with(ctrl.rgb_color())
        assert mock_leds.show.called

    def test_turn_off(self, mock_yaml_processor, ctrl):
        ctrl.turn_off()
        assert not ctrl.is_on()
        assert mock_yaml_processor.write.called
        mock_leds.fill.assert_called_with(DISABLED_RGB)
        assert mock_leds.show.called

    def test_rgb_color(self, ctrl):
        ctrl.state.set_rgb_color("#ffffff")
        assert ctrl.rgb_color() == list(WHITE_RGB)

    def test_rgb_hex_color(self, ctrl):
        ctrl.state.set_rgb_color("#ffffff")
        assert ctrl.rgb_hex_color() == "#ffffff"

    def test_set_rgb_color_turned_on(self, mock_yaml_processor, ctrl):
        ctrl.set_rgb_color("#ffffff")
        assert ctrl.rgb_color() == list(WHITE_RGB)
        assert mock_yaml_processor.write.called
        assert mock_leds.fill.called
        assert mock_leds.show.called

    def test_brightness(self, ctrl):
        ctrl.state.set_brightness(0.5)
        assert ctrl.brightness() == 0.5

    def test_set_brightness(self, mock_yaml_processor, ctrl):
        ctrl.set_brightness(0.5)
        assert ctrl.brightness() == 0.5
        assert mock_yaml_processor.write.called
        assert mock_leds.fill.called
        assert mock_leds.show.called

    def test_get_leds(self, ctrl):
        assert ctrl.get_leds() == 160
