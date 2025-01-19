import random
import time

from functions.random_date import random_date
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.errorhandler import StaleElementReferenceException

from selenium.webdriver.common.action_chains import ActionChains

def fill_dropdown_menu(driver):
    """
    Выбор делается только из видимого меню
    Для всех остальных значений (прим - выбор порта) нужен рандомный скролл по элементу
    """
    elements = driver.find_elements('xpath', '//button[contains(@class, "dropdown__selector") and contains(@class, "mandatory")]')

    for element in elements:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)
        ActionChains(driver).click(element).perform()
        menu_elements = element.find_elements('xpath', './/following-sibling::div//anchor-menu-item')
        menu_element_choise = random.choice(menu_elements)
        # Заголовок поля
        label = element.find_element('xpath', './/parent::anchor-dropdown//parent::div//parent::div//label')
        print(label.text)
        menu_element_choise.click()

    # Проверка на появившиеся после выбора поля (при выборе Yes появляется новое поле с выбором прим. ред.)
    appears_elements = driver.find_elements('xpath', '//button[contains(@class, "dropdown__selector") and contains(@class, "mandatory")]')
    if appears_elements:
        fill_dropdown_menu(driver)
