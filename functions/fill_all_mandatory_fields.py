from pages.base_page import BasePage
import random
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

MENU_ITEM = ('xpath', './/following-sibling::div[@class="dropdown__list-container"]//anchor-menu-item')


def fill_all_mandatory_fields(driver):
    # олучение всех обязательных элементов (со значением "--mandatory" в классе)
    elements = driver.find_elements('xpath', '//*[contains(@class, "--mandatory")]')
    print(elements)
    print()
    # перебор всех найденных элементов
    for element in elements:
        time.sleep(1)
        ActionChains(driver).scroll_to_element(element).perform()
        time.sleep(1)
        print(element, element.tag_name, element.get_attribute('qa-id'), element.get_attribute('placeholder'))
        # если в теге присутствует параметр 'placeholder'
        if element.get_attribute('placeholder') is not None:
            print('!!! element.get_attribute placeholder is not None')
            # если элемент button

            # если элемент не button

            element_placeholder = element.get_attribute('placeholder')
            # получить placeholder
            # получить верхнюю и нижнюю границы
            element_placeholder_min, element_placeholder_max = element_placeholder.split('-')[0], \
            element_placeholder.split('-')[1]
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
            except TypeError:
                element.send_keys('hello')
        # иначе если в теге отсутствует параметр 'placeholder'
        else:
            print('!!!element.get_attribute placeholder is None')
            if element.tag_name == 'button':
                print('ELEMENT BUTTON')
                element.click()
                # Нужно ли добавить скролл выпадающего меню, т.к. при большом меню элементы будут подгружаться динамически и также динамически появляться в DOM
                # получение списка видимых элементов
                element_menu_visible_elements = element.find_elements(*MENU_ITEM)
                # нажимаем на рандомный видимый элемент

                choise = random.choice(element_menu_visible_elements)
                ActionChains(driver).scroll_to_element(choise).perform()
                choise.click()
                print('done')
            # если элемент - поле ввода даты
            elif element.tag_name == 'anchor-date-picker':
                # водим рандомную дату от минимального значения до сегодняшней даты
                print(element.tag_name, element.get_attribute('qa-id'), element.get_attribute('min'))
                element.send_keys('1')
            # если элемент - поле ввода времени
            # для репортов
            # пока не реализовывалось
            elif element.tag_name == 'anchor-time-picker':
                element.send_keys('1')
            # иначе если элемент - какое-либо другое поле ввода
            # пример - ввод MCR оборудования
            else:
                # получаем элемент
                inner_element = element.find_element('xpath', './/*[@placeholder]')
                element_placeholder = inner_element.get_attribute('placeholder')
                # вводим значение из диапазона laceholder
                element_placeholder_min, element_placeholder_max = element_placeholder.split('-')[0], \
                    element_placeholder.split('-')[1]
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
    if driver.find_elements('xpath', '//*[contains(@class, "--mandatory")]'):
        fill_all_mandatory_fields(driver)

# ВНИМАНИЕ!
# Fuel consumption
# Bunkering lot name
#
# Div, не имеет plaxeholder'a (первый else)
# Но нажимать нужно внутренний anchor-dropdown

# Ф-я поиска тегов
# Ф-я заполнения
# Ф-я нажатия на кнопку
# Ф-я выбора из списка
