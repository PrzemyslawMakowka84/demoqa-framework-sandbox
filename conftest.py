import pytest
from browser import Browser


@pytest.fixture
def browser():
    brw = Browser()
    yield brw
    brw.quit_driver()
