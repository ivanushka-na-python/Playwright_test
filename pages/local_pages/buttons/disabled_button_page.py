from pages.base_page.base_page import BasePage

class DisabledButtonPage(BasePage):

    page_url = 'elements/button/disabled'

    def check_button_disabled(self, locator):
        self.check_element_disabled(locator)


    def check_button_enabled(self, locator):
        self.check_element_enabled(locator)


    def select_enabled_option(self, locator, test_data):
        self.find_element(locator).select_option(test_data)


    def select_disabled_option(self, locator, test_data):
        self.find_element(locator).select_option(test_data)


    def click_button(self, locator):
        self.click(locator)


    def check_button_submitted(self, locator, test_data):
        self.check_result_text(locator, test_data)

