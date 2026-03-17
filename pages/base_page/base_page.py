from playwright.sync_api import Page, expect, Locator

class BasePage:
    base_url = 'https://www.qa-practice.com/'
    page_url = None


    def __init__(self, page: Page):
        self.page = page


    def open_page(self, url=None):
        if url is None:
            url = self.page_url
        if url.startswith('http'):
            full_url = url
        else:
            full_url = self.base_url + url
        self.page.goto(full_url)


    def check_h1_text(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def find_element(self, locator: str) -> Locator:
        return self.page.locator(locator)


    def check_count_elements(self, locator, num):
        return self.find_element(locator).count() == num


    def send_keys(self, locator, keys):
        element = self.find_element(locator)
        element.fill(keys)


    def select_option(self, locator, value):
        element = self.find_element(locator)
        element.select_option(value)


    def submit(self, locator):
        element = self.find_element(locator)
        element.press('Enter')


    def click(self, locator):
        element = self.find_element(locator)
        element.click()


    def check_result_text(self, locator, text):
        element = self.find_element(locator)
        expect(element).to_have_text(text)


    def check_element_enabled(self, locator):
        element = self.find_element(locator)
        expect(element).to_be_enabled()


    def check_element_invisible(self, locator):
        element = self.find_element(locator)
        expect(element).not_to_be_visible()


    def check_element_disabled(self, locator):
        element = self.find_element(locator)
        expect(element).to_be_disabled()


    def element_required(self, locator):
        element = self.find_element(locator)
        expect(element).to_have_attribute('required', '')


