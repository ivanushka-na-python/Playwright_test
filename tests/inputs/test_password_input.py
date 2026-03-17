import pytest
from locators.inputs import inputs_loc as loc
from test_data.inputs import test_data_inputs as test_data
from test_data.inputs.test_data_inputs import validPayloadPassword as validDataPassword
from test_data.inputs.test_data_inputs import invalidPayloadPassword as invalidDataPassword

def test_check_h1_text(password_input_page):
    password_input_page.open()
    password_input_page.check_h1_text(loc.h1_loc, test_data.h1_text)


@pytest.mark.parametrize('payload', validDataPassword)
def test_valid_passwd_input(password_input_page, payload):
    password_input_page.open_page()
    password_input_page.send_keys_to_passwd_input(loc.passwd_input_loc, payload)
    password_input_page.submit_passwd_input(loc.passwd_input_loc)
    password_input_page.check_valid_result_passwd_input(loc.valid_result_element, payload)


@pytest.mark.parametrize('payload', invalidDataPassword)
def test_valid_passwd_input(password_input_page, payload):
    password_input_page.open_page()
    password_input_page.send_keys_to_passwd_input(loc.passwd_input_loc, payload)
    password_input_page.submit_passwd_input(loc.passwd_input_loc)
    password_input_page.check_invalid_result_passwd_input(loc.invalid_result_passwd, test_data.invalidPayloadPassword)
