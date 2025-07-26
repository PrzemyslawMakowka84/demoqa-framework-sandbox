from driver import Driver
from enums import BrowserTypes


class Browser:
    def __init__(self, browser_type: BrowserTypes, log):
        self.__log = log
        self.__driver = Driver(log)
        match browser_type:
            case BrowserTypes.CHROME:
                self.__driver.initial_driver(BrowserTypes.CHROME)
            case BrowserTypes.FIREFOX:
                self.__driver.initial_driver(BrowserTypes.FIREFOX)

    def goto_url(self, url):
        self.__log.info(f"Open {url} in browser")
        self.__driver.get(url)

    def quit_driver(self):
        self.__log.info("Browser quit()")
        self.__driver.quit()
