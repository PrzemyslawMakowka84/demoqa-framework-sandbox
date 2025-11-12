from enum import StrEnum

class BrowserTypes(StrEnum):
    CHROME = "chrome"
    FIREFOX = "firefox"

class SelectorTypes(StrEnum):
    XPATH = "xpath"
    CSS_SELECTOR = "css_selector"