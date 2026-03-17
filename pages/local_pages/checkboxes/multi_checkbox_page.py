from pages.base_page.base_page import BasePage



class MultiCheckboxPage(BasePage):

    page_url = 'elements/checkbox/mult_checkbox'


    def check_count_checkboxes(self, locator, count):
        self.check_count_elements(locator, count)


    def check_checkbox_by_icon(self, locator):
        self.click(locator)


    def check_checkbox_by_text(self, locator):
        self.click(locator)


    def check_many_checkboxes(self, *locator):
        for loc in locator:
            self.check_checkbox_by_icon(loc)


    def check_result_checkbox_text(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def click_button(self, locator):
        self.click(locator)


    def invisible_result_checkbox(self, locator):
        self.check_element_invisible(locator)


    def button_enabled(self, locator):
        self.check_element_enabled(locator)