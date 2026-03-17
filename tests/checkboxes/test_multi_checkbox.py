
from locators.checkboxes import checkboxes_loc as loc
from test_data.checkboxes import test_data_checkboxes as test_data
from locators.checkboxes.checkboxes_loc import checkboxes as loc_checkbox
from locators.checkboxes.checkboxes_loc import checkboxes_texts as loc_checkbox_texts
from test_data.checkboxes.test_data_checkboxes import result_checkbox_text_list as list_checkbox_texts


import pytest


def test_check_h1_text(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.check_h1_text(loc.h1_loc, test_data.h1_text)


def test_check_count_checkboxes(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.check_count_checkboxes(loc.checkbox_class, test_data.checkbox_three)


@pytest.mark.parametrize('locator , expected_result',
                         zip(loc_checkbox_texts, list_checkbox_texts))
def test_click_checkboxes_by_text(multi_checkbox_page, locator, expected_result):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_checkbox_by_text(locator)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, expected_result)


@pytest.mark.parametrize('locator , expected_result',
                         zip(loc_checkbox, list_checkbox_texts))
def test_click_checkboxes_by_checkbox(multi_checkbox_page, locator, expected_result):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_checkbox_by_icon(locator)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, expected_result)


def test_first_and_second_click_checkbox(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_many_checkboxes(loc.checkbox1, loc.checkbox2)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, f'{test_data.result_first_check_text },'
                                                               f' {test_data.result_second_check_text}')


def test_first_and_third_click_checkbox(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_many_checkboxes(loc.checkbox1, loc.checkbox3)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, f'{test_data.result_first_check_text }, '
                                                               f'{test_data.result_third_check_text}')


def test_second_and_third_click_checkbox(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_many_checkboxes(loc.checkbox2, loc.checkbox3)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, f'{test_data.result_second_check_text },'
                                                               f' {test_data.result_third_check_text}')


def test_click_all_checkboxes(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.check_many_checkboxes(loc.checkbox1, loc.checkbox2, loc.checkbox3)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.check_result_checkbox_text(loc.result, f'{test_data.result_first_check_text }, '
                                                               f'{test_data.result_second_check_text}, '
                                                               f'{test_data.result_third_check_text}')


def test_click_button_without_checkbox(multi_checkbox_page):
    multi_checkbox_page.open_page()
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.click_button(loc.button)
    multi_checkbox_page.button_enabled(loc.button)
    multi_checkbox_page.invisible_result_checkbox(loc.result)







