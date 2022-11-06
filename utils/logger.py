

import logging


class Logger:
    """Builds a generic logger to use along the project."""
    def __init__(self, file_name: str):
        logging.basicConfig(
            format='%(asctime)s,%(msecs)d %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s',
            datefmt='%Y-%m-%d:%H:%M:%S',
            level=logging.DEBUG)
        self.logger_name = file_name

    def build_logger(self):
        logger = logging.getLogger(self.logger_name)
        return logger
