

import json
import yaml
from utils.file_utils import PROJECT_ROOT


class Config:
    def __init__(self):
        pass

    @staticmethod
    def game_config():
        with open(f'{PROJECT_ROOT}/config/game_config.yaml', 'r') as stream:
            game_config_file = yaml.safe_load(stream)

        return game_config_file

    @staticmethod
    def game_strings():
        with open(f'{PROJECT_ROOT}/config/game_strings.json', 'r') as f:
            game_strings_file = json.load(f)

        return game_strings_file
