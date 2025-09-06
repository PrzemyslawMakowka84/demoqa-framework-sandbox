from browser import Browser


def test_page(browser: Browser):
    browser.goto_url("https://demoqa.com/")