# -*- coding: utf-8 -*-

import unittest
import time

from Settingsfields_File import  Settingsfields_File , timet, CaCUrl
from selenium.webdriver.common.action_chains import ActionChains
import CAC_accountCreationWithVehicle

    
        
class CAC_assignVehicleToExistingAccount(unittest.TestCase):
    accountClosed = False
    NumbVehC= False    
    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        time.sleep(1)
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\assigningVehicleToAccount\\attachments\\")
        CAC_assignVehicleToExistingAccount.assigningVehcleToExistingAccount(self)
        if self.accountClosed==True:
            print("No se puede asignar un Vehículo a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            self.fail("No se puede asignar un Vehículo a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")                
        time.sleep(1)
        CAC_accountCreationWithVehicle.CAC_accountCreationWithVehicle.accountCreationWithVehicle(self)
        time.sleep(1)
        print("Se le asignado el vehículo con la matrícula " +self.matriNu+" a la cuenta "+self.accountNumbr[7:16]+" correctamente")
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])
    

    def assigningVehcleToExistingAccount(self):
        settings = self.settings
        driver = settings.driver
        driver.get(CaCUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\assigningVehicleToAccount\\attachments\\loginCACCVHPage.jpeg")
        settings.loginPage("00001", "00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\assigningVehicleToAccount\\attachments\\homeCACCVHPage.jpeg")
        self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
        time.sleep(2)                    
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")
        table = tableres.find_elements_by_tag_name("tr")
        selectAccount = settings.ranNumbr(2,len(table))
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        time.sleep(1)
        if "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        else:
            self.accountClosed = False
            settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
            
        time.sleep(.50)
    
if __name__== "__main__":
    unittest.main()