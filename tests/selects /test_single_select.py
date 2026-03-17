from locators.selects import selects_loc as loc
from test_data.selects import test_data_selects as test_data
from test_data.selects.test_data_selects import lang as lang
import pytest

def test_check_h1_text(single_select_page):
    single_select_page.open_page()
    single_select_page.check_h1_text(loc.h1, test_data.h1_text)


def test_check_select_input_required_and_enabled(single_select_page):
    single_select_page.open_page()
    single_select_page.check_select_input_language_required(loc.select)
    single_select_page.check_select_input_language_enabled(loc.select)


@pytest.mark.parametrize('payload', lang)
def test_choose_select_lang(single_select_page, payload):
    single_select_page.open_page()
    single_select_page.select_option(loc.select, payload)
    single_select_page.click_button(loc.button)
    single_select_page.check_result_text(loc.result_select_text, payload)





