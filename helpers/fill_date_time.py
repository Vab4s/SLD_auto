from random import randint
from helpers.random_date import random_date
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains


def fill_date_time(driver):
    date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]//*[contains(@class, "--mandatory")]')
    for element in date_time_elements:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)
        ActionChains(driver).click(element).perform()
        # ActionChains(driver).scroll_to_element(element).click(element).perform()
        if element.tag_name == 'anchor-date-picker':
            element.send_keys(random_date())
            driver.find_element('xpath', '//body').click()
        elif element.tag_name == 'anchor-time-picker':
            element.send_keys(randint(0, 100))
