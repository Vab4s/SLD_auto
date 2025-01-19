from selenium.common import NoSuchElementException

from locators.base_locators import *

def close_all_notifications(driver):
    while True:
        try:
            driver.find_element(*BUTTON_NOTIFICATION_CLOSE).click()
        except NoSuchElementException:
            break
