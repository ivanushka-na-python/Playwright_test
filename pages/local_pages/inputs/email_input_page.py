from pages.base_page.base_page import BasePage


class EmailInputPage(BasePage):


    page_url = 'elements/input/email'


    def send_keys_to_email_input(self, locator, test_data):
        self.send_keys(locator, test_data)


    def submit_email_input(self, locator):
        self.submit(locator)


    def check_valid_result_email_input(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def check_invalid_result_email_input(self, locator, test_data):
        self.check_result_text(locator, test_data)

