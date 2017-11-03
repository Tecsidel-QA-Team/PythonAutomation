# -*- coding: utf-8 -*-

import unittest
import time
from Settingsfields_File import  Settingsfields_File, mcsVersion, timet, MCSUrl
from selenium.common.exceptions import NoAlertPresentException
 
          
class MCS_simulacionPaso(unittest.TestCase):    
            
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
        
    def test(self):   
        settings = self.settings
        driver=settings.driver               
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\")
        try:
            driver.get(MCSUrl)
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\loginMCSCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\loginMCSCVHPage.jpeg")
            mcsVer = driver.find_element_by_id(mcsVersion).text
            settings.loginPageMCS("00001","00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homeMCSCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\homeMCSCVHPage.jpeg")    
            time.sleep(2)
            settings.elementClick("lane_name_link_26")
            time.sleep(1)        
            driver.find_element_by_xpath("//*[@id='lyr_menu']/div[2]").click()
            time.sleep(.6)
            driver.find_element_by_link_text("Simulación de paso").click()
            time.sleep(.6)
            if self.isAlertPresent() == True:
                driver.switch_to_alert().accept()
        
            driver.get_screenshot_as_file("E:\\Selenium\\DetalleViaPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\DetalleViaPage.jpeg")
            operationWindow = driver.find_element_by_id("titlebar").text
            operationWindow = operationWindow.strip
            if operationWindow == "Error":
                errormessage = driver.find_element_by_id("lbl_message").textg
                print(operationWindow+": "+errormessage)
                self.fail(errormessage)
                return
             
            time.sleep(1)
            confirmMessage = driver.find_element_by_id("lbl_message").text        
            driver.get_screenshot_as_file("E:\\Selenium\\abrirViaResults"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\abrirViaResults.jpeg")
            operationWindow2 = driver.find_element_by_id("lbl_alert_title").text
            print(operationWindow2+": "+confirmMessage)        
            print("Pruebas hechas en la versión del MCS de CoviHonduras: "+mcsVer)
            time.sleep(1)     
            driver.close()               
        except:
            self.fail()

    def isAlertPresent (self):                                
        try:
            alert = self.settings.driver.switch_to_alert()
            alert.text
            if not alert is None:
                return True
            else:
                return False
              
        except NoAlertPresentException:
            time.sleep(2)
            return False  
        
if __name__== "__main__":
    unittest.main()  