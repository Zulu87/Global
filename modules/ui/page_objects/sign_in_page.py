
from modules.ui.page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class SignInPage(BasePage):
    URL = "https://github.com/login"
    
    def __init__(self):
        
        super().__init__()

    def go_to(self):
        
        self.driver.get(SignInPage.URL)


    def try_login(self, username, password):
        
        #знаходимо поле для вводу пошти
        login_elem = self.driver.find_element (By.ID, "login_field")
        
        #вводимо пошту
        login_elem.send_keys (username)

        #знаходимо поле для вводу паролю
        pass_elem = self.driver.find_element (By.ID, "password")

        pass_elem.send_keys (password)

        #знаходимо кнопку sighIn
        btn_elem = self.driver.find_element (By.NAME, "commit")

        btn_elem.click ()

    
    def check_title(self, expected_title):
        
        return self.driver.title == expected_title