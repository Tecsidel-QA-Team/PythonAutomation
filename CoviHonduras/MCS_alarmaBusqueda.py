# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from Settingsfields_File import  Settingsfields_File, mcsVersion, timet, MCSUrl


 
          
class MCS_alarmaBusqueda(unittest.TestCase):    
            
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\MCS_alarmaBusqueda\\attachments\\")
        try:
            driver.get(MCSUrl)
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\loginMCSCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_alarmaBusqueda\\attachments\\loginMCSCVHPage.jpeg")
            mcsVer = driver.find_element_by_id(mcsVersion).text
            settings.loginPageMCS("00001","00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homeMCSCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_alarmaBusqueda\\attachments\\homeMCSCVHPage.jpeg")    
            time.sleep(2)
            driver.find_element_by_xpath("//div[@onclick=\"dropdownmenu(this, event, menu3, '250px')\"]").click()
            driver.find_element_by_link_text("Ver alarmas").click()
            time.sleep(1)
            driver.switch_to_frame(0)
            driver.get_screenshot_as_file("E:\\Selenium\\verAlarmasPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_alarmaBusqueda\\attachments\\verAlarmasPage.jpeg")
            time.sleep(.50)
            month=settings.ranNumbr(0,11)
            self.days = 0
            if  month==0 or month == 2 or month == 4 or month == 6 or month == 7 or month == 8 or month == 11:
                self.days = settings.ranNumbr(0,30)
            elif month == 1:
                self.days = settings.ranNumbr(0,27)
            else:
                self.days = settings.ranNumbr(0,29)                
            Select(driver.find_element_by_id("cbDia1")).select_by_index(self.days)
            Select(driver.find_element_by_id("cbMes1")).select_by_index()
            settings.selectDropDown("cmb_type")
            time.sleep(1)        
            settings.elementClick("btn_search")
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\verAlarmasResults"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\MCS_alarmaBusqueda\\attachments\\verAlarmasResults.jpeg")
            time.sleep(1)
            elementsFound = driver.find_element_by_id("lbl_showing").text                
            time.sleep(1.5)
            print("Busqueda Completa: "+ elementsFound)
            print("Pruebas hechas en la versión del MCS de CoviHonduras: "+mcsVer)
            time.sleep(1)                    
        except:
            self.fail()
    
if __name__== "__main__":
    unittest.main()    
