from pages.base_page import BasePage
from data.urls import VOYAGE_PAGE
from locators.base_locators import *
from locators.voyage_sidebar_locators import *
from locators.voyage_timeline_locators import *
from locators.modal_window_locators import *


class VoyagePage(BasePage):
    def go_to_voyage_page(self):
        self.go_to_url(VOYAGE_PAGE)
        self.wait_element_loading(ELEMENT_SIDEBAR)

    def click_enable_all_toggle(self):
        self.wait_element_in_dom(TOGGLE_ENABLE_ALL)
        self.click_element_toggle(TOGGLE_ENABLE_ALL)

    # def get_toggle_attributes(self):
    #     print(self.get_element_attributes(TOGGLE_ENABLE_ALL))

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

    # def click_report(self, event_index):
    #     required_event_locator = self.timeline_list[event_index][1]
    #     required_report = self.format_locator_with_one_parameter(REPORT, required_event_locator)
    #     self.click_element(required_report)

    def click_departure_report(self):
        DEPARTURE_REPORT = ('xpath', '//div[text()="Departure report"]//ancestor::div[contains(@qa-id, "timeline-report")]')
        self.click_element(DEPARTURE_REPORT)

    def voyage_report_equipment_assertion(self, equipment_list):
        REPORT_EQUIPMENT_LOCATOR = ('xpath', '//div[text()="{}{}"]')
        REPORT_FORM = ('xpath', '//div[@qa-id="voyage-page"]')
        self.wait_element_loading(REPORT_FORM)
        for equipment_name, number_of_equipment in equipment_list:
            for number in range(1, number_of_equipment + 1):
                equipment_locator = self.format_locator_with_two_parameters(REPORT_EQUIPMENT_LOCATOR, equipment_name, number)
                assert self.driver.find_element(*equipment_locator).is_displayed()
