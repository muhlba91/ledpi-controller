"""Server components for the WS2801 controller."""

import argparse
import flask
from flask import jsonify, request

from controller import Controller
from yaml_processor import YamlProcessor, StateYamlProcessor

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", required=True)
parser.add_argument("-s", "--state", required=True)
args = parser.parse_args()

config = YamlProcessor(args.config).load()

controller = Controller(StateYamlProcessor(args.state), config.get("leds", 160))
app = flask.Flask(__name__)


def controller_status():
    return {
        "state": "on" if controller.is_on() else "off",
        "rgb_color": controller.rgb_hex_color(),
        "leds": controller.get_leds(),
        "brightness": controller.brightness(),
    }


@app.route("/api/v1/state", methods=['GET', 'POST'])
def status():
    if request.method == "GET":
        msg = {
            "success": True,
            **controller_status()
        }
    elif request.method == "POST":
        json = request.get_json(force=True)

        if "rgb_color" in json:
            controller.set_rgb_color(json["rgb_color"])

        if "brightness" in json:
            controller.set_brightness(json["brightness"])

        if "state" in json:
            state = json["state"]
            if state == "on":
                controller.tun_on()
            elif state == "off":
                controller.turn_off()

        msg = {
            "success": True,
            **controller_status()
        }
    else:
        msg = {
            "success": False,
            "error": "Invalid HTTP method."
        }

    return jsonify(msg)


# main()
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.get("port", 80), debug=config.get("debug", False))
