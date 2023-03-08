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

class TestPIM7:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search7(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpName_Locator))).send_keys(Data.DataHRM().Emplo_Search)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpSearch_Loca))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,Locators.LocatorHRM().EmerCon_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmerADD_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EName_Loc))).send_keys(Data.DataHRM().E_Name)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Relat_Loc))).send_keys(Data.DataHRM().Relation)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EHomeNo_Loc))).send_keys(Data.DataHRM().EHOME_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EMobNo_Loc))).send_keys(Data.DataHRM().EMob_NO)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EworkNo_Loc))).send_keys(Data.DataHRM().EWork_No)
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().ESave_Loc))).click()
        sleep(5)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : All the details in the Emergency Contact Detail Page are filled and its Visible')
