from selenium.webdriver.common.action_chains import ActionChains

def fill_consumption_time(driver):
    consumption_time = driver.find_elements('xpath', '//div[contains(@qa-id, "Bunkering lot name")]//ancestor::div[contains(@qa-id, "report-form-item")]//anchor-duration-input')
    for element_time in consumption_time:
        driver.execute_script("arguments[0].scrollIntoView({block: 'start'});", element_time)
        ActionChains(driver).click(element_time).send_keys('1').perform()
    driver.find_element('xpath', '//body').click()
