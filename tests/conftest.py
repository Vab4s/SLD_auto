import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# @pytest.fixture(params=['firefox', 'chrome'])
# def driver(request):
#     if request.param == 'firefox':
#         driver = webdriver.Firefox()
#     elif request.param == 'chrome':
#         driver = webdriver.Chrome()
#     yield driver
#     driver.quit()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    # driver.set_window_size(1920,1080)
    yield driver
    driver.quit()

# @pytest.fixture
# def driver():
#     chrome_options = Options()
#     chrome_options.add_argument("--headless=new")
#     driver = webdriver.Chrome(options=chrome_options)
#     driver.maximize_window()
#     yield driver
#     driver.quit()