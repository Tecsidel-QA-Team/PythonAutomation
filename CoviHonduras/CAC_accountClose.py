# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from Settingsfields_File import  Settingsfields_File , CaCUrl, timet


class CAC_accountClose(unittest.TestCase):
    accountClosed = False
    NumbVeh= False    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):        
        settings = self.settings        
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\")
        CAC_accountClose.accountClose(self)
        time.sleep(1)
        if self.accountClosed==True:
            print("No se puede cerrar la cuenta "+self.accountNumbr[7:16]+" porque ya est� cerrada")
            self.fail("No se puede cerrar la cuenta "+self.accountNumbr[7:16]+" porque ya está cerrada")
            
        if self.NumbVeh==True:
            print("No se puede cerrar la cuenta "+self.accountNumbr[7:16]+" porque tiene "+str(self.NumbVeh)+" vehículo/s asignado/s")
            self.fail("No se puede cerrar la cuenta "+self.accountNumbr[7:16]+" porque tiene "+self.NumbVeh+" veh�culo/s asignado/s")
        time.sleep(1)
        print("Se ha cerrado la cuenta "+self.accountNumbr[7:16]+" correctamente");
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:]);
        
    def accountClose(self):
        settings = self.settings
        driver = settings.driver
        driver.get(CaCUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\loginCACCVHPage.jpeg")
        settings.loginPage("00001", "00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\homeCACCVHPage.jpeg")
        self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
        time.sleep(2)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta")
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")        
        table = tableres.find_elements_by_tag_name("tr")            
        selectAccount = settings.ranNumbr(2,len(table))
        driver.get_screenshot_as_file("E:\\Selenium\\accountSearchPage"+timet+".jpg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\accountSearchPage.jpeg")
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\accountPage.jpeg")
        numberVehicles = driver.find_element_by_id("ctl00_ContentZone_lbl_vehicles").text
        time.sleep(1)
        if "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        else:
            self.accountClosed = False
        self.NumbVeh = int(numberVehicles)
        if self.NumbVeh>0:
            self.NumbVehC = True
            return;
        else:
            self.NumbVehC = False
            settings.elementClick("ctl00_ContentZone_BtnCloseAccount")
            time.sleep(.50)
            driver.find_element_by_id("ctl00_ContentZone_txtComment").send_keys("Esta Cuenta se cerrará")
            driver.get_screenshot_as_file("E:\\Selenium\\accountClosePage"+timet+".jpeg")    
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\accountClosePage.jpeg")
            settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
            time.sleep(.50)        
            time.sleep(1)    
            settings.elementClick("ctl00_ButtonsZone_BtnBack_IB_Label")
            driver.get_screenshot_as_file("E:\\Selenium\\accountClosedPage"+timet+".jpeg")    
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountClose\\attachments\\accountClosedPage.jpeg")
            time.sleep(1)
    
if __name__== "__main__":
    unittest.main()