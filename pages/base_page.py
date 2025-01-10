from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from locators.modal_window_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def get_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_element_loading(self, element):
        self.wait.until(expected_conditions.visibility_of_element_located(element))

    def wait_element_in_dom(self, element):
        self.wait.until(expected_conditions.presence_of_element_located(element))

    def click_element(self, element):
        self.wait.until(expected_conditions.visibility_of_element_located(element))
        self.wait.until(expected_conditions.element_to_be_clickable(element)).click()

    def click_element_toggle(self, element_toggle):
        if 'anchor-toggle--checked' not in self.driver.find_element(*element_toggle).get_attribute('class'):
            self.click_element(element_toggle)

    def get_element_attributes(self, element):
        WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(element))
        new_element = self.driver.find_element(*element)
        return self.driver.execute_script(
            """
            let attr = arguments[0].attributes;
            let items = {}; 
            for (let i = 0; i < attr.length; i++) {
                items[attr[i].name] = attr[i].value;
            }
            return items;
            """,
            new_element
        )

    def get_element_existance(self, element):
        return self.wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element_unexistance(self, element):
        return self.wait.until(expected_conditions.invisibility_of_element_located(element))

    def get_element_parameter_equality(self, element, element_attribute, supposed_attribute):
        return supposed_attribute in self.driver.find_element(*element).get_attribute(element_attribute)

    def get_element_text_equality(self, element, supposed_text):
        return supposed_text in self.driver.find_element(*element).text

    def check_modal_window_existance(self, window_title):
        assert (self.get_element_existance(MODAL_WINDOW) and self.get_element_text_equality(MODAL_TITLE, window_title))

    def check_modal_window_unexistance(self):
        assert (self.wait.until(expected_conditions.invisibility_of_element_located(MODAL_WINDOW)))
