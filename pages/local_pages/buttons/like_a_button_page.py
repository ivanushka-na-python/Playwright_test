from pages.base_page.base_page import BasePage


class LikeAButtonPage(BasePage):

    page_url = 'elements/button/like_a_button'



    def click_button(self, locator):
        self.click(locator)


    def check_button_enabled(self, locator):
        self.check_element_enabled(locator)


    def check_button_submitted(self, locator, test_data):
        self.check_result_text(locator, test_data)

