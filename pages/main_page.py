from driver import Driver

class MainPage:
    URL = "https://demoqa.com/"

    def __init__(self, driver: Driver):
        self.__driver = driver

    def open_page(self):
        self.__driver.get(self.URL)
