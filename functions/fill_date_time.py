import time
from random import randint
from functions.random_date import random_date
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains


def fill_date_time(driver, mandatory=True):
    if mandatory:
        # найти незаполненные поля
        # date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]//*[contains(@class, "--mandatory") and ((@value="") or not (@value))]')
        # date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]/anchor-date-picker[contains(@class, "--mandatory") and ((@value="") or not (@value))]')
        # date_time_elements_masterdata = driver.find_elements('xpath', '//anchor-date-picker[contains(@class, "--mandatory") and ((@value="") or not (@value))]')
        date_time_elements = driver.find_elements('xpath', '//anchor-date-picker[contains(@class, "--mandatory") and ((@value="") or not (@value))]')
        # date_time_elements.extend(date_time_elements_masterdata)
    else:
        # date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]//*[(@value="") or not (@value)]')
        # date_time_elements = []
        date_time_elements = driver.find_elements('xpath', '//anchor-date-picker[(@value="") or not (@value)]')
        # date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]//*[(@value="") or not (@value)]')
        # date_time_elements.extend(date_time_elements)

    # date_time_elements = driver.find_elements('xpath', '//div[@class="date-time-picker"]//*[contains(@class, "--mandatory")]')
    # date_time_elements_masterdata = driver.find_elements('xpath', '//anchor-date-picker[contains(@class, "--mandatory")]')
    # date_time_elements.extend(date_time_elements_masterdata)
    for element in date_time_elements:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)
        element.click()
        # ActionChains(driver).scroll_to_element(element).click(element).perform()
        if element.tag_name == 'anchor-date-picker':
            element.send_keys(random_date())
            driver.find_element('xpath', '//body').click()
        elif element.tag_name == 'anchor-time-picker':
            element.send_keys(randint(0, 100))
            driver.find_element('xpath', '//body').click()
