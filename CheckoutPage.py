
from selenium.webdriver.common.by import By

from constants import EMAIL_CSS_SELECTOR, NAME_CSS_SELECTOR, PHONE_CSS_SELECTOR, FILE_CSS_SELECTOR, SSN_XPATH, \
    CHECK_TERMS_AND_CONDITIONS_CLASS_NAME, PAY_BUTTON_CLASS_NAME


class CheckoutPage:
    def __init__(self, browser):
        self.browser = browser
        self.name = browser.find_element(By.CSS_SELECTOR, NAME_CSS_SELECTOR)
        self.email = browser.find_element(By.CSS_SELECTOR, EMAIL_CSS_SELECTOR)
        self.ssn = browser.find_element(By.XPATH, SSN_XPATH)
        self.phone = browser.find_element(By.CSS_SELECTOR, PHONE_CSS_SELECTOR)
        self.file_input = browser.find_element(By.CSS_SELECTOR, FILE_CSS_SELECTOR)

    def fill_form(self, name, email, ssn, phone, file_path):
        self.name.send_keys(name)
        self.email.send_keys(email)
        self.ssn.send_keys(ssn)
        self.phone.send_keys(phone)
        self.file_input.send_keys(file_path)

    def check_terms_and_conditions(self):
        checkbox = self.browser.find_element(By.CLASS_NAME, CHECK_TERMS_AND_CONDITIONS_CLASS_NAME)
        checkbox.click()

    def pay_now(self):
        pay_button = self.browser.find_element(By.CLASS_NAME, PAY_BUTTON_CLASS_NAME)
        pay_button.click()
