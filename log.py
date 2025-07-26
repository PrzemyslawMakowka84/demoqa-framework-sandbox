import logging

class Log:
    def __init__(self):
        self.__log = logging.getLogger()
        self.__log.setLevel(logging.INFO)

    def info(self, message: str):
        self.__log.info(message)