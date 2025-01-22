import time

from pages.base_page import BasePage
from data.urls import INIT_PAGE
from locators.init_locators import *
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


class InitPage(BasePage):
    def go_to_init_page(self):
        self.go_to_url(INIT_PAGE)
        self.wait_element_loading(TIPS_IMG)

    def flip_all_tips(self):
        self.driver.delete_all_cookies()
        self.click_element(BUTTON_SUCCESS)
        self.click_element(BUTTON_SUCCESS)
        self.click_element(BUTTON_SUCCESS)

    def initialization_guide_step(self):
        self.click_element(BUTTON_SUCCESS)

    def initialization_backup_step(self):
        self.click_element(BUTTON_SUCCESS)

    def initialization_voyage_settings_step(self):
        self.click_element(BUTTON_SUCCESS)

    def fill_all_mandatory_fields_MD(self):
        fill_dropdown_menu(self.driver)
        fill_regular_fields(self.driver)

        fill_date_time(self.driver)
        time.sleep(1)
        # self.click_element(BUTTON_SAVE)
        self.click_element(BUTTON_SEND)
        self.click_element(BUTTON_SUCCESS)

    def fill_all_mandatory_fields_ROB(self):
        fill_dropdown_menu(self.driver)
        fill_regular_fields(self.driver)
        fill_date_time(self.driver)
        time.sleep(1)
        # self.click_element(BUTTON_SAVE)
        self.click_element(BUTTON_SEND)
        self.click_element(BUTTON_SUCCESS)

    def initialization_finish_step(self):
        self.click_element(BUTTON_SUCCESS)