import time

from pages.base_page import BasePage
from data.urls import SETTINGS_MASTERDATA_PAGE
from locators.base_locators import *
from locators.voyage_menu_locators import *
from locators.masterdata_locators import *
from locators.modal_window_locators import *

from selenium.common import NoSuchElementException

from functions.fill_regular_fields import fill_regular_fields
from functions.fill_dropdown_menu import fill_dropdown_menu
from functions.fill_position import fill_position
from functions.fill_date_time import fill_date_time
from functions.fill_consumption import fill_consumption
from functions.fill_consumption_time import fill_consumption_time


class MasterdataPage(BasePage):
    def go_to_masterdata_page(self):
        self.go_to_url(SETTINGS_MASTERDATA_PAGE)
        self.wait_element_loading(MD_LOAD_WAIT)

    def choose_menu_vessel_type(self, vessel_type):
        vessel = self.format_locator_with_one_parameter(VESSEL_TYPE_SUBMENU, vessel_type)
        self.choose_drop_menu_item(VESSEL_TYPE, vessel)

        try:
            self.driver.find_element(*BUTTON_SUCCESS).click()
        except NoSuchElementException:
            pass

    def choose_main_engine_power_type(self, engine_power_type):
        self.choose_drop_menu_item(MAIN_ENGINE_POWER_TYPE, engine_power_type)

    def masterdata_equipment_assertion(self, equipment_list):
        MASTERDATA_EQUIPMENT_LOCATOR = ('xpath', '//div[contains(@qa-id, "report-form-item-{}")]//descendant::div[contains(@qa-id, "ame-")]')
        REPORT_FORM = ('xpath', '//div[@class="report-form"]')
        self.wait_element_loading(REPORT_FORM)
        for equipment, number in equipment_list:
            equipment_locator = self.format_locator_with_one_parameter(MASTERDATA_EQUIPMENT_LOCATOR, equipment)
            print(f'equipment: {equipment}\nequipment_locator: {equipment_locator}\nlen(self.driver.find_elements(*equipment_locator)): {len(self.driver.find_elements(*equipment_locator))}\nnumber: {number}')
            assert len(self.driver.find_elements(*equipment_locator)) == number
            print(equipment, number)


    def add_masterdata_equipment(self, equipment_list):
        ADD_ITEM_BUTTON = ('xpath', '//div[contains(@qa-id, "{}")]//descendant::div[@class="add"]')
        # указываем эквип и количество, которое нужно добавить (ME, 2)
        REPORT_FORM = ('xpath', '//div[@class="report-form"]')
        self.wait_element_loading(REPORT_FORM)
        for equipment, number in equipment_list:
            equipment_locator = self.format_locator_with_one_parameter(ADD_ITEM_BUTTON, equipment)
            for i in range(number):
                self.click_element(equipment_locator)

    def click_save_button(self):
        self.click_element(BUTTON_SAVE)


    def fill_all_mandatory_fields(self):
        fill_regular_fields(self.driver)
        # fill_dropdown_menu(self.driver)
        # fill_position(self.driver)
        # fill_date_time(self.driver)
        # time.sleep(10)
        # fill_consumption(self.driver)
        # fill_consumption_time(self.driver)
        # self.click_element(BUTTON_SAVE)
        # self.click_element(BUTTON_SEND)