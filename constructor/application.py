from pages.launch_page import LaunchPage
from pages.sign_up_page import SignUpPage


class Application:

    def __init__(self, driver):
        self.launch_page = LaunchPage(driver)
        self.sign_up_page = SignUpPage(driver)
