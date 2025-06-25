from selenium.webdriver.remote.webdriver import WebDriver


def test_page(driver: WebDriver):
    driver.get("https://demoqa.com/")
