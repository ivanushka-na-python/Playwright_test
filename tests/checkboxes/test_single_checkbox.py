from locators.checkboxes import checkboxes_loc as loc
from test_data.checkboxes import test_data_checkboxes as test_data


def test_check_h1_text(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.check_h1_text(loc.h1_loc, test_data.h1_text)


def test_check_count_checkboxes(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.check_count_checkboxes(test_data.checkbox_one)


def test_check_by_icon_checkbox(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.check_checkbox_by_icon(loc.checkbox1)
    single_checkbox_page.click_button(loc.button)
    single_checkbox_page.check_result_checkbox_text(loc.result, test_data.result_single_checkbox_text)


def test_check_by_text_checkbox(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.check_checkbox_by_text(loc.checkbox_text1)
    single_checkbox_page.click_button(loc.button)
    single_checkbox_page.check_result_checkbox_text(loc.result, test_data.result_single_checkbox_text)


def test_click_without_check_checkbox(single_checkbox_page):
    single_checkbox_page.open_page()
    single_checkbox_page.click_button(loc.button)
    single_checkbox_page.invisible_result_checkbox(loc.result)


