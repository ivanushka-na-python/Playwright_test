import pytest
from locators.inputs import inputs_loc as loc
from test_data.inputs import test_data_inputs as test_data
from test_data.inputs.test_data_inputs import validPayloadEmail as validDataEmail
from test_data.inputs.test_data_inputs import invalidPayloadEmail as invalidDataEmail


def test_check_h1_text(email_input_page):
    email_input_page.open_page()
    email_input_page.check_h1_text(loc.h1_loc, test_data.h1_text)

@pytest.mark.parametrize('payload', validDataEmail)
def test_valid_email_input(email_input_page, payload):
    email_input_page.open_page()
    email_input_page.send_keys_to_email_input(loc.email_input_loc, payload)
    email_input_page.submit_email_input(loc.email_input_loc)
    email_input_page.check_valid_result_email_input(loc.valid_result_element, payload)

@pytest.mark.parametrize('payload', invalidDataEmail)
def test_invalid_email_input(email_input_page, payload):
    email_input_page.open_page()
    email_input_page.send_keys_to_email_input(loc.email_input_loc, payload)
    email_input_page.submit_email_input(loc.email_input_loc)
    email_input_page.check_invalid_result_email_input(loc.invalid_result_email, test_data.invalid_result_email)




