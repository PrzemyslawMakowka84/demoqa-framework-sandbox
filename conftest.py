import pytest
from driver import Driver
from selenium import webdriver


@pytest.fixture
def driver() -> webdriver:
    drv = Driver()
    drv.initial_driver()
    yield drv.driver
    drv.quit()
