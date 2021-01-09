"""Tests for the State class."""

import pytest

from ledpi_controller.const import DISABLED_RGB
from ledpi_controller.const import WHITE_RGB
from ledpi_controller.state import State


class TestState:
    @pytest.fixture
    def state(self):
        yield State()

    def test_init_defaults(self, state):
        assert state.rgb == WHITE_RGB
        assert not state.on
        assert state.bright == 1.0

    def test_init_from_state(self, state):
        state.rgb = DISABLED_RGB
        new_state = State(state)
        assert new_state == state

    def test_rgb_hex_color(self, state):
        state.rgb = WHITE_RGB
        assert state.rgb_hex_color() == "#ffffff"

    def test_set_rgb_color(self, state):
        state.set_rgb_color("#ffffff")
        assert state.rgb_color() == list(WHITE_RGB)

    def test_is_on(self, state):
        state.on = True
        assert state.is_on()

    def test_set_on(self, state):
        state.set_on(True)
        assert state.on

    def test_brightness(self, state):
        state.bright = 0.5
        assert state.brightness() == 0.5

    def test_set_brightness(self, state):
        state.set_brightness(0.5)
        assert state.bright == 0.5

    def test_eq(self):
        assert State() == State()

    def test_not_eq(self):
        assert State() != list()
