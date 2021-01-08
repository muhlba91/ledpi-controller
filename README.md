# LED-Pi - Raspberry Pi WS2801 LED Controller

[![](https://img.shields.io/github/license/muhlba91/ledpi-controller?style=for-the-badge)](LICENSE)
[![](https://img.shields.io/github/workflow/status/muhlba91/ledpi-controller/Python%20package?style=for-the-badge)](https://github.com/muhlba91/ledpi-controller/actions)

This repository contains a **server component** to control a **WS2801 LED strip** connected to a Raspberry Pi.

---

## Installation

The package is published in **(Test)PyPi** and can be installed via:

```bash
pip3 install ledpi-controller
```

In `examples/main.py` a simple Flask application shows the usage which can be run by:

1) Install the `ledpi-controller` package.
2) Create a configuration file as shown in *Configuration*.
3) Install the Python requirements.

```bash
$ pip3 install -r requirements.txt
$ pip3 install -r examples/requirements.txt
```

4) Run the application.

```bash
$ python3 examples/main.py -c path/to/config.yml -s path/to/state.yml
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
