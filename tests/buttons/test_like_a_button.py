from locators.buttons import buttons_loc as loc
from test_data.buttons import test_data_buttons as test_data


def test_check_h1_text(like_a_button_page):
    like_a_button_page.open_page()
    like_a_button_page.check_h1_text(loc.h1_loc, test_data.h1_text)


def test_button_enabled(like_a_button_page):
    like_a_button_page.open_page()
    like_a_button_page.check_button_enabled(loc.button_link)


def test_submit_button(like_a_button_page):
    like_a_button_page.open_page()
    like_a_button_page.click_button(loc.button_link)
    like_a_button_page.check_button_submitted(loc.button_submitted, test_data.button_submitted_text)