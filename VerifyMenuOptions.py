# coding=utf-8
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
import time
import unittest
import xlrd
from pyvirtualdisplay import Display
# -*- coding: utf-8 -*-


workbook = xlrd.open_workbook('DataMN.xlsx')
worksheet = workbook.sheet_by_index(0)
crcURL = worksheet.cell(1, 0).value
adjustResolution = worksheet.cell(1, 3).value

def AdjustResolution():
    display = Display(visible=0, size=(800, 800))
    display.start()

if adjustResolution == 1:
    AdjustResolution()


class Verify_MN_Menu_Options(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
       # self.driver.get('http://idwebtg.carsstage.org/#roadReports?timeFrame=TODAY&layers=roadReports%2CwinterDriving%2CweatherWarnings%2CotherStates')
        self.driver.get(crcURL)
        print ('\n') + "Test Verifying MN TG Web Menu Options"


    def test_idaho_menu(self):

        driver = self.driver

        # Login To The System
        element = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.ID, 'sign-in-link')))
        driver.find_element_by_id('sign-in-link').click()
        driver.find_element_by_id('userAccountEmail').send_keys('ryan.kavanaugh@crc-corp.com')
        driver.find_element_by_id('userAccountPassword').send_keys('test')
        driver.find_element_by_id('userAccountPassword').submit()

        # Check that the menu items are all present
        left_Panel_Wait = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//*[@title="Ryan’s Favorites"]')))
        # Personalize your 511
        assert (driver.find_element_by_xpath('//*[@title="Ryan’s Favorites"]').is_displayed()) == True, "Favorites not present"
        # All Reports
        assert driver.find_element_by_xpath('//*[@title="See all traffic reports and winter driving conditions"]').is_displayed(), "All Reports not present"
        # Google Traffic
        assert driver.find_element_by_xpath('//*[@title="See up-to-date traffic conditions"]').is_displayed(), "Google Traffic not present"
        # Cameras
        assert driver.find_element_by_xpath('//*[@title="See maps and lists of cameras and view camera images"]').is_displayed(), "Cameras not present"
        # Weather Stations
        assert driver.find_element_by_xpath('//*[@title="See maps and lists of weather stations and review weather data"]').is_displayed(), "Weather Stations not present"
        # Snow Plows
        assert driver.find_element_by_xpath('//*[@title="See maps and lists of snow plows and view plow images"]').is_displayed(), "Snow plows are not present"
        # Transit Routes
        assert driver.find_element_by_xpath('//*[@title="Metro Traffic Map"]'), "Metro Traffic Map not present"

        # Check that the menu options that open the Favorites panel is functioning properly (This text is more extensive for Idaho)
        # Favorites
        driver.find_element_by_xpath('//*[@title="Ryan’s Favorites"]').click()
        assert driver.find_element_by_id('favorites-content-area').is_displayed()
        time.sleep(1)
        home_Button_Wait = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.ID, 'homeBtn')))
        home_Button_Wait.click()


    def tearDown(self):
         self.driver.quit()


if __name__ == '__main__':
    unittest.main()
