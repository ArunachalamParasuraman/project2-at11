from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
from time import sleep
from TestData import Data
from TestLocator import Locators

class TestPIM10:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search10(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpName_Locator))).send_keys(Data.DataHRM().Emplo_Search)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpSearch_Loca))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,Locators.LocatorHRM().Job_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Terminate_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM.TerminDate_Loc))).send_keys(Data.DataHRM().Termi_Date)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().TerminRea_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Note_Loc))).send_keys(Data.DataHRM().Note)
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().TerSave_Loc))).click()
        sleep(6)
        self.driver.execute_script("window.scrollBy(0, 300)")
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : TERMINATION on Job detail Page is Done and ACTIVATE EMPLOYMENT is Visible')

