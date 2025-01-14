from selenium.common import NoSuchElementException

from locators.base_locators import *

def enter_date_time(driver, date=None, time=None):
    while True:
        try:
            driver.find_element(*BUTTON_NOTIFICATION_CLOSE).click()
        except NoSuchElementException:
            break
