from typing import Any, Generator
import pytest
from selenium.webdriver.ie.webdriver import WebDriver
from driver import Driver
from enums import BrowserTypes
from log import Log
from pages.main_page import MainPage


@pytest.fixture
def browser_name(browser_type: str) -> BrowserTypes:
    try:
        return BrowserTypes(browser_type.lower())
    except ValueError:
        raise ValueError(f"Only {BrowserTypes.CHROME} or {BrowserTypes.FIREFOX} is supported!")

@pytest.fixture
def driver(browser_name, log) -> Generator[WebDriver, None, None]:
    drv = Driver(browser_name, log)
    yield drv.initial_driver()
    drv.quit()

@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser-type")

@pytest.fixture
def log() -> Log:
    return Log()

@pytest.fixture
def main_page(driver: Driver) -> MainPage:
    return MainPage(driver)

def pytest_addoption(parser):
    parser.addoption("--browser-type", type=str, default="chrome", help="Browser type")
