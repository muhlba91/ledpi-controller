"""App components for the WS2801 controller."""

from flask import Flask
from ledpi.controller import Controller
from ledpi.server import Server


def create_app(config=None, state_processor=None):
    leds = config.get("leds", 160) if config is not None else 160
    controller = Controller(state_processor, leds)
    server = Server(controller)

    app = Flask(__name__)

    @app.route("/api/v1/state", methods=['GET', 'POST'])
    def state_method():
        return server.status()

    return app
