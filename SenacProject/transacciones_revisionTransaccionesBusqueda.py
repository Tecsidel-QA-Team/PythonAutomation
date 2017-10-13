# -*- coding: utf-8 -*-

import unittest
import time
import os.path
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl, timet

class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Mavi_Repository\\transacciones_revisionTransacciones\\attachments\\")                   
        try:
            driver.get(HostbaseUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginpageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\transacciones_revisionTransacciones\\attachments\\loginpageSenac.jpeg")                    
            settings.loginPage("00001","00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homepageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\transacciones_revisionTransacciones\\attachments\\homepageSenac.jpeg")
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Transacciones")).perform()
            time.sleep(1)
            driver.find_element_by_link_text("Revisión de Transacciones").click()                                
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\revisionTransicionesPage_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\transacciones_revisionTransacciones\\attachments\\revisionTransicionesPage.jpeg")
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").clear()
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").send_keys("01/01/2017")
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_Button_transactions")
            time.sleep(3)
            driver.get_screenshot_as_file("E:\\Selenium\\revisionTransicionesResults_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\transacciones_revisionTransacciones\\attachments\\revisionTransicionesResults.jpeg")
            elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text                
            time.sleep(1.5)
            print("Busqueda Completa: "+ elementsFound)
            time.sleep(1)
        except:
            unittest.TestCase.fail(self, Exception)
            
if __name__== "__main__":
    unittest.main()