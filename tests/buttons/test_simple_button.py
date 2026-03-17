from locators.buttons import buttons_loc as loc
from test_data.buttons import test_data_buttons as test_data



def test_check_h1_text(simple_button_page):
    simple_button_page.open_page()
    simple_button_page.check_h1_text(loc.h1_loc, test_data.h1_text)


def test_submit_button(simple_button_page):
    simple_button_page.open_page()
    simple_button_page.check_button_enabled(loc.button)
    simple_button_page.click_button(loc.button)
    simple_button_page.check_button_submitted(loc.button_submitted, test_data.button_submitted_text)