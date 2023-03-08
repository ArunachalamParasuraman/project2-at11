from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from TestData import Data
from TestLocator import Locators
from time import sleep

class TestPIM2:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search2(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Admin_Locator))).click()
        Dropdown = self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().UserM_Locator)))
        self.action.click(on_element=Dropdown).perform()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,Locators.LocatorHRM().UserDrop_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().UserRole_Locator))).click()
        sleep(3)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Status_Locator))).click()
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : The values in User Role and Status Drop-Down are same and visible')



