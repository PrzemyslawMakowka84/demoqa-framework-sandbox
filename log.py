import logging
from datetime import datetime

class Log:
    def __init__(self):
        self.__log = logging.getLogger(__name__)

    def info(self, message: str):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        line = f"{timestamp} {message}"
        self.__log.info(line)