from selenium import webdriver
from enums import BrowserTypes

class Driver:
    def __init__(self):
        self.__driver: webdriver = None

    def initial_driver(self, browser_type: BrowserTypes) -> webdriver:
        if not self.__driver:
            match browser_type:
                case BrowserTypes.CHROME:
                    chrome_options = webdriver.ChromeOptions()
                    chrome_options.add_argument("--start-maximized")
                    self.__driver = webdriver.Chrome(options=chrome_options)
                case BrowserTypes.FIREFOX:
                    self.__driver = webdriver.Firefox()
                    self.__driver.maximize_window()

        return self.driver

    @property
    def driver(self) -> webdriver:
        if self.__driver:
            return self.__driver
        else:
            raise ValueError("driver must be initialized first!")

    def get(self, url):
        if url:
            self.__driver.get(url)

    def quit(self):
        if self.__driver:
            self.__driver.quit()
            self.__driver = None
