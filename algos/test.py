import logging
import time
import sys

logger = logging.getLogger()
formatter = logging.Formatter("%(asctime)s %(name)-12s %(levelname)-8s %(message)s")
fmt2 = logging.Formatter("errorrrrrrrrrrrrr %(name)-12s %(levelname)-8s %(message)s")

consoleh = logging.StreamHandler(sys.stdout)

errorh = logging.StreamHandler(sys.stderr)

errorh.setFormatter(fmt2)

nonerror = lambda record: record.levelno != logging.ERROR
error = lambda record: record.levelno == logging.ERROR

consoleh.setFormatter(formatter)
consoleh.addFilter(nonerror)
errorh.addFilter(error)

logger.addHandler(consoleh)
logger.addHandler(errorh)
logger.setLevel(logging.DEBUG)

for i in range(0, 1000):
    logging.info("Info log")
    time.sleep(1)
    logging.error("error log")
    logging.debug("debug log")

