# coding=utf-8
from selenium import webdriver
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common import action_chains, keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import unittest
import xlrd
from pprint import pprint
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


class Verify_MN_Layers(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get(crcURL)


    def test_presence_of_correct_layers(self):

        driver = self.driver
        driver.maximize_window()

        dropDownMenuWait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, 'layers-menu-dropdown-button')))
        driver.find_element_by_id('layers-menu-dropdown-button').click()

        #=================== Road Reports Verification 1
        # MN: CHECKED √
        menuItemsWait = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@id="layerSelector"]/ul/li[1]/a/span/img[1]')))
        roadReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[1]')
        roadReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", roadReports)
        self.assertIn('images/checkbox-checked.png', roadReportsOuterHTMLData)

        #=================== Winter Driving DOT 2
        # MN: CHECKED √
        winterDrivingReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[2]')
        winterDrivingOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", winterDrivingReports)
        self.assertIn('images/checkbox-checked.png', winterDrivingOuterHTMLData)

        #=================== Winter Driving Citizen 3
        # MN: CHECKED √
        weatherWarningsReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[3]')
        weatherWarningsReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", weatherWarningsReports)
        self.assertIn('images/checkbox-checked.png', weatherWarningsReportsOuterHTMLData)

        #=================== Weather Warnings Verification 4
        # MN: CHECKED
        trafficSpeedsReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[4]')
        trafficSpeedsReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", trafficSpeedsReports)
        self.assertIn('images/checkbox-checked.png', trafficSpeedsReportsOuterHTMLData)

        # =================== Flooding 5
        # MN: CHECKED
        eSignsReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[5]')
        eSignsReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", eSignsReports)
        self.assertIn('images/checkbox-checked.png', eSignsReportsOuterHTMLData)

        # =================== Traffic Speeds 6
        # MN: UNCHECKED
        mountainPassesReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[6]')
        mountainPassesReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", mountainPassesReports)
        self.assertIn('images/checkbox-unchecked.png', mountainPassesReportsOuterHTMLData)

        # =================== Cameras 7
        # MN: UNCHECKED
        cameraReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[7]')
        cameraReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", cameraReports)
        self.assertIn('images/checkbox-unchecked.png', cameraReportsOuterHTMLData)

        # =================== Weather Stations 8
        # MN: UNCHECKED
        weatherStationsReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[8]')
        weatherStationsReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", weatherStationsReports)
        self.assertIn('images/checkbox-unchecked.png', weatherStationsReportsOuterHTMLData)

        # =================== Other States' Info 9
        # MN: CHECKED
        restAreasReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[9]')
        restAreasReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", restAreasReports)
        self.assertIn('images/checkbox-checked.png', restAreasReportsOuterHTMLData)

        # =================== Plow Cameras 10
        # MN: UNCHECKED √
        otherStatesReports = driver.find_element_by_xpath('//*[@id="layerSelector"]/ul/li[10]')
        otherStatesReportsOuterHTMLData = driver.execute_script("return arguments[0].outerHTML;", otherStatesReports)
        self.assertIn('images/checkbox-unchecked.png', otherStatesReportsOuterHTMLData)


    def tearDown(self):
         print "Test Completed"
         self.driver.quit()


if __name__ == '__main__':
    print ('\n') + "Verifying MN TG Web Default Map Layers" + '\n'
    unittest.main()