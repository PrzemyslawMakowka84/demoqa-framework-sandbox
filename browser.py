from driver import Driver
from enums import BrowserTypes

class Browser:
    def __init__(self, browser_type: BrowserTypes = BrowserTypes.CHROME):
        self.__driver = Driver()
        self.__driver.initial_driver(browser_type)

    def goto_url(self, url):
        self.__driver.get(url)

    def quit_driver(self):
        self.__driver.quit()
