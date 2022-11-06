

from pathlib import Path
from utils.logger import Logger
from config.config import Config


filename = Path(__file__).stem
logger = Logger(filename).build_logger()


class Poker:
    def __init__(self):
        self.number_of_players = 0

        self.config = Config()
        self.game_config = self.config.game_config()

        self.game_strings = self.config.game_strings()
        self.pregame_strings = self.game_strings.get('before_start')

    def run(self):
        print(self.pregame_strings.get('welcome'))

        play = False

        while not play:
            while self.number_of_players == 0:
                number_of_players = input(self.pregame_strings.get('how_many_players'))
                try:
                    self.number_of_players = int(number_of_players)
                    if self.number_of_players != 0:
                        if self.number_of_players > 9:
                            print(self.pregame_strings.get('maximum_players_out_of_reach').format(
                                self.number_of_players)
                            )
                            self.number_of_players = 0
                            continue
                except ValueError:
                    print(self.pregame_strings.get('int_not_selected'))

            print(self.pregame_strings.get('proceed_start').format(self.number_of_players))
