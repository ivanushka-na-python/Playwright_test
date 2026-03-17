import pytest

from pages.local_pages.buttons.disabled_button_page import DisabledButtonPage
from pages.local_pages.buttons.like_a_button_page import LikeAButtonPage
from pages.local_pages.buttons.simple_button_page import SimpleButtonPage
from pages.local_pages.checkboxes.multi_checkbox_page import MultiCheckboxPage
from pages.local_pages.checkboxes.single_checkbox_page import SingleCheckboxPage
from pages.local_pages.inputs.simple_input_page import SimpleInputPage
from pages.local_pages.inputs.email_input_page import EmailInputPage
from pages.local_pages.inputs.password_input_page import PasswordInputPage
from pages.local_pages.selects.single_select_page import SingleSelectPage


# @pytest.fixture
# def pages(page):
#     return {
#         SimpleInputPage(page),
#         EmailInputPage(page),
#         PasswordInputPage(page),
#         SimpleButtonPage(page),
#         LikeAButtonPage(page),
#         DisabledButtonPage(page)
#      }


@pytest.fixture
def simple_input_page(page):
    return SimpleInputPage(page)

@pytest.fixture
def email_input_page(page):
    return EmailInputPage(page)

@pytest.fixture
def password_input_page(page):
    return PasswordInputPage(page)

@pytest.fixture
def simple_button_page(page):
    return SimpleButtonPage(page)

@pytest.fixture
def like_a_button_page(page):
    return LikeAButtonPage(page)

@pytest.fixture
def disabled_button_page(page):
    return DisabledButtonPage(page)

@pytest.fixture
def single_checkbox_page(page):
    return SingleCheckboxPage(page)

@pytest.fixture
def multi_checkbox_page(page):
    return MultiCheckboxPage(page)

@pytest.fixture
def single_select_page(page):
    return SingleSelectPage(page)

