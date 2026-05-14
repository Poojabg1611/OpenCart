import os
from datetime import datetime

import pytest
from selenium import webdriver

from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager


@pytest.fixture
def setup(browser):
    if browser == 'edge':
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
        print ("Launching Edge browser....")
    elif browser == "firefox":
        driver = webdriver.Firefox(GeckoDriverManager().install())
        print("Launching Firefox browser.....")
    else:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        print("Launching Chrome browser....")

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


######################### pytest HTML Report ############################

def pytest_configure(config):
    config._metadata['Project Name'] = 'OpenCart'
    config._metadata['Module Name'] = 'CustRegistration'
    config._metadata['Tester'] =  'Pavan'

## It is hook for delete/modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_Home", None)
    metadata.pop("Plugins", None)


#Specifying report folder location and save report with timestamp
@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    config.option.htmlpath = os.path.abspath(os.curdir)+"\\reports\\"+datetime.now().strftime("%d-%m-%y %H-%M-%S")+".html"