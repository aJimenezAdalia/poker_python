

import yaml
from pathlib import Path
from utils.logger import Logger


filename = Path(__file__).stem
logger = Logger(filename).build_logger()


class Deck:
    """Builds a full deck from YAML configuration file."""
    def __init__(self) -> None:
        self.spades = self.cards().get('spades')
        self.spades_cards = list(self.spades.keys())

        self.clubs = self.cards().get('clubs')
        self.clubs_cards = list(self.clubs.keys())

        self.hearts = self.cards().get('hearts')
        self.hearts_cards = list(self.hearts.keys())

        self.diamonds = self.cards().get('diamonds')
        self.diamonds_cards = list(self.diamonds.keys())

        self.full_deck = self.diamonds_cards + self.clubs_cards + self.hearts_cards + self.diamonds_cards

    @staticmethod
    def cards() -> dict:
        with open('../config/game_config.yaml', 'r') as stream:
            config_file = yaml.safe_load(stream)
        cards = config_file.get('cards')
        return cards
