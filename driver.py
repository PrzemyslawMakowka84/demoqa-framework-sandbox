from selenium import webdriver
from selenium.webdriver.ie.webdriver import WebDriver
from enums import BrowserTypes

class Driver:
    def __init__(self, browser_name: str, log):
        self.driver = None
        self.__log = log
        self.__browser_type = browser_name


    def initial_driver(self) -> WebDriver:
        if not self.driver:
            match self.__browser_type:
                case BrowserTypes.CHROME:
                    self.__log.info("Setup Chrome browser")
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--start-maximized")
                    self.driver = webdriver.Chrome(options=chrome_options)
                    self.__log.info("Chrome browser was initialized")
                case BrowserTypes.FIREFOX:
                    self.__log.info("Setup Firefox browser")
                    self.driver = webdriver.Firefox()
                    self.driver.maximize_window()
                    self.__log.info("Firefox browser was initialized")

        return self.driver

    def get(self, url):
        if not self.driver:
            raise RuntimeError("Driver is not initialed!")
        if url:
            self.__log.info(f"Navigate to {url}")
            self.driver.get(url)


    def quit(self):
        if self.driver:
            self.__log.info("driver quit()")
            self.driver.quit()
            self.driver = None