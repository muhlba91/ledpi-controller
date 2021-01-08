# LED-Pi - Raspberry Pi WS2801 LED Controller

[![](https://img.shields.io/github/license/muhlba91/ledpi-controller?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/workflow/status/muhlba91/ledpi-controller/Python%20package?style=for-the-badge)](https://github.com/muhlba91/ledpi-controller/actions)

This repository contains a **server component** to control a **WS2801 LED strip** connected to a Raspberry Pi.

---

## Installation

The package is published in **(Test)PyPi** and can be installed via:

```bash
pip install ledpi-controller
```

In `examples/main.py` a simple Flask application shows the usage which can be run by:

1) Install the `ledpi-controller` package.
2) Create a configuration file as shown in *Configuration*.
4) Run the application.

```bash
$ python examples/main.py -c path/to/config.yml -s path/to/state.yml
```

### Configuration

The configuration defines **global properties** as a `dict` for the application running.

| Option | Description | Default |
|--------|-------------|---------|
| port | The port to bind the API to. | 80 |
| leds | The number of LEDs on the strip. | 160 |
| debug | True if the application should run in debug mode. | false |

### State File

The state file **stores** the **current state** of the LED strip and, therefore, is a way of persistent storage to
**recover the state** after a restart.

**Important:** please do **not modify** the state file manually!

---

## Development

The project uses [poetry](https://poetry.eustace.io/) and to install all dependencies and the build environment, run:

```bash
$ pip install poetry
$ poetry install
```

## Testing

To run the tests, use poetry to install all dependencies and then execute:

```bash
$ pytest
```

---

## Contributions

Please feel free to contribute, be it with Issues or Pull Requests! Please read
the [Contribution guidelines](CONTRIBUTING.md)
