def check_toggle(toggle_element, parameter, driver):
    if parameter not in driver.find_element(*toggle_element).get_attribute('class'):
        self.click_element(element_toggle)