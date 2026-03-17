from pages.base_page.base_page import BasePage


class SingleSelectPage(BasePage):

    page_url = 'elements/select/single_select'

    def check_select_input_language_required(self, locator):
        self.element_required(locator)


    def check_select_input_language_enabled(self, locator):
        self.check_element_enabled(locator)


    def click_button(self, locator):
        self.click(locator)



