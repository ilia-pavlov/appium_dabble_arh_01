from appium import webdriver
from constructor.application import Application


def before_scenario(context, scenario):
    desired_capabilities = {
        "platformName": "Android",
        "platformVersion": "9",  # MAXIMUM carefully with OS version
        "deviceName": "Android Emulator",
        "app": "/Users/iliapavlov/PycharmProjects/appium_dabble_arh_01/app/app-adjoy-staging-release.apk",
        "automationName": "UiAutomator1"

    }

    context.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
    context.driver.implicitly_wait(10)

    """
       "//*[@content-desk='Search Wikipedia']"
       """
    context.constructor = Application(context.driver)


def after_scenario(context, scenario):
    context.driver.quit()
