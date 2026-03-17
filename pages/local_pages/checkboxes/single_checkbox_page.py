from pages.base_page.base_page import BasePage

class SingleCheckboxPage(BasePage):

    page_url = 'elements/checkbox/single_checkbox'


    def check_count_checkboxes(self, locator, test_data):
        self.check_count_elements(locator, test_data)


    def check_checkbox_by_icon(self, locator):
        self.click(locator)


    def check_checkbox_by_text(self, locator):
        self.click(locator)


    def check_result_checkbox_text(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def invisible_result_checkbox(self, locator):
        self.check_element_invisible(locator)


    def click_button(self, locator):
        self.click(locator)