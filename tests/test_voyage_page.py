import time
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


from pages.voyage_page import VoyagePage
from locators.voyage_sidebar_locators import *
from locators.modal_window_locators import *


class TestCreateFirstDepartureEvent:
    def test_open_voyage_page(self, driver):
        voyage_page = VoyagePage(driver)
        voyage_page.get_voyage_page()

    @pytest.mark.parametrize('MODAL_WINDOW',
                             [
                                 (MODAL_WINDOW)
                             ]
                             )
    def test_create_first_departure_report(self, driver, MODAL_WINDOW):
        voyage_page = VoyagePage(driver)
        voyage_page.get_voyage_page()
        voyage_page.create_departure()
        assert voyage_page.get_element_unexistance(MODAL_WINDOW)