from locators.buttons import buttons_loc as loc
from test_data.buttons import test_data_buttons as test_data

def test_check_h1_text(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.check_h1_text(loc.h1_loc, test_data.h1_text)


def test_submitted_button(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.check_button_disabled(loc.button)
    disabled_button_page.select_enabled_option(loc.select, test_data.option_enable)
    disabled_button_page.check_button_enabled(loc.button)
    disabled_button_page.click_button(loc.button)
    disabled_button_page.check_button_submitted(loc.button_submitted, test_data.button_submitted_text)


def test_switch_select_button(disabled_button_page):
    disabled_button_page.open_page()
    disabled_button_page.check_button_disabled(loc.button)
    disabled_button_page.select_enabled_option(loc.select, test_data.option_enable)
    disabled_button_page.check_button_enabled(loc.button)
    disabled_button_page.select_disabled_option(loc.select, test_data.option_disable)
    disabled_button_page.check_button_disabled(loc.button)