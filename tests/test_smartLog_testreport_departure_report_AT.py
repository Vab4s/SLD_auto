from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

import time
import pytest

from functions.clear_timeline import clear_timeline
from functions.close_all_notifications import close_all_notifications

from functions.fill_consumption_time import fill_consumption_time
from functions.fill_consumption import fill_consumption
from functions.fill_regular_fields import fill_regular_fields
from functions.fill_dropdown_menu import *
from functions.fill_position import fill_position
from functions.fill_date_time import fill_date_time
from functions.fill_all_mandatory_fields import fill_all_mandatory_fields

from pages.voyage_page import VoyagePage
from pages.masterdata_page import MasterdataPage
from pages.init_page import InitPage

from locators.voyage_timeline_locators import *
from locators.masterdata_locators import *
from locators.base_locators import *



class TestCreateFirstDepartureEvent:
    def test_open_voyage_page(self, driver):
        voyage_page = VoyagePage(driver)
        voyage_page.go_to_voyage_page()

    def test_create_first_departure_report(self, driver):
        voyage_page = VoyagePage(driver)
        voyage_page.go_to_voyage_page()
        voyage_page.create_departure()
        voyage_page.check_departure_created()
        clear_timeline(driver)


class TestSectionsDependencyOnMasterData:
    @pytest.mark.parametrize(
        'vessel_type, engine_power_type, avalable_equipment, report_equipment, equipment_to_add, report_equipment_after_add_new_equipment',
        [
            ['lpg_tanker',  # vessel_type Выбор типа судна
             MAIN_ENGINE_POWER_TYPE_SHAFT_SUBMENU,  # engine_power_type Выбор типа основного двигателя
             [('propellers', 1), ('main-engines', 1), ('diesel-generators', 1), ('auxiliary-engines', 3),
              ('exhaust-gas-boilers', 1), ('gas-turbines', 1), ('gas-combustion-units', 1), ('boilers', 1),
              ('compressors-(cargo-care-usage)', 1), ('other-larger-consumers', 1),
              ('other-safety/emergency-consumers', 1), ('scrubbers', 1)],
             [('ME', 1), ('AE', 2), ('AB', 1), ('AC', 1)], # report_equipment Проверка оборудование в репорте]
             [(GAS_COMBUSTION_UNITS, 1)],
             [('ME', 1), ('AE', 2), ('AB', 1), ('AC', 1), ('GCU', 2)]
            ]
        ]
        )
    def test_check_that_only_equipment_which_were_added_to_master_data_are_shown_in_reports(self, driver, vessel_type, engine_power_type, avalable_equipment, report_equipment, equipment_to_add, report_equipment_after_add_new_equipment):
        '''
        voyage_page.click_report(event_index)
        Пока убрал за ненадобностью и усложнением.
        Написано для того, чтобы в таймлайне по индексу можно было выбрать конкретный ивент/репорт.
        Ивенты/репорты добавляются при создании ивентов/репортов ф-ей add_last_added_event_report_to_list из SLD

        clear_timeline(driver) # if MD locked
        voyage_page.create_departure() # if MD locked
        Добавлены ради корректной отработки теста
        MD должна быть разлочена
        '''
        masterdata_page = MasterdataPage(driver)
        masterdata_page.go_to_masterdata_page()

        masterdata_page.choose_menu_vessel_type(vessel_type)
        masterdata_page.choose_main_engine_power_type(engine_power_type)
        masterdata_page.masterdata_equipment_assertion(avalable_equipment)
        close_all_notifications(driver)
        masterdata_page.click_save_button()

        voyage_page = VoyagePage(driver)
        voyage_page.go_to_voyage_page()
        voyage_page.create_departure()
        voyage_page.click_departure_report()
        # voyage_page.click_report(event_index)
        voyage_page.voyage_report_equipment_assertion(report_equipment)

        clear_timeline(driver)  # if MD locked

        masterdata_page.go_to_masterdata_page()
        masterdata_page.add_masterdata_equipment(equipment_to_add)
        masterdata_page.click_save_button()

        voyage_page.go_to_voyage_page()
        voyage_page.create_departure()  # if MD locked
        voyage_page.click_departure_report()
        voyage_page.voyage_report_equipment_assertion(report_equipment_after_add_new_equipment)
        clear_timeline(driver)

    @pytest.mark.parametrize(
        'vessel_type, engine_power_type, avalable_equipment, report_equipment, equipment_to_add, report_equipment_after_add_new_equipment',
        [
            ['lpg_tanker',  # vessel_type Выбор типа судна
             MAIN_ENGINE_POWER_TYPE_DIESEL_SUBMENU,  # engine_power_type Выбор типа основного двигателя
             [('propellers', 1), ('main-engines', 2), ('auxiliary-engines', 2), ('boilers', 1),
              ('other-larger-consumers', 1)],
             [('ME', 1), ('AE', 2), ('AB', 1), ('AC', 1)],  # report_equipment Проверка оборудование в репорте]
             [(GAS_COMBUSTION_UNITS, 1)],
             [('ME', 1), ('AE', 2), ('AB', 1), ('AC', 1), ('GCU', 2)]
             ]
        ]
    )
    def all_available_equipment_which_are_added_in_md_are_shown_in_reports(self):
        pass

    def test_fillinf(self, driver):
        voyage_page = VoyagePage(driver)
        voyage_page.go_to_voyage_page()
        clear_timeline(driver)
        voyage_page.create_departure()
        voyage_page.fill_current_voyage()
        voyage_page.click_element(TIMELINE_REPORT)
        voyage_page.fill_all_mandatory_fields()
        # voyage_page.wait_element_loading(('xpath', '//div[contains(@qa-id, "report-form")]'))

        # masterdata_page = MasterdataPage(driver)
        # masterdata_page.go_to_masterdata_page()
        # fill_all_mandatory_fields(driver)
        # masterdata_page.fill_all_mandatory_fields()

        # fill_regular_fields(driver)
        # fill_dropdown_menu(driver)
        # fill_position(driver)
        # fill_date_time(driver)
        # fill_consumption(driver)
        # fill_consumption_time(driver)

        # voyage_page.click_element(BUTTON_SAVE_MENU_ITEM)
        # voyage_page.click_element(BUTTON_SEND)
        time.sleep(10)

    def test_tips(self, driver):
        init_page = InitPage(driver)
        init_page.go_to_init_page()
        init_page.flip_all_tips()
        init_page.initialization_guide_step()
        init_page.initialization_backup_step()
        init_page.initialization_voyage_settings_step()
        init_page.fill_all_mandatory_fields_MD()
        init_page.fill_all_mandatory_fields_ROB()
        init_page.initialization_finish_step()
        time.sleep(5)
