import logging
import os


def loggen():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(name)s - %(message)s",
        filename="../logs/report.log",
        encoding="utf-8",
    )
    logger = logging.getLogger()
    # f_handler = logging.FileHandler('./logs/report.log', mode="w")
    # formatter = logging.Formatter('%(asctime)s  - %(levelname)s - %(message)s')
    # f_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.info("Test log")
loggen()