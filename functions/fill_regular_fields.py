import random
import time

def input_elements(driver, mandatory):
    if mandatory:
        regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input[contains(@class, "mandatory") and((@value="") or not (@value))]')
        regular_mandatory_input_elements_masterdata = driver.find_elements('xpath', '//div[contains(@class, "mandatory")]//anchor-input[(@value="") or not (@value)]')
        regular_mandatory_input_elements.extend(regular_mandatory_input_elements_masterdata)
    else:
        regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input[((@value="") or not (@value)) and not (contains(@qa-id, "search")) and (@disabled="false")]')

    return regular_mandatory_input_elements


def fill_regular_fields(driver, mandatory=True):
    # if mandatory:
    #     regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input[contains(@class, "mandatory")]')
    #     regular_mandatory_input_elements_masterdata = driver.find_elements('xpath', '//div[contains(@class, "mandatory")]//anchor-input')
    #     regular_mandatory_input_elements.extend(regular_mandatory_input_elements_masterdata)
    # else:
    #     regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input')

    regular_mandatory_input_elements = input_elements(driver, mandatory)
    # regular_mandatory_input_elements.reverse()
    for element in regular_mandatory_input_elements:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element)
        # ActionChains(driver).click(element).perform()
        element.click()
        # ActionChains(driver).scroll_to_element(element).click(element).perform()
        # if element.get_attribute('value'):
        #     continue

        # LABEL = element.find_element('xpath', './/ancestor::div//p')
        element_placeholder = element.get_attribute('placeholder')
        # если указан диапазон, либо значение, то первый элемент в любом случае буде числом, отделённым знаком "-"
        # если в поле не диапазон, то первый элемент числом не будет
        element_placeholder_min = element_placeholder.split('-')[0]
        if element_placeholder_min.isdigit():
            element_placeholder_max = element_placeholder.split('-')[1]
            try:
                element_placeholder_max = int(element_placeholder_max)
                element_placeholder_min = int(element_placeholder_min)
                random_number = random.randint(element_placeholder_min, element_placeholder_max)
                element.send_keys(str(random_number))
            except ValueError:
                element_placeholder_max = float(element_placeholder_max)
                element_placeholder_min = float(element_placeholder_min)
                random_number = round(random.uniform(element_placeholder_min, element_placeholder_max), 1)
                element.send_keys(str(random_number))
        else:
            if 'XXXX' in element_placeholder_min:
                print(len(element_placeholder_min))
                element.send_keys(random.randint(10 ** (len(element_placeholder_min) - 1), 10 ** len(element_placeholder_min) - 1))
            else:
                element.send_keys('text')

    # if mandatory:
    #     regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input[contains(@class, "mandatory") and ((@value="") or not (@value))]')
    #     regular_mandatory_input_elements_masterdata = driver.find_elements('xpath', '//div[contains(@class, "mandatory")]//anchor-input[(@value="") or not (@value)]')
    #     regular_mandatory_input_elements.extend(regular_mandatory_input_elements_masterdata)
    # else:
    #     regular_mandatory_input_elements = driver.find_elements('xpath', '//anchor-input[(@value="") or not (@value)]')

    regular_mandatory_input_elements = input_elements(driver, mandatory)

    if regular_mandatory_input_elements:
        fill_regular_fields(driver, mandatory)
