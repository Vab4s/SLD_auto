import time

from pages.base_page import BasePage
from data.urls import VOYAGE_PAGE
from locators.base_locators import *
from locators.voyage_sidebar_locators import *
from locators.modal_window_locators import *


class VoyagePage(BasePage):
    def get_voyage_page(self):
        self.get_url(VOYAGE_PAGE)
        self.wait_element_loading(ELEMENT_SIDEBAR)

    def click_enable_all_toggle(self):
        self.wait_element_in_dom(TOGGLE_ENABLE_ALL)
        self.click_element_toggle(TOGGLE_ENABLE_ALL)

    # def get_toggle_attributes(self):
    #     print(self.get_element_attributes(TOGGLE_ENABLE_ALL))

    def create_departure(self):
        self.click_element(BUTTON_PORT_DEPARTURE_EVENT)
        assert (self.get_element_existance(MODAL_WINDOW) and self.get_element_text_equality(MODAL_TITLE, 'New voyage'))
        # self.check_modal_window_existance('New voyage')
        self.click_element(BUTTON_SUCCESS)
        self.check_modal_window_unexistance()
        # Проверка того, что существует ивент с названием Депаче и репорт с названием Депаче репорт