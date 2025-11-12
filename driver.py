from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from enums import BrowserTypes, SelectorTypes

class Driver:
    _selectors_map = {
        SelectorTypes.CSS_SELECTOR: By.CSS_SELECTOR,
        SelectorTypes.XPATH: By.XPATH
    }


    def __init__(self, browser_name: str, log):
        self.driver: WebDriver | None = None
        self.__timeout = 10
        self.__log = log
        self.__browser_type = browser_name
        self.initial_driver()
        self.__wait: WebDriverWait = WebDriverWait(self.driver, self.__timeout)


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


    def find_element(self, selector_type: SelectorTypes, value: str) -> WebElement:
       return self.__get_element(selector_type=selector_type, value=value)


    def find_elements(self, selector_type: SelectorTypes, value: str) -> list[WebElement]:
        return self.__get_elements(selector_type=selector_type, value=value)


    def __get_element(self, selector_type: SelectorTypes, value: str) -> WebElement:
        by_selector = self._selectors_map[selector_type]
        self.__log.info(f"Waiting {self.__timeout}s for element: type={selector_type}, value={value} and return")
        return self.__wait.until(EC.presence_of_element_located((by_selector, value)))


    def __get_elements(self, selector_type: SelectorTypes, value: str):
        by_selector = self._selectors_map[selector_type]
        self.__log.info(
            f"Waiting {self.__timeout}s for multiple elements: type={selector_type}, value={value} and return"
        )
        return self.__wait.until(EC.presence_of_all_elements_located((by_selector, value)))


    @property
    def current_url(self):
        return self.driver.current_url

    def quit(self):
        if self.driver:
            self.__log.info("driver quit()")
            self.driver.quit()
            self.driver = None
