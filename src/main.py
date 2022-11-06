

from pathlib import Path
from utils.logger import Logger
from src.launch_game import Poker


filename = Path(__file__).stem
logger = Logger(filename).build_logger()


def new_game():
    logger.info('Starting new game')

    poker = Poker()
    poker.run()


if __name__ == "__main__":
    new_game()
