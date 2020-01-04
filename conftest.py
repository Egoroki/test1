from tkinter import Image

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.remote import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def selenium_hub():
    return 'http://127.0.0.1:4445/wd/hub'


@pytest.fixture(scope='session', params=[DesiredCapabilities.CHROME])
# @pytest.fixture(scope='session', params=[DesiredCapabilities.CHROME, DesiredCapabilities.FIREFOX])
def connection(selenium_hub, request):
    d = webdriver.WebDriver(command_executor=selenium_hub, desired_capabilities=request.param)
    yield d
    d.close()


class Google:
    def __init__(self, d: webdriver.WebDriver):
        self.d = d
        self.d.set_window_size(1920, 1280)
        self.d.get('http://google.by')

    @property
    def logon_button(self):
        return self.d.find_element_by_xpath('//*[@id="gb_70"]')

    @property
    def login_input(self):
        return self.d.find_element_by_xpath('//input[@id="identifierId"]').text

    @login_input.setter
    def login_input(self, value):
        name_input = self.d.find_element_by_xpath('//input[@id="identifierId"]')
        name_input.send_keys(value)

    def logon(self, username, password):
        self.logon_button.click()
        WebDriverWait(self.d, 10).until(EC.presence_of_element_located((By.ID, "initialView")))
        self.login_input = username
        send_btn = self.d.find_element_by_xpath('//*[contains(text(), "Далей")]')
        send_btn.click()
        WebDriverWait(self.d, 10).until(
            EC.presence_of_all_elements_located((By.XPATH, "//*[contains(text(), \"Вітаем\")]")))
        import time
        time.sleep(3)
        pwd_input = self.d.find_element_by_xpath('//input[@type="password"]')
        pwd_input.send_keys(password)
        send_btn = self.d.find_element_by_xpath('//*[contains(text(), "Далей")]')
        send_btn.click()
        time.sleep(10000)

    def logoff(self):
        pass


@pytest.fixture(scope="session")
def app(connection):
    google = Google(connection)
    google.logon('egorokib@gmail.com', 'Egorokio1')
    yield google
    google.logoff()


def test_search(app):
    pass
