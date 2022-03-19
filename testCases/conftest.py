import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    if browser == "chrome":
        s = Service("C:/BroswerDriver/Chrome/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("Launching Chrome browser.........")
    elif browser == "firefox":
        s = Service("C:/BroswerDriver/Chrome/chromedriver.exe")
        driver = webdriver.Chrome(service=s)
        print("Launching Firfox browser.........")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

########### PyTest HTML Report ############

def pytest_config(config):
    config._metadata['Project Name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Ganesh'

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)




