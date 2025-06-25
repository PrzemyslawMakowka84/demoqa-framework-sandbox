from enum import StrEnum
from selenium import webdriver


class WebDrivers(StrEnum):
    CHROME = "chrome"
    EDGE = "edge"


class Driver:
    def __init__(self):
        self.__driver = None

    def initial_driver(self, driver: WebDrivers = WebDrivers.CHROME) -> webdriver:
        if not self.__driver:
            match driver:
                case WebDrivers.CHROME:
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--start-maximized")
                    self.__driver = webdriver.Chrome(options=chrome_options)
                case WebDrivers.EDGE:
                    edge_options = webdriver.EdgeOptions()
                    edge_options.add_argument("--start-maximized")
                    self.__driver = webdriver.Edge(options=edge_options)

        return self.driver

    @property
    def driver(self) -> webdriver:
        if self.__driver:
            return self.__driver
        else:
            raise ValueError("driver must by initialized first!")

    def quit(self):
        if self.__driver:
            self.__driver.quit()
            self.__driver = None
