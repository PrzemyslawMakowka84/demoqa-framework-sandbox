from pages.main_page import MainPage
from assertpy import assert_that

def test_open_main_page(main_page: MainPage):
    main_page.open_page()
    assert_that(main_page.current_url).is_equal_to(main_page.URL)
