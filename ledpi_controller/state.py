"""State class for the WS2801 controller."""

import webcolors

from ledpi_controller.const import WHITE_RGB


class State:
    """WS2801 LED Status"""

    def __init__(self, state=None):
        """Initialize the state from a present one."""
        self.rgb = state.rgb if state is not None else WHITE_RGB
        self.bright = state.bright if state is not None else 1.0
        self.on = state.on if state is not None else False

    def is_on(self):
        """Check if the LEDs are turned on."""
        return self.on

    def set_on(self, on: bool):
        """Set the on property."""
        self.on = on

    def rgb_color(self):
        """Get the current RGB color."""
        return self.rgb or WHITE_RGB

    def rgb_hex_color(self):
        """Get the current RGB color."""
        return webcolors.rgb_to_hex(self.rgb_color())

    def set_rgb_color(self, hex: str):
        """Set the RGB color in HEX."""
        self.rgb = list(webcolors.hex_to_rgb(hex))

    def brightness(self):
        """Get the current brightness."""
        return self.bright

    def set_brightness(self, brightness: float):
        """Set the desired brightness."""
        self.bright = brightness

    def __eq__(self, other):
        if isinstance(self, other.__class__):
            return (
                self.rgb == other.rgb
                and self.on == other.on
                and self.bright == other.bright
            )
        return False
