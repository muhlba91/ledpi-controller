"""Tests for the YamlProcessor classes."""

import os
from ledpi_controller.state import State
from ledpi_controller.yaml_processor import YamlProcessor, StateYamlProcessor


class TestYamlProcessor:
    def test_load(self):
        yaml = YamlProcessor("tests/test.yml").load()
        assert yaml.get("enabled")
        assert yaml.get("not_found") is None

    def test_write(self):
        YamlProcessor("tests/test_write.yml").write({"enabled": True})
        assert os.path.exists("tests/test_write.yml")
        os.remove("tests/test_write.yml")


class TestStateYamlProcessor:
    def test_load(self):
        state = StateYamlProcessor("tests/test_state.yml").load()
        assert isinstance(state, State)
