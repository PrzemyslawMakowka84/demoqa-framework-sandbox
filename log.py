import logging
import allure


class Log:
    def __init__(self, allure_text: list[str]):
        self.__log = logging.getLogger()
        self.__log.setLevel(logging.INFO)
        self.__allure_text = allure_text

    def info(self, message: str):
        self.__log.info(message)
        self.__append(message)

    def __append(self, message: str):
        self.__allure_text.append(message)

    def __attach_to_allure(self):
        allure.attach(self.__allure_text, "Allure logs", attachment_type=allure.attachment_type.TEXT, extension=".txt")