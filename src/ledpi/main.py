"""Server components for the WS2801 controller."""

import argparse

from ledpi.app import create_app
from ledpi.yaml_processor import YamlProcessor, StateYamlProcessor

parser = argparse.ArgumentParser()
parser.add_argument("-c", "--config", required=True)
parser.add_argument("-s", "--state", required=True)
args = parser.parse_args()

# main()
if __name__ == "__main__":
    config = YamlProcessor(args.config).load()
    state_processor = StateYamlProcessor(args.state)
    create_app(config, state_processor) \
        .run(host='0.0.0.0', port=config.get("port", 80), debug=config.get("debug", False))
