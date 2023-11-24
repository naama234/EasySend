from datetime import timedelta
from telnetlib import EC

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import DATA_ELEMENTS_CLASS_NAME, PRICE_CLASS_NAME, COLOR_CSS_SELECTOR, PASSENGERS_ELEMENTS_CLASS_NAME, \
    MONTH_YEAR_CLASS_NAME, RIGHT_ARROW_ID, OK_SET_DATE_BUTTON_XPATH, SLIDER_CONTAINER_CLASS_NAME


def get_returning_date(departure_date):
    returning_date = departure_date + timedelta(days=7)
    returning_date_formatted = returning_date.strftime("%d %B %Y")
    return returning_date_formatted


class BookingPage:
    def __init__(self, browser):
        self.browser = browser
        date_elements = browser.find_elements(By.CLASS_NAME, DATA_ELEMENTS_CLASS_NAME)
        passengers_elements = browser.find_elements(By.CLASS_NAME, PASSENGERS_ELEMENTS_CLASS_NAME)
        self.departure_date = date_elements[0]
        self.returning_date = date_elements[1]
        self.price = browser.find_element(By.CLASS_NAME, PRICE_CLASS_NAME)
        self.color = browser.find_element(By.CSS_SELECTOR, COLOR_CSS_SELECTOR)
        self.adults_number = passengers_elements[0]
        self.children_number = passengers_elements[1]

    def set_price(self, desired_position):
        slider_container = self.browser.find_element(By.CLASS_NAME, SLIDER_CONTAINER_CLASS_NAME)
        slider_width = slider_container.size['width']
        range_min = 100
        range_max = 1800
        percentage = (desired_position - range_min) / (range_max - range_min)
        target_position = percentage * slider_width
        actions = ActionChains(self.browser)
        actions.drag_and_drop_by_offset(self.price, -target_position, 0).perform()

    def set_color(self, color):
        self.color.click()
        option = self.browser.find_element(By.XPATH, f"//li[text()='{color}']")
        option.click()

    def set_passengers_number(self, number):
        number_xpath = f"//li[text()='{number}']"
        option = WebDriverWait(self.browser, 10).until(EC.element_to_be_clickable((By.XPATH, number_xpath)))
        option.click()

    def set_adults_number(self, number):
        self.adults_number.click()
        self.set_passengers_number(number)

    def set_children_number(self, number):
        self.children_number.click()
        option_selector = f'#app > div > section.Hero__hero___1FDXn > div:nth-child(3) > div > div:nth-child(4) > ul > li:nth-child({number+1})'
        option_selector = self.browser.find_element(By.CSS_SELECTOR, option_selector)
        option_selector.click()

    def set_date(self, date):
        day, month, year = date.split(' ')
        while True:
            current_month_year = WebDriverWait(self.browser, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, MONTH_YEAR_CLASS_NAME))
            ).text
            if f'{month}' in current_month_year and f'{year}' in current_month_year:
                break
            right_arrow = self.browser.find_element(By.ID, RIGHT_ARROW_ID)
            right_arrow.click()
        day_element_xpath = f"//div[@data-react-toolbox='day'][.//span[text()='{day}']]"
        day_element = self.browser.find_element(By.XPATH, day_element_xpath)
        day_element.click()

    def set_departure_date(self, departure_date_formatted):
        self.departure_date.click()
        self.set_date(departure_date_formatted)
        save_departures_button = self.browser.find_element(By.XPATH, OK_SET_DATE_BUTTON_XPATH)
        save_departures_button.click()

    def set_returning_date(self, departure_date):
        self.returning_date.click()
        returning_date = get_returning_date(departure_date)
        self.set_date(returning_date)
        save_returning_date_button = self.browser.find_element(By.XPATH, OK_SET_DATE_BUTTON_XPATH)
        save_returning_date_button.click()
