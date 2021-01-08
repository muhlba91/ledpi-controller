"""Setup of WS2801 LED Controller."""

import os
from setuptools import setup, find_packages


def read(file):
    return open(os.path.join(os.path.dirname(__file__), file)).read()


setup(
    name="ledpi-controller",
    version="0.0.1",
    author="Daniel Muehlbachler-Pietrzykowski",
    author_email="daniel.muehlbachler@niftyside.io",
    description=("Raspberry Pi API component to control a WS2801 LED strip."),
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    license="MIT",
    keywords="ws2801 raspberrypi",
    url="https://github.com/muhlba91/ledpi-controller",
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
)
