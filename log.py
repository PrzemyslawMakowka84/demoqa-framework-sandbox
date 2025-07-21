import logging

class Log:
    def __init__(self):
        self.__log = logging.getLogger("framework_demoqa")
        self.__log.setLevel(logging.INFO)
        self.__log.propagate = False
        formater = logging.Formatter(
            fmt='%(asctime)s %(levelname)s %(message)s (%(name)s)', datefmt="%Y-%m-%d  %H:%M:%S"
        )
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formater)
        console_handler.setLevel(logging.INFO)
        if not self.__log.handlers:
            self.__log.addHandler(console_handler)

    def info(self, message: str):
        self.__log.info(message)