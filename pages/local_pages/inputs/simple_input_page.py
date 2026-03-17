from pages.base_page.base_page import BasePage

class SimpleInputPage(BasePage):

    page_url = 'elements/input/simple'


    def send_keys_to_text_input(self, locator, test_data):
        self.send_keys(locator, test_data)


    def submit_text_input(self, locator):
        self.submit(locator)


    def check_valid_result_text_input(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def check_invalid_result_text_input(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def check_invalid_1_result_text_input(self, locator, test_data):
        self.check_result_text(locator, test_data)


    def check_invalid_25_result_text_input(self, locator, test_data):
        self.check_result_text(locator, test_data)


















    """дописать в классе pages общие методы, создать по классу на каждую страницу, назначить дочерние классы, 
    выписать локаторы и тестовые данные в отдельные файлы, собрать из всего сами вызовы методов, добавить фикстуры, 
    инициализирующие страницы сайта"""