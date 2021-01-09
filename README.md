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

### Testing

1) Install all dependencies as shown above.
2) Run `pytest` by:

```bash
$ poetry run pytest
# or
$ pytest
```

### Linting and Code Style

The project uses [flakehell](https://github.com/life4/flakehell) as a wrapper for flake8,
and [black](https://github.com/psf/black) for automated code style fixing, also
using [pre-commit](https://pre-commit.com/).

1) Install all dependencies as shown above.
2) (Optional) Install pre-commit hooks:

```bash
$ poetry run pre-commit install
```

3) Run black:

```bash
$ poetry run black .
```

4) Run flakehell:

```bash
$ poetry run flakehell lint
```

### Building

This package uses [poetry-dynamic-versioning](https://github.com/mtkennerly/poetry-dynamic-versioning) which infers the
version number based on the Git tags. Hence, to have a proper versioning for the distribution, use Python's build system
like:

```bash
$ pip install build
$ python -m build
```

Your distribution will be in the `dist` directory.

---

## Contributions

Please feel free to contribute, be it with Issues or Pull Requests! Please read
the [Contribution guidelines](CONTRIBUTING.md)
