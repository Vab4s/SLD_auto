import random
import time
from selenium.webdriver.support.ui import Select

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait

from selenium.webdriver.support import expected_conditions


def click_dropdown_menu_item(driver, menu_webelement, menu_items_locator):
    driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", menu_webelement)
    # ActionChains(driver).click(menu_webelement).perform()
    menu_webelement.click()
    menu_items = menu_webelement.find_elements(*menu_items_locator)
    # menu_item = random.choice(menu_items)
    try:
        menu_item = menu_items[1]
    except IndexError:
        menu_item = menu_items[0]
    menu_item.click()

def fill_dropdown_menu(driver):
    """
    Выбор делается только из видимого меню
    Для всех остальных значений (прим - выбор порта) нужен рандомный скролл по элементу
    """
    menus_elements = driver.find_elements('xpath', '//button[contains(@class, "dropdown__selector") and contains(@class, "mandatory")]')
    menus_elements_init_masterdata = driver.find_elements('xpath', '//div[contains(@class, "mandatory")]//anchor-dropdown')
    menu_items = ('xpath', './/following-sibling::div//anchor-menu-item')
    menus_elements.extend(menus_elements_init_masterdata)
    menus_elements.reverse()

    for element in menus_elements:
        click_dropdown_menu_item(driver, element, menu_items)
        # driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)
        # ActionChains(driver).click(element).perform()
        # menu_elements = element.find_elements('xpath', './/following-sibling::div//anchor-menu-item')
        # menu_element_choise = random.choice(menu_elements)
        # # Заголовок поля
        # label = element.find_element('xpath', './/parent::anchor-dropdown//parent::div//parent::div//label')
        # print(label.text)
        # menu_element_choise.click()

    # Проверка на появившиеся после выбора поля (при выборе Yes появляется новое поле с выбором прим. ред.)
    appears_elements = driver.find_elements('xpath', '//button[contains(@class, "dropdown__selector") and contains(@class, "mandatory")]')
    appears_menus_elements_init_masterdata = driver.find_elements('xpath', '//div[contains(@class, "mandatory")]//anchor-dropdown')
    appears_elements.extend(appears_menus_elements_init_masterdata)
    if appears_elements:
        fill_dropdown_menu(driver)
