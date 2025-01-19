import random
import time

from functions.random_date import random_date
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.action_chains import ActionChains

def fill_consumption(driver):
    equipment_fuel_lots = driver.find_elements('xpath', '//div[contains(@qa-id, "Bunkering lot name") and contains(@class, "mandatory")]')
    time_since_last_report = driver.find_element('xpath', '//anchor-duration-input[@qa-id="Time since last rep."]')
    hours_since_last_report = time_since_last_report.get_attribute('hours')
    minutes_since_last_report = time_since_last_report.get_attribute('minutes')

    equipment_fuel = list()
    for element in equipment_fuel_lots:
        equipment_fuel_lot_menu = element.find_element('xpath', './/anchor-dropdown')
        equipment_fuel_lot_consumption = element.find_element('xpath', './/following::div[contains(@qa-id, "consumption amount") and contains(@class, "mandatory")]//anchor-input')
        equipment_fuel.append((equipment_fuel_lot_menu, equipment_fuel_lot_consumption))

    for lot_menu, consumption in equipment_fuel:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", lot_menu)
        ActionChains(driver).click(lot_menu).perform()
        lot_menu_items = lot_menu.find_elements('xpath', './/anchor-menu-item')
        lot_menu_items_choice = random.choice(lot_menu_items)
        ActionChains(driver).scroll_to_element(lot_menu_items_choice).click(lot_menu_items_choice).perform()

        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", consumption)
        ActionChains(driver).click(consumption).perform()
        element_placeholder = consumption.get_attribute('placeholder')
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
            consumption.send_keys(random_number)
        except ValueError:
            element_placeholder_max = float(element_placeholder_max)
            element_placeholder_min = float(element_placeholder_min)
            # ввести в поле float-значение в промежутке между верхней и нижней границей
            random_number = round(random.uniform(element_placeholder_min, element_placeholder_max), 1)
            consumption.send_keys(random_number)

    # Почему-то не отрабаьывает этот кусок кода
    # Перенёс в отдельный файл
    # UPD: после заполнения расхода топлива и выбора лота это поле перестаёт быть mandatory----------▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼▼  вот тут
    # consumption_time = driver.find_elements('xpath', '//div[contains(@qa-id, "Bunkering lot name") and contains(@class, "mandatory")]//ancestor::div[contains(@qa-id, "report-form-item")]//anchor-duration-input')
    # for element_time in consumption_time:
    #     driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element_time)
    #     ActionChains(driver).click(element_time).send_keys('1').perform()
