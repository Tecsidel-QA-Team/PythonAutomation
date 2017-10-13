# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl, timet
from test.test_deque import fail

class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()        
        
    def test(self):
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\")        
        try:  
            driver.get(HostbaseUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginHostSenacPage_"+timet+".jpeg");
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\loginHostSenacPage.jpeg");
            time.sleep(1)                        
            settings.loginPage("00001", "00001")
            time.sleep(2)   
            driver.get_screenshot_as_file("E:\\Selenium\\homeSenacPage_"+timet+".jpeg");
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\homeSenacPage.jpeg");         
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
            time.sleep(1)
            ActionChains(driver).click(driver.find_element_by_link_text("Seleccionar cuenta")).perform()
            time.sleep(1)
            tagNumbr = "68989"
            driver.find_element_by_id("ctl00_ContentZone_Textbox_byTag").send_keys(tagNumbr)
            time.sleep(0.5)
            driver.find_element_by_id("ctl00_ButtonsZone_BtnSearch").click()
            time.sleep(3)
            nextPageS = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text            
            time.sleep(0.20);
            if nextPageS =="Selección de cuenta":
                errorSearch = driver.find_element_by_id("ctl00_LblError").text 
                if errorSearch.equal("Luhn incorrecto"):
                    time.sleep(0.50);
                    driver.get_screenshot_as_file("E:\\Selenium\\SearchErr"+timet+".jpeg");
                    driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\SearchErr.jpeg");
                    print("ERROR AL TRATAR DE BUSCAR TAG, debido a: " + errorSearch)
                    fail("ERROR BUSQUEDA TAG: "+errorSearch)
            else:
                time.sleep(3)
                driver.get_screenshot_as_file("E:\\Selenium\\seleccionarCuentabyTag_"+timet+".jpeg");
                driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\seleccionarCuentabyTag.jpeg");
                driver.find_element_by_id("ctl00_ContentZone_BtnVehicles").click()                
                time.sleep(1)                
                driver.get_screenshot_as_file("E:\\Selenium\\vehicleandTagAssigned_"+timet+".jpeg");
                driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionCuentas_SeleccionarCuenta\\attachments\\vehicleandTagAssigned.jpeg");
                print("La cuenta se ha visualizado correctamente");
                time.sleep(1);                                    
            
        except:           
            unittest.TestCase.fail(self, Exception)
            

if __name__== "__main__":
    unittest.main()        
