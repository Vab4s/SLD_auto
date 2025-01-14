MD_LOAD_WAIT = ('xpath', '//div[@qa-id="ship-master-data-report"]')


SIDEBAR_MENU = ('xpath', '//section[@qa-id="settings-sidebar"]')

VESSEL_TYPE = ('xpath', '//button[@qa-id="Vessel type"]')
VESSEL_TYPE_SUBMENU = ('xpath', '//anchor-menu-item[@value="{}"]')

MAIN_ENGINE_POWER_TYPE = ('xpath', '//button[@qa-id="Main Engine power type"]')
MAIN_ENGINE_POWER_TYPE_SHAFT_SUBMENU = ('xpath', '//anchor-menu-item[@label="Conventional (shaft connected)"]')
MAIN_ENGINE_POWER_TYPE_DIESEL_SUBMENU = ('xpath', '//anchor-menu-item[@label="Diesel-Electric"]')



ADD_ITEM_BUTTON = ('xpath', '//div[contains(@qa-id, "{}")]//descendant::div[@class="add"]')
# ADD_BUTTON = ('xpath', '//div[contains(@qa-id, "report-form-item-propellers")]//descendant::div[@class="add"]')

ME_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-main-engines")]')
DIESEL_GENERATORS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-diesel-generators")]')
SHAFT_GENERATORS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-shaft-generators")]')
AE_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-auxiliary-engines")]')
EXHAUST_GAS_BOILERS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-exhaust-gas-boilers")]')
GAS_TURBINES_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-gas-turbines")]')
BOILERS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-boilers")]')
GAS_COMBUSTION_UNITS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-gas-combustion-units")]')
COMPRESSORS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-compressors")]')
OTHER_CONSUMERS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-other-larger-consumers-(non-safety/emergency)")]')
SCRUBBERS_FIELD = ('xpath', '//div[contains(@qa-id, "report-form-item-incinerators")]')

propellers = 'report-form-item-propellers'
ME = 'report-form-item-main-engines'
DIESEL_GENERATORS = 'report-form-item-diesel-generators'
SHAFT_GENERATORS = 'report-form-item-shaft-generators'
AE = 'report-form-item-auxiliary-engines'
EXHAUST_GAS_BOILERS = 'report-form-item-exhaust-gas-boilers'
GAS_TURBINES = 'report-form-item-gas-turbines'
BOILERS = 'report-form-item-boilers'
GAS_COMBUSTION_UNITS = 'report-form-item-gas-combustion-units'
COMPRESSORS = 'report-form-item-compressors'
OTHER_CONSUMERS = 'report-form-item-other-larger-consumers-(non-safety/emergency)'
SCRUBBERS = 'report-form-item-incinerators'