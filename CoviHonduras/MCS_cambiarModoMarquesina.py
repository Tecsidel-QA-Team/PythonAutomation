# -*- coding: utf-8 -*-

import unittest
import time
from Settingsfields_File import  Settingsfields_File, mcsVersion, timet, MCSUrl

          
class MCS_cambiarModoMarquesina(unittest.TestCase):    
            
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
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
            driver.find_element_by_link_text("Cambiar señal de marquesina").click()
            time.sleep(.60)
            self.ModMar=""
            if settings.ranNumbr(0,1)==0:
                self.ModoMar = "Aspa"
                driver.find_element_by_link_text(self.ModoMar).click()
            else:
                self.ModoMar = "Flecha"            
                settings.elementClick("btn_showChangeLaneSignWindow_arrow")                     
               
            driver.get_screenshot_as_file("E:\\Selenium\\DetalleViaPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\DetalleViaPage.jpeg")
            operationWindow = driver.find_element_by_id("titlebar").text
            operationWindow = operationWindow.strip
            if operationWindow=="Error":
                errormessage = driver.find_Element_by_id("lbl_message").text
                print(operationWindow+": "+errormessage)
                self.fail(errormessage)
                return  
            time.sleep(1)  
            operationWindow2 = driver.find_element_by_id("lbl_alert_title").text            
            time.sleep(.60)            
            confirmMessage = driver.find_element_by_id("lbl_message").text
            driver.get_screenshot_as_file("E:\\Selenium\\cambiarMarquesinaResults"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_application\\attachments\\cambiarMarquesinaResults.jpeg")        
            print(operationWindow2+": "+confirmMessage+" a "+self.ModoMar)
            print("Pruebas hechas en la versión del MCS de CoviHonduras: "+mcsVer)
            time.sleep(1)                    
        except:
            self.fail()

if __name__== "__main__":
    unittest.main()    