from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pytest
from TestData import Data
from TestLocator import Locators
from time import sleep

class TestPIM5:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search5(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpName_Locator))).send_keys(Data.DataHRM().Emplo_Search)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpSearch_Loca))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Nick_Locator))).send_keys(Data.DataHRM().Nick_Name)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().OtID_Locator))).send_keys(Data.DataHRM().Other_ID)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().DrLNo_Locator))).send_keys(Data.DataHRM().DrLice_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().DrLEx_Locator))).send_keys(Data.DataHRM().DrLice_Ex)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().SSN_Locator))).send_keys(Data.DataHRM().SSN_NO)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().SIN_Locator))).send_keys(Data.DataHRM().SIN_NO)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Nat_Locator))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Mar_Locator))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().DOB_Locator))).send_keys(Data.DataHRM().DOB)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().GEN_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().MilSer_Loc))).send_keys(Data.DataHRM().Mil_Ser)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PerSave_Loc))).click()
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Blood_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().BloSav_Loc))).click()
        sleep(5)
        self.driver.execute_script("window.scrollBy(0, -500)")
        sleep(4)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : All the details in the Personal Detail Page are filled and its Visible')
