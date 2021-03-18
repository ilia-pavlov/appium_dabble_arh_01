from appium import webdriver
from selenium.webdriver.common.by import By


desired_capabilities = {
    "platformName": "Android",
    "platformVersion": "9",  # MAXIMUM carefully with OS version
    "deviceName": "Android Emulator",
    "app": "/Users/iliapavlov/PycharmProjects/appium_dabble_arh_01/app/app-adjoy-staging-release.apk",
    "automationName": "UiAutomator1"

}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_capabilities)
"""
"//*[@content-desk='Search Wikipedia']"
"""
driver.implicitly_wait(10)

next_button = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCreateAccount').click()
next_button = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCreateAccount').click()
next_button = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCreateAccount').click()
next_button = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCreateAccount').click()

phone_number = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/etSignUpPhone')
phone_number.clear()
phone_number.send_keys('482-537-9999')

date_of_birth = driver.find_element(By.ID, 'android:id/button1')
date_of_birth.click()
driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnSignUp').click()

driver.find_element(By.ID, 'android:id/button1').click()

sms_filed = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/etSmsCode')
sms_filed.clear()
sms_filed.send_keys('1131')

password_notice = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCancel')
password_notice.click()

password_field = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/llPasswordConainer')
password_field.clear()
password_field.send_keys('CGFAIeufl7658')

driver.press_keycode(66)

tap_finish_button = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnCreatePass')
tap_finish_button.click()

driver.implicitly_wait(5)
tap_no_thanks = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/btnLocationDecline')
tap_no_thanks.click()

driver.implicitly_wait(10)
home_screen = driver.find_element(By.ID, 'com.adjoy.standalone.test2:id/tvFeedSectionTitle').text
assert 'From Dabbl' in home_screen, f'Expected From Dabble should be in {home_screen}'

