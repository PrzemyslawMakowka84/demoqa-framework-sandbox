from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from enums import BrowserTypes

class Driver:
    def __init__(self, browser_name: str, log):
        self.driver: WebDriver | None = None
        self.__log = log
        self.__browser_type = browser_name
        self.initial_driver()


    def initial_driver(self):
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


    def get(self, url):
        if not self.driver:
            raise RuntimeError("Driver is not initialed!")
        if url:
            self.__log.info(f"Navigate to {url}")
            self.driver.get(url)

    @property
    def current_url(self):
        return self.driver.current_url

    def quit(self):
        if self.driver:
            self.__log.info("driver quit()")
            self.driver.quit()
            self.driver = None