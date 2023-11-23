from selenium.webdriver.common.by import By
from CheckoutPage import CheckoutPage
import pytest
from constants import NAME, EMAIL, SSN, PHONE

@pytest.mark.usefixtures("login")
def test_book_ticket(browser, booking_page, selected_planet, file_path):
    book_button = selected_planet.find_element(By.XPATH, './/button[contains(text(), "Book")]')
    book_button.click()

    checkout_form = CheckoutPage(browser)
    checkout_form.fill_form(NAME, EMAIL, SSN, PHONE, file_path)
    checkout_form.check_terms_and_conditions()
    checkout_form.pay_now()
