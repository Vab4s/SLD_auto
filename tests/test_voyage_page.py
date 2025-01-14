import time
import pytest

from helpers.clear_timeline import clear_timeline
from helpers.close_all_notifications import close_all_notifications
from pages.voyage_page import VoyagePage

from locators.masterdata_locators import *
from pages.masterdata_page import MasterdataPage


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
             [('propellers', 1), ('main-engines', 1), ('auxiliary-engines', 2), ('boilers', 1), ('other-larger-consumers', 1)],
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
