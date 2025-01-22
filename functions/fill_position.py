from random import randint

from selenium.webdriver.common.action_chains import ActionChains


def fill_position(driver):
    '''
    Просто заполняет единицами.
    Как отдельно заполнять градусы и минуты/секунды - не знаю.
    Мешает shadow root
    '''
    position_elements = driver.find_elements('xpath', '//anchor-coordinate-input[contains(@qa-id, "Position")]')
    for element in position_elements:
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        ActionChains(driver).click(element).send_keys('111').perform()

