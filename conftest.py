import pytest
from browser import Browser
from enums import BrowserTypes
from log import Log

@pytest.fixture
def browser_enum(browser_type: str) -> BrowserTypes:
    try:
        return BrowserTypes(browser_type.lower())
    except ValueError:
        raise ValueError(f"Only {BrowserTypes.CHROME} or {BrowserTypes.FIREFOX} is supported!")

@pytest.fixture
def browser(browser_enum, log):
    brw = Browser(browser_enum, log)
    yield brw
    brw.quit_driver()

@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser-type")

@pytest.fixture
def log() -> Log:
    return Log()

def pytest_addoption(parser):
    parser.addoption("--browser-type", type=str, default="chrome", help="Browser type")
