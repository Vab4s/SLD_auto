import time

from pages.base_page import BasePage
from data.urls import VOYAGE_PAGE

from locators.base_locators import *
from locators.voyage_menu_locators import *
from locators.voyage_timeline_locators import *
from locators.modal_window_locators import *

from functions.fill_regular_fields import fill_regular_fields
from functions.fill_dropdown_menu import fill_dropdown_menu
from functions.fill_position import fill_position
from functions.fill_date_time import fill_date_time
from functions.fill_consumption import fill_consumption
from functions.fill_consumption_time import fill_consumption_time


class VoyagePage(BasePage):
    def go_to_voyage_page(self):
        self.go_to_url(VOYAGE_PAGE)
        self.wait_element_loading(ELEMENT_SIDEBAR)

    def switch_on_enable_all_toggle(self):
        self.wait_element_in_dom(TOGGLE_ENABLE_ALL)
        self.click_element_toggle_on_force(TOGGLE_ENABLE_ALL)

    def fill_current_voyage(self):
        self.click_element(BUTTON_EDIT)
        self.send_text_to_input_element(VOYAGE_DRAFT_VOYAGE_NUMBER_INPUT, '1')
        self.choose_drop_menu_item(VOYAGE_DRAFT_DIRECTION_STAGE_DROPMENU, VOYAGE_DRAFT_DIRECTION_STAGE_DROPMENU_ITEM)
        self.send_text_to_input_element(VOYAGE_DRAFT_VOYAGE_NAME_INPUT, '1')
        self.click_element(BUTTON_SAVE)
        self.click_element(BUTTON_VOYAGE_DRAFT_BACK)

    def create_voyage_event_report(self, element_event_report, supposed_text):
        self.click_element(element_event_report)
        assert (self.get_element_existance(MODAL_WINDOW) and self.get_element_text_equality(MODAL_TITLE, supposed_text))
        self.click_element(BUTTON_SUCCESS)

    def create_departure(self):
        self.create_voyage_event_report(BUTTON_PORT_DEPARTURE_EVENT, 'New voyage')

    def check_departure_created(self):
        assert (self.get_element_unexistance(MODAL_WINDOW)
                and self.get_element_existance(TIMELINE_EVENT)
                and self.get_element_existance(TIMELINE_REPORT)
                and self.get_element_text_equality(TIMELINE_EVENT_TITLE, 'Departure')
                and self.get_element_text_equality(TIMELINE_REPORT_TITLE, 'Departure report')
                and self.get_elements_text_equality(TIMELINE_EVENT_DATE, TIMELINE_REPORT_DATE)
                and self.get_elements_text_equality(TIMELINE_EVENT_TIME, TIMELINE_REPORT_TIME))

    def click_departure_report(self):
        departure_report = self.format_locator_with_one_parameter(TIMELINE_DEPARTURE_REPORT, 'Departure report')
        self.click_element(departure_report)

    def voyage_report_equipment_assertion(self, equipment_list):
        REPORT_EQUIPMENT_LOCATOR = ('xpath', '//div[text()="{}{}"]')
        REPORT_FORM = ('xpath', '//div[@qa-id="voyage-page"]')
        self.wait_element_loading(REPORT_FORM)
        for equipment_name, number_of_equipment in equipment_list:
            for number in range(1, number_of_equipment + 1):
                equipment_locator = self.format_locator_with_two_parameters(REPORT_EQUIPMENT_LOCATOR, equipment_name, number)
                assert self.driver.find_element(*equipment_locator).is_displayed()


    def fill_all_mandatory_fields(self):
        fill_dropdown_menu(self.driver)
        fill_regular_fields(self.driver)
        fill_position(self.driver)
        fill_date_time(self.driver)
        fill_consumption(self.driver)
        # fill_consumption_time(self.driver)
        time.sleep(3)
        self.click_element(BUTTON_SEND)
        # assert not self.driver.find_elements('xpath', '//*[contains(@class, "mandatory")]')