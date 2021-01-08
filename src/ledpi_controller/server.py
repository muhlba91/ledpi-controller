"""Server component for the WS2801 controller."""

from ledpi_controller.controller import Controller


class Server:
    def __init__(self, controller: Controller):
        self.controller = controller

    def get_status(self):
        return {
            "state": "on" if self.controller.is_on() else "off",
            "rgb_color": self.controller.rgb_hex_color(),
            "leds": self.controller.get_leds(),
            "brightness": self.controller.brightness(),
        }

    def set_status(self, state: dict):
        if "rgb_color" in state:
            self.controller.set_rgb_color(state["rgb_color"])

        if "brightness" in state:
            self.controller.set_brightness(state["brightness"])

        if "state" in state:
            state = state["state"]
            if state == "on":
                self.controller.turn_on()
            elif state == "off":
                self.controller.turn_off()
