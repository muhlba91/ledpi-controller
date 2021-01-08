"""Server component for the WS2801 controller."""

from flask import jsonify, request
from ledpi.controller import Controller


class Server:
    def __init__(self, controller: Controller):
        self.controller = controller

    def controller_status(self):
        return {
            "state": "on" if self.controller.is_on() else "off",
            "rgb_color": self.controller.rgb_hex_color(),
            "leds": self.controller.get_leds(),
            "brightness": self.controller.brightness(),
        }

    def status(self):
        if request.method == "GET":
            msg = {
                "success": True,
                **self.controller_status()
            }
        elif request.method == "POST":
            json = request.get_json(force=True)

            if "rgb_color" in json:
                self.controller.set_rgb_color(json["rgb_color"])

            if "brightness" in json:
                self.controller.set_brightness(json["brightness"])

            if "state" in json:
                state = json["state"]
                if state == "on":
                    self.controller.turn_on()
                elif state == "off":
                    self.controller.turn_off()

            msg = {
                "success": True,
                **self.controller_status()
            }
        else:
            msg = {
                "success": False,
                "error": "Invalid HTTP method."
            }

        return jsonify(msg)
