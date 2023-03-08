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

class TestPIM6:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.action = ActionChains(self.driver)
        self.driver.maximize_window()
        yield
        self.driver.close()
    
    def test_Search6(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpName_Locator))).send_keys(Data.DataHRM().Emplo_Search)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpSearch_Loca))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,Locators.LocatorHRM().ConDet_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Street1_Loc))).send_keys(Data.DataHRM().Street1)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Street2_Loc))).send_keys(Data.DataHRM().Street2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().City_Loc))).send_keys(Data.DataHRM().City)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().State_Loc))).send_keys(Data.DataHRM().State)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Post_Loc))).send_keys(Data.DataHRM().Post)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Country_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().HomeNo_Loc))).send_keys(Data.DataHRM().Home_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().MobNo_Loc))).send_keys(Data.DataHRM().Mobile_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().WorkNo_Loc))).send_keys(Data.DataHRM().Work_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Wemail_Loc))).send_keys(Data.DataHRM().W_Email)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Oemail_Loc))).send_keys(Data.DataHRM().O_Email)
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Con_Save))).click()
        sleep(4)
        self.driver.execute_script("window.scrollBy(0, -500)")
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : All the details in the Contact Detail Page are filled and its Visible')
