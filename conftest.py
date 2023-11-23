import pytest
from selenium import webdriver
from datetime import datetime, timedelta
from selenium.webdriver.common.by import By
import os
from BookingPage import BookingPage
from constants import GALLERY_ITEMS_CLASS_NAME, GALLERY_ITEM_TITLE_CLASS_NAME


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def login(browser):
    browser.get("https://demo.testim.io")


@pytest.fixture
def departure_date():
    departure_date = datetime.now() + timedelta(days=60)
    departure_date_formatted = departure_date.strftime("%d %B %Y")
    return departure_date, departure_date_formatted


@pytest.fixture
def selected_planet(browser):
    planet = 'Babahoyo'
    gallery_items = browser.find_elements(By.CLASS_NAME, GALLERY_ITEMS_CLASS_NAME)
    for gallery_item in gallery_items:
        title_element = gallery_item.find_element(By.CLASS_NAME, GALLERY_ITEM_TITLE_CLASS_NAME)
        title_text = title_element.text
        if title_text == planet:
            return gallery_item


@pytest.fixture
def file_path():
    current_directory = os.getcwd()
    file_name = "Automated Testing - EasySend Candidate Exercise 2.pdf"
    file_path = os.path.join(current_directory, "files", file_name)
    return str(file_path)


@pytest.fixture
def booking_page(browser, departure_date):
    browser.implicitly_wait(10)
    booking_page = BookingPage(browser)
    booking_page.set_departure_date(departure_date[1])
    booking_page.set_adults_number(3)
    booking_page.set_price(1000)
    booking_page.set_children_number(2)
    booking_page.set_returning_date(departure_date[0])
    booking_page.set_color("Blue")
    return booking_page
