import allure
from selenium import webdriver
from enums import BrowserTypes

class Driver:
    def __init__(self, log):
        self.__driver: webdriver = None
        self.__log = log

    def initial_driver(self, browser_type: BrowserTypes) -> webdriver:
        if not self.__driver:
            self.__log.info("Starting initializing browser")
            match browser_type:
                case BrowserTypes.CHROME:
                    self.__log.info("Setup Chrome browser")
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--start-maximized")
                    self.__driver = webdriver.Chrome(options=chrome_options)
                    self.__log.info("Chrome browser was initialized")
                case BrowserTypes.FIREFOX:
                    self.__log.info("Setup Firefox browser")
                    self.__driver = webdriver.Firefox()
                    self.__driver.maximize_window()
                    self.__log.info("Firefox browser was initialized")

        return self.driver

    @property
    def driver(self) -> webdriver:
        if self.__driver:
            return self.__driver
        else:
            raise ValueError("driver must be initialized first!")

    def get(self, url):
        if url:
            self.__log.info(f"Navigate to {url}")
            self.__driver.get(url)

    def quit(self):
        if self.__driver:
            self.__log.info("driver quit()")
            self.__driver.quit()
            self.__driver = None