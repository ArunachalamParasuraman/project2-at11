from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from TestData import Data
from TestLocator import Locators
from time import sleep

class TestPIM3:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search3(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Admin_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().ADD_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().FName_Locator))).send_keys(Data.DataHRM().Name_F)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().MName_Locator))).send_keys(Data.DataHRM().Name_M)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().LName_Locator))).send_keys(Data.DataHRM().Name_L)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Toggle_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().UseLog_Locator))).send_keys(Data.DataHRM().Username_Log)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Enable_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PassLog_Locator))).send_keys(Data.DataHRM().Password_Log)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().CPasslog_Locator))).send_keys(Data.DataHRM().ConPass_Log)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Save_Locator))).click()
        sleep(10)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : User is created and page moved to Employee list')
