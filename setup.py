"""Setup of WS2801 LED Controller."""

from setuptools import setup, find_packages

setup(name="ledpi",
      package_dir={'': 'src'},
      packages=find_packages(where='src'))
