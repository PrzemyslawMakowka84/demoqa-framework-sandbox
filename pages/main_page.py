from driver import Driver

class MainPage:
    URL = "https://demoqa.com/"

    def __init__(self, driver: Driver):
        self.driver = driver

    def open_page(self):
        self.driver.get(self.URL)

    @property
    def current_url(self) -> str:
        return self.driver.current_url