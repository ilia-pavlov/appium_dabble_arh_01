from selenium.webdriver.common.by import By

from pages.base_page import Page


class SignUpPage(Page):
    PHONE_FILED = (By.ID, 'com.adjoy.standalone.test2:id/etSignUpPhone')
    DATE_OF_BIRTH_PICKER = (By.ID, 'android:id/button1')
    SIGN_UP = (By.ID, 'com.adjoy.standalone.test2:id/btnSignUp')
    POP_UP_CONFIRM_PHONE = (By.ID, 'android:id/button1')
    ACCESS_FILED = (By.ID, 'com.adjoy.standalone.test2:id/etSmsCode')
    POP_UP_PASSWORD_TERMS = (By.ID, 'com.adjoy.standalone.test2:id/btnCancel')
    PASSWORD_FILED = (By.ID, 'com.adjoy.standalone.test2:id/llPasswordConainer')
    # driver.press_keycode(66)
    FINISH_BUTTON = (By.ID, 'com.adjoy.standalone.test2:id/btnCreatePass')
    NOT_THANKS = (By.ID, 'com.adjoy.standalone.test2:id/btnLocationDecline')
    HOME_SCREEN_Title = (By.ID, 'com.adjoy.standalone.test2:id/tvFeedSectionTitle')

    def input_phone_number(self, text: int):
        self.input(text, *self.PHONE_FILED)

    def tap_date_of_birth_picker(self):
        self.click(*self.DATE_OF_BIRTH_PICKER)

    def tap_button_sign_up(self):
        self.click(*self.SIGN_UP)

    def tap_pop_up_confirm_phone(self):
        self.click(*self.POP_UP_CONFIRM_PHONE)

    def input_passcode(self, passcode: int):
        self.input(passcode, *self.ACCESS_FILED)

    def tap_pop_up_password_terms(self):
        self.click(*self.POP_UP_PASSWORD_TERMS)

    def input_password(self, text: str):
        self.input(text, *self.PASSWORD_FILED)

    def tap_enter_on_keyboard(self, number: int):
        self.press_keycode(number)

    def tap_finish_button(self):
        self.click(*self.FINISH_BUTTON)

    def verify_title_on_home_screen(self, title: str):
        result_title = self.find_element(*self.HOME_SCREEN_Title).text
        assert title in result_title, f'Expected {title} should be in {result_title}'
