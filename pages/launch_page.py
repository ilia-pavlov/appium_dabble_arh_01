from selenium.webdriver.common.by import By

from pages.base_page import Page


class LaunchPage(Page):
    CREATE_ACCOUNT = (By.ID, 'com.adjoy.standalone.test2:id/btnCreateAccount')

    def tap_button_create_account(self):
        self.click(*self.CREATE_ACCOUNT)

    def tap_button_create_account(self):
        self.click(*self.CREATE_ACCOUNT)

    def tap_button_create_account(self):
        self.click(*self.CREATE_ACCOUNT)

    def tap_button_create_account(self):
        self.click(*self.CREATE_ACCOUNT)




