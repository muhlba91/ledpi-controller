"""Controller class for the WS2801 controller."""

import adafruit_ws2801
import board

from ledpi_controller.const import DISABLED_RGB
from ledpi_controller.state import State
from ledpi_controller.yaml_processor import YamlProcessor


class Controller:
    """WS2801 LED Controller"""

    def __init__(self, state_processor: YamlProcessor, leds: int):
        """Initialize the controller and it's configuration."""
        self.state_processor = state_processor
        self.leds = leds

        self._read_state()
        self._init_led()
        self._send_commands()

    def turn_on(self):
        """Turn the LEDs on."""
        self.state.set_on(True)
        self._send_commands()

    def turn_off(self):
        """Turn the LEDs off."""
        self.state.set_on(False)
        self._send_commands()

    def is_on(self):
        """Check if the LEDs are turned on."""
        return self.state.is_on()

    def rgb_color(self):
        """Get the current RGB color."""
        return self.state.rgb_color()

    def rgb_hex_color(self):
        """Get the current RGB color."""
        return self.state.rgb_hex_color()

    def set_rgb_color(self, hex: str):
        """Set the RGB color in HEX."""
        self.state.set_rgb_color(hex)
        self._send_commands()

    def brightness(self):
        """Get the brightness of the LEDs."""
        return self.state.brightness()

    def set_brightness(self, brightness: float):
        """Set the brightness of the LEDs."""
        self.state.set_brightness(brightness)
        self._init_led()
        self._send_commands()

    def get_leds(self):
        """Get the number of LEDs on the strip."""
        return self.leds

    def _send_commands(self):
        self.led.fill(self.rgb_color() if self.is_on() else DISABLED_RGB)
        self.led.show()
        self._write_state()

    def _init_led(self):
        self.led = adafruit_ws2801.WS2801(
            board.SCLK, board.MOSI, self.leds, brightness=self.brightness()
        )

    def _write_state(self):
        self.state_processor.write(
            self.state
        ) if self.state_processor is not None else None

    def _read_state(self):
        self.state = (
            self.state_processor.load() if self.state_processor is not None else State()
        )
