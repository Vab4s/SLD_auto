from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from locators.base_locators import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)

    def go_to_url(self, url):
        self.driver.get(url)

    def get_current_url(self):
        return self.driver.current_url

    def wait_element_loading(self, element):
        self.wait.until(expected_conditions.visibility_of_element_located(element))

    def wait_element_in_dom(self, element):
        self.wait.until(expected_conditions.presence_of_element_located(element))

    def click_element(self, element):
        # self.wait.until(expected_conditions.visibility_of_element_located(element))
        self.wait.until(expected_conditions.element_to_be_clickable(element)).click()

    def click_element_toggle_on(self, element_toggle):
        if 'anchor-toggle--checked' not in self.driver.find_element(*element_toggle).get_attribute('class'):
            self.click_element(element_toggle)

    # def get_element_attributes(self, element):
    #     WebDriverWait(self.driver, 5).until(expected_conditions.presence_of_element_located(element))
    #     new_element = self.driver.find_element(*element)
    #     return self.driver.execute_script(
    #         """
    #         let attr = arguments[0].attributes;
    #         let items = {};
    #         for (let i = 0; i < attr.length; i++) {
    #             items[attr[i].name] = attr[i].value;
    #         }
    #         return items;
    #         """,
    #         new_element
    #     )

    def get_element_existance(self, element):
        return self.wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element_unexistance(self, element):
        return self.wait.until(expected_conditions.invisibility_of_element_located(element))

    def get_element_parameter_equality(self, element, element_attribute, supposed_attribute):
        return supposed_attribute in self.driver.find_element(*element).get_attribute(element_attribute)

    # def get_element_text_equality(self, element, supposed_text):
    #     return supposed_text in self.driver.find_element(*element).text

    def get_element_text_equality(self, element, supposed_text):
        return supposed_text == self.driver.find_element(*element).text

    def get_elements_text_equality(self, element_one, element_two):
        return self.driver.find_element(*element_one).text == self.driver.find_element(*element_two).text




    def choose_drop_menu_item(self, menu, menu_item):
        self.click_element(menu)
        self.action.scroll_to_element(self.driver.find_element(*menu_item)).perform()
        self.click_element(menu_item)

    def format_locator_with_one_parameter(self, method_locator, parameter):
        method, locator = method_locator
        locator = locator.format(parameter)
        return (method, locator)

    def format_locator_with_two_parameters(self, method_locator, param_one, param_two):
        method, locator = method_locator
        locator = locator.format(param_one, param_two)
        return method, locator

    # В каком угаре я это сюда написал? Убери нахер, дурак, блять
    def click_save_button(self):
        self.click_element(BUTTON_SAVE)
