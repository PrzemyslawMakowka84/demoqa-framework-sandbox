import pytest
from browser import Browser
from enums import BrowserTypes


@pytest.fixture
def browser_enum(browser_type: str) -> BrowserTypes:
    try:
        return BrowserTypes(browser_type.lower())
    except ValueError:
        raise ValueError(f"Only {BrowserTypes.CHROME} or {BrowserTypes.FIREFOX} is supported!")

@pytest.fixture
def browser(browser_enum):
    brw = Browser(browser_enum)
    yield brw
    brw.quit_driver()

@pytest.fixture
def browser_type(request):
    return request.config.getoption("--browser-type")

def pytest_addoption(parser):
    parser.addoption("--browser-type", type=str, default="chrome", help="Browser type")
