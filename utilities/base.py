import inspect
import logging
from pathlib import Path

import pytest


@pytest.mark.usefixtures("setup")
class Base:

    ROOT_PATH = str(Path(__file__).parent.parent)

    def get_logger(self):
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
        file_handler = logging.FileHandler(self.ROOT_PATH+"/logs/"+'logfile.log')
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)  # filehandler object
        logger.setLevel(logging.DEBUG)
        return logger
