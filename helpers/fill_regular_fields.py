import random
import time

from helpers.random_date import random_date
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

def fill_regular_fields(driver):
    regular_elements = driver.find_elements('xpath', '//anchor-input[contains(@class, "mandatory")]')
    for element in regular_elements:
        ActionChains(driver).scroll_to_element(element).click(element).perform()
        # получить placeholder
        element_placeholder = element.get_attribute('placeholder')
        # получить верхнюю и нижнюю границы
        # element_placeholder_min, element_placeholder_max = element_placeholder.split('-')[0], \
        #     element_placeholder.split('-')[1]

        # если указан диапазон, либо значение, то первый элемент в любом случае буде числом, отделённым знаком "-"
        # если в поле не диапазон, то первый элемент числом не будет
        element_placeholder_min = element_placeholder.split('-')[0]
        if element_placeholder_min.isdigit():
            element_placeholder_max = element_placeholder.split('-')[1]
            # определить тип границы (int, float)
            # можно сделать через if (if '.' in element_placeholder_max => float, else int)
            try:
                element_placeholder_max = int(element_placeholder_max)
                element_placeholder_min = int(element_placeholder_min)
                # ввести в поле int-значение в промежутке между верхней и нижней границей
                random_number = random.randint(element_placeholder_min, element_placeholder_max)
                element.send_keys(str(random_number))
            except ValueError:
                element_placeholder_max = float(element_placeholder_max)
                element_placeholder_min = float(element_placeholder_min)
                # ввести в поле float-значение в промежутке между верхней и нижней границей
                random_number = round(random.uniform(element_placeholder_min, element_placeholder_max), 1)
                element.send_keys(str(random_number))
        # except TypeError:
        #     element.send_keys('hello')
        else:
            element.send_keys('hello')