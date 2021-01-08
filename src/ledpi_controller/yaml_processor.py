"""YAML reader and writer."""

import yaml

from ledpi_controller.state import State


class YamlProcessor:
    def __init__(self, file):
        self.file = file

    def load(self):
        with open(self.file) as stream:
            return yaml.full_load(stream)

    def write(self, doc):
        with open(self.file, "w") as stream:
            yaml.dump(doc, stream, explicit_start=True)


class StateYamlProcessor(YamlProcessor):
    def load(self):
        return State(super().load())
