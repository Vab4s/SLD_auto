ELEMENT_SIDEBAR = ('xpath', '//div[@class="voyage-sidebar"]')

BUTTON_EDIT = ('xpath', '//anchor-button[@qa-id="btn-edit"]')

# Voyage report form
# Поле с названием "Voyage number"
LABEL_VOYAGE_DRAFT_NUMBER_FIELD = ('xpath', '//label[text()="Voyage number"]')
# Поле с параметром
INPUT_VOYAGE_DRAFT_NUMBER_PARAMETER = ('xpath', '//anchor-input[@qa-id="Voyage number"]')

# Поле с названием "Direction/Stage"
LABEL_VOYAGE_DRAFT_DIRECTION_FIELD = ('xpath', '//label[text()="Direction/Stage"]')
# Поле с параметром
MENU_VOYAGE_DRAFT_DIRECTION_PARAMETER = ('xpath', '//button[@qa-id="Direction/Stage"]')

# Поле с названием "Voyage name"
LABEL_VOYAGE_DRAFT_NAME_FIELD = ('xpath', '//label[text()="Voyage name"]')
# Поле с параметром
INPUT_VOYAGE_DRAFT_NAME_PARAMETER = ('xpath', '//anchor-input[@qa-id="Voyage name"]')


# Поле с названием "Name"
FIELD_CURRENT_VOYAGE_NAME_FIELD = ('xpath', '//div[@qa-id="voyage-name"]//child::div[@class="voyage-info__title"]')
# Поле с параметром
FIELD_CURRENT_VOYAGE_NAME_PARAMETER = ('xpath', '//div[@qa-id="voyage-name"]//child::div[@class="voyage-info__value"]')

# Поле с названием "Voyage number"
FIELD_CURRENT_VOYAGE_NUMBER_FIELD = ('xpath', '//div[@qa-id="voyage-id"]//child::div[@class="voyage-info__title"]')
# Поле с параметром
FIELD_CURRENT_VOYAGE_NUMBER_PARAMETER = ('xpath', '//div[@qa-id="voyage-id"]//child::div[@class="voyage-info__value"]')

# Поле с названием "Direction/Stage"
FIELD_CURRENT_VOYAGE_DIRECTION_FIELD = ('xpath', '//div[@qa-id="voyage-direction"]//child::div[@class="voyage-info__title"]')
# Поле с параметром
FIELD_CURRENT_VOYAGE_DIRECTION_PARAMETER = ('xpath', '//div[@qa-id="voyage-direction"]//child::div[@class="voyage-info__value"]')

# Поле с названием "Vessel status"
FIELD_CURRENT_VOYAGE_VESSEL_STATUS_FIELD = ('xpath', '//div[@qa-id="voyage-vessel-status"]//child::div[@class="voyage-info__title"]')
# Поле с параметром
FIELD_CURRENT_VOYAGE_VESSEL_STATUS_PARAMETER = ('xpath', '//div[@qa-id="voyage-vessel-status"]//child::div[@class="voyage-info__value"]')


BUTTON_CREATE_CHARTERPARTY = ('xpath', '//anchor-button[@qa-id="bеn-create-cp"]')


TOGGLE_ENABLE_ALL = ('xpath', '//anchor-toggle[@qa-id="btn-show-all"]')
# checked="true" - включен
# checked="false" - выключен

MENU_BUTTON_PORT = ('xpath', '//div[@qa-id="port-events"]')

BUTTON_PORT_DEPARTURE_EVENT = ('xpath', '//anchor-button[@qa-id="event_departure"]')
BUTTON_PORT_BUNKERING_REPORT = ('xpath', '//anchor-button[@qa-id="report_bunkering"]')
BUTTON_PORT_POSITION_REPORT = ('xpath', '//anchor-button[@qa-id="report_position_in_port"]')
BUTTON_PORT_END_OF_ANCHORAGE_EVENT = ('xpath', '//anchor-button[@qa-id="event_anchorage_end_wpl_w"]')
BUTTON_PORT_BEGIN_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_begin_in_port"]')
BUTTON_PORT_END_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_end_in_port"]')

MENU_BUTTONS_PORT_LIST = [BUTTON_PORT_DEPARTURE_EVENT,
                          BUTTON_PORT_BUNKERING_REPORT,
                          BUTTON_PORT_POSITION_REPORT,
                          BUTTON_PORT_END_OF_ANCHORAGE_EVENT,
                          BUTTON_PORT_BEGIN_OF_EMERGENCY_EVENT,
                          BUTTON_PORT_END_OF_EMERGENCY_EVENT]


MENU_BUTTON_RIVER_PASSAGE = ('xpath', '//div[@qa-id="pilotage-events"]')

BUTTON_RIVER_ARRIVAL_EVENT = ('xpath', '//anchor-button[@qa-id="event_arrival"]')
BUTTON_RIVER_BOSP_EVENT = ('xpath', '//anchor-button[@qa-id="event_sea_passage_begin"]')
BUTTON_RIVER_BEGIN_OF_PILOTAGE_EVENT = ('xpath', '//anchor-button[@qa-id="event_pilotage_begin"]')
BUTTON_RIVER_END_OF_PILOTAGE_EVENT = ('xpath', '//anchor-button[@qa-id="event_pilotage_end"]')
BUTTON_RIVER_ARRIVAL_PILOT_BOARDING_PLACE_EVENT = ('xpath', '//anchor-button[@qa-id="event_pilot_arrival"]')
BUTTON_RIVER_STS_OPL_REPORT = ('xpath', '//anchor-button[@qa-id="report_sts"]')
BUTTON_RIVER_BEGIN_OF_DRIFTING_EVENT = ('xpath', '//anchor-button[@qa-id="event_drifting_begin_w"]')
BUTTON_RIVER_BEGIN_OF_ANCHORAGE_EVENT = ('xpath', '//anchor-button[@qa-id="event_anchorage_begin_opl_w"]')
BUTTON_RIVER_ENTERING_CANAL_EVENT = ('xpath', '//anchor-button[@qa-id="event_canal_enter"]')
BUTTON_RIVER_LEAVING_CANAL_EVENT = ('xpath', '//anchor-button[@qa-id="event_canal_leave"]')
BUTTON_RIVER_POSITION_REPORT = ('xpath', '//anchor-button[@qa-id="report_position"]')
BUTTON_RIVER_BEGIN_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_begin_river"]')
BUTTON_RIVER_END_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_end_river"]')


MENU_BUTTON_SEA_PASSAGE = ('xpath', '//div[@qa-id="sea-events"]')

BUTTON_SEA_EOSP_EVENT = ('xpath', '//anchor-button[@qa-id="event_sea_passage_end"]')
BUTTON_SEA_POSITION_REPORT = ('xpath', '//anchor-button[@qa-id="report_position"]')
BUTTON_SEA_ENTERING_ECA_EVENT = ('xpath', '//anchor-button[@qa-id="event_eca_enter"]')
BUTTON_SEA_LEAVING_ECA_EVENT = ('xpath', '//anchor-button[@qa-id="event_eca_leave"]')
BUTTON_SEA_ENTERING_HRA_EVENT = ('xpath', '//anchor-button[@qa-id="event_hra_enter"]')
BUTTON_SEA_LEAVING_HRA_REPORT = ('xpath', '//anchor-button[@qa-id="event_hra_leave"]')
BUTTON_SEA_BEGIN_OF_DEVIATION_EVENT = ('xpath', '//anchor-button[@qa-id="event_deviation_begin"]')
BUTTON_SEA_END_OF_DEVIATIONE_EVENT = ('xpath', '//anchor-button[@qa-id="event_deviation_end"]')
BUTTON_SEA_BEGIN_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_begin_at_sea"]')
BUTTON_SEA_END_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_end_at_sea"]')
BUTTON_SEA_BEGIN_OF_DRIFTING_EVENT = ('xpath', '//anchor-button[@qa-id="event_drifting_begin_atsea"]')
BUTTON_SEA_BEGIN_OF_ANCHORAGE_SHELTERING_EVENT = ('xpath', '//anchor-button[@qa-id="event_anchorage_begin_opl_sheltering"]')


MENU_BUTTON_STOPPAGE = ('xpath', '//div[@qa-id="stoppage-events"]')

BUTTON_STOPPAGE_END_OF_DRIFTING_EVENT = ('xpath', '//anchor-button[@qa-id="event_drifting_end_w"]')
BUTTON_STOPPAGE_END_OF_ANCHORAGE_EVENT = ('xpath', '//anchor-button[@qa-id="event_anchorage_end_opl_w"]')
BUTTON_STOPPAGE_STS_OPL_CARGO_OPERATIONS_REPORT = ('xpath', '//anchor-button[@qa-id="report_sts"]')
BUTTON_STOPPAGE_BUNKERING_REPORT = ('xpath', '//anchor-button[@qa-id="report_bunkering"]')
BUTTON_STOPPAGE_POSITION_REPORT = ('xpath', '//anchor-button[@qa-id="report_position"]')
BUTTON_STOPPAGE_BEGIN_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_begin_stoppage"]')
BUTTON_STOPPAGE_END_OF_EMERGENCY_EVENT = ('xpath', '//anchor-button[@qa-id="event_emergency_end_stoppage"]')