from locators.inputs import inputs_loc as loc
from test_data.inputs import test_data_inputs as test_data
from test_data.inputs.test_data_inputs import validPayloadSimple as validData
from test_data.inputs.test_data_inputs import invalidPayloadSimple as invalidData
from test_data.inputs.test_data_inputs import invalid1PayloadSimple as invalidData1
from test_data.inputs.test_data_inputs import invalid25PayloadSimple as invalidData25
import pytest


def test_check_h1_text(simple_input_page):
    simple_input_page.open_page()
    simple_input_page.check_h1_text(loc.h1_loc, test_data.h1_text)


@pytest.mark.parametrize('payload', validData)
def test_valid_text_input(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(loc.text_string_loc, payload)
    simple_input_page.submit_text_input(loc.text_string_loc)
    simple_input_page.check_valid_result_text_input(loc.valid_result_element, payload)


@pytest.mark.parametrize('payload', invalidData)
def test_invalid_text_input(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(loc.text_string_loc, payload)
    simple_input_page.submit_text_input(loc.text_string_loc)
    simple_input_page.check_invalid_result_text_input(loc.invalid_result_string, test_data.invalid_result_string)


@pytest.mark.parametrize('payload', invalidData1)
def test_invalid_1_input_text(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(loc.text_string_loc, payload)
    simple_input_page.submit_text_input(loc.text_string_loc)
    simple_input_page.check_invalid_1_result_text_input(loc.invalid_result_string, test_data.invalid_result_1_string)


@pytest.mark.parametrize('payload', invalidData25)
def test_invalid_25_input_text(simple_input_page, payload):
    simple_input_page.open_page()
    simple_input_page.send_keys_to_text_input(loc.text_string_loc, payload)
    simple_input_page.submit_text_input(loc.text_string_loc)
    simple_input_page.check_invalid_25_result_text_input(loc.invalid_result_string, test_data.invalid_result_25_string)
