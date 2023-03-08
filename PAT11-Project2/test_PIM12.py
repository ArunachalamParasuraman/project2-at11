from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import pytest
from time import sleep
from TestData import Data
from TestLocator import Locators

class TestPIM12:
    @pytest.fixture
    def booting_function(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        self.wait = WebDriverWait(self.driver,20)
        self.action = ActionChains(self.driver)
        yield
        self.driver.close()
    
    def test_Search12(self,booting_function):
        self.driver.get(Data.DataHRM().url)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Username_Locator))).send_keys(Data.DataHRM().Username)
        self.wait.until(EC.presence_of_element_located((By.NAME,Locators.LocatorHRM().Password_Locator))).send_keys(Data.DataHRM().Password)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().LoginButtonLocator))).click()
        sleep(4)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PIM_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpName_Locator))).send_keys(Data.DataHRM().Emplo_Search)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().EmpSearch_Loca))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Edit_Locator))).click()
        self.wait.until(EC.presence_of_element_located((By.LINK_TEXT,Locators.LocatorHRM().Salary_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().SalAdd_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().SalComp_Loc))).send_keys(Data.DataHRM().Sal_Comp)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().PayFre_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Currency_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().Amount_Loc))).send_keys(Data.DataHRM().Amount)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM.SalCmnt_Loc))).send_keys(Data.DataHRM().Cmnt)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().InDDD_Loc))).click()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().AccNo_Loc))).send_keys(Data.DataHRM().Acc_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().AccTyp_Loc))).click()
        sleep(2)
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ARROW_DOWN).perform()
        self.action.send_keys(Keys.ENTER).perform()
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().RoutNo_Loc))).send_keys(Data.DataHRM().Rout_No)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().AmntIn_Loc))).send_keys(Data.DataHRM().Amount)
        sleep(2)
        self.wait.until(EC.presence_of_element_located((By.XPATH,Locators.LocatorHRM().SaveIn_Loc))).click()
        sleep(5)
        self.driver.execute_script("window.scrollBy(0, -500)")
        sleep(3)
        assert self.driver.title == 'OrangeHRM'
        print('SUCCESS : All the details in the Salary Detail Page are filled and its Visible')