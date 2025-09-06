import logging
import allure


class Log:
    def __init__(self, allure_list_log: list[str]):
        self.__log = logging.getLogger(__name__)
        self.__log.setLevel(logging.INFO)
        self.__allure_list_log = allure_list_log

    def info(self, message: str):
        self.__log.info(message)
        self.__append(message)

    def __append(self, message: str):
        self.__allure_list_log.append(message)

    def attach_to_allure(self):
        allure_all_log_str: str = ""
        "\n".join(self.__allure_list_log)
        allure.attach(allure_all_log_str, "Allure logs", attachment_type=allure.attachment_type.TEXT, extension=".txt")