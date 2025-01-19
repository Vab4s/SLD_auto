from selenium.common import TimeoutException

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from functions.close_all_notifications import close_all_notifications

from locators.base_locators import *
from locators.voyage_timeline_locators import *

def clear_timeline(driver):
    wait = WebDriverWait(driver, 1, 0.1)
    close_all_notifications(driver)     # Закрыть все нотификашки
    while True:
        try:
            wait.until(expected_conditions.visibility_of_element_located(TIMELINE_ITEM_EVERY)).click()
            wait.until(expected_conditions.visibility_of_element_located(BUTTON_DELETE_MENU_ITEM)).click()
            wait.until(expected_conditions.visibility_of_element_located(BUTTON_SUCCESS)).click()
        except TimeoutException:
            break
