import pytest
from selenium import webdriver

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
    yield driver
    driver.quit()