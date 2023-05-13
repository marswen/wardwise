import logging
import datetime


def init_logger():
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    file_handler = logging.FileHandler(f'{datetime.date.today().strftime("%Y%m%d")}.log')
    file_handler.setLevel(level=logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s - %(message)s")
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    return logger


logger = init_logger()
