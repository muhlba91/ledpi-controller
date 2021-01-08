# LED-Pi - Raspberry Pi WS2801 LED Controller

[![](https://img.shields.io/github/license/muhlba91/ledpi-controller?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/workflow/status/muhlba91/ledpi-controller/Python%20package?style=for-the-badge)](https://github.com/muhlba91/ledpi-controller/actions)

This repository contains a **server component** to control a **WS2801 LED strip** connected to a Raspberry Pi.

---

## Installation

1) Checkout the repository.
2) Create the configuration file as shown in *Configuration*.
3) Install the Python requirements.

```bash
$ pip3 install -r requirements.txt
```

4) Run the application.

```bash
$ cd src/
$ python3 main.py -c path/to/config.yml -s path/to/state.yml
```

## Configuration

The application supports two **options**:

| Option | Description |
|--------|-------------|
| -c, --config | Path to the configuration file. |
| -s, --state | Path to the state file. |

### Configuration File

The configuration file defines **global properties** for the application running.

| Option | Description | Default |
|--------|-------------|---------|
| port | The port to bind the API to. | 80 |
| leds | The number of LEDs on the strip. | 160 |
| debug | True if the application should run in debug mode. | false |

An *example* is available in the `examples` directory.

### State File

The state file **stores** the **current state** of the LED strip and, therefore, is a way of persistent storage to **
recover the state** after a restart.

**Important:** please do **not modify** the state file manually!

## API Documentation

The documentation of the exposed API is **defined** in `OpenAPI` in the **file [`api.yml`](api.yml)**.

## Systemd Service

A simple systemd service can be created to automatically start the server like:

```
[Unit]
Description=LedPi service
After=network.target

[Service]
User=pi
WorkingDirectory=/home/pi/ledpi
ExecStartPre=pip3 install -r requirements.txt
ExecStart=python3 main.py -c config.yml -s state.yml
Restart=always

[Install]
WantedBy=multi-user.target
```

(Also available in the `examples` directory.)

---

## Running Tests

To run the test suite create a virtualenv (I recommend checking out [pyenv](https://github.com/pyenv/pyenv)
and [pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) for this) and install the test requirements.

```bash
$ pip install -r requirements.test.txt
```

After the test dependencies are installed you can simply invoke `pytest` to run the test suite.

```bash
$ pytest
```

---

## Contributions

Please feel free to contribute, be it with Issues or Pull Requests! Please read
the [Contribution guidelines](CONTRIBUTING.md)
