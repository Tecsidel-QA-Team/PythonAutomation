# -*- coding: utf-8 -*-

import unittest
import time

from Settingsfields_File import  Settingsfields_File , CaCUrl, timet
from selenium.webdriver.common.action_chains import ActionChains

    
        
class CAC_assignTagToExistingAccount(unittest.TestCase):
    accountClosed = False
    NumbVehC= False
    TagAssigned= False
    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        time.sleep(1)
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\assigningTagToAccount\\attachments\\")
        CAC_assignTagToExistingAccount.assignTagToExistingAccount(self)
        time.sleep(1)
        
        if self.accountClosed==True:
            print("No se puede asignar un Tag a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            self.fail("No se puede asignar un Tag a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            
        if self.NumbVehC==True:
            print("No se puede asignar un Tag a la cuenta "+self.accountNumbr[7:16]+" porque no hay vehículo asociado a la cuenta")
            self.fail("No se puede asignar un Tag a la cuenta "+self.accountNumbr[7:16]+" porque no hay vehículo asociado a la cuenta")
        
        if self.TagAssigned==True:
            print("ERROR AL ASIGNAR TAG a la cuenta: "+self.accountNumbr[7:16]+", "+self.confirmationMessage)
            self.fail("ERROR AL ASIGNAR TAG a la cuenta: "+self.accountNumbr[7:16]+", "+self.confirmationMessage)
        
        time.sleep(1)
        print("Se le asignado el el tag No."+self.tagIdNmbr+" a la cuenta "+self.accountNumbr[7:16]+" correctamente")
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])    

    def assignTagToExistingAccount(self):
        settings = self.settings
        driver = settings.driver
        driver.get(CaCUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\assigningTagToAccount\\attachments\\loginCACCVHPage.jpeg")
        settings.loginPage("00001","00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\assigningTagToAccount\\attachments\\homeCACCVHPage.jpeg")
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
        numberVehicles = driver.find_element_by_id("ctl00_ContentZone_lbl_vehicles").text
        NumbVeh = int(numberVehicles)
        if  NumbVeh==0:
            self.NumbVehC = True
            return
        else:
            self.NumbVehC = False
            settings.elementClick("ctl00_ContentZone_BtnTags")
            driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentMainPage"+timet+".jpeg");
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentMainPage.jpeg");
            time.sleep(1)
            vehCheck = settings.ranNumbr(0,NumbVeh-1)
            settings.elementClick("ctl00_ContentZone_chk_"+str(vehCheck))
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_btn_token_assignment")
            time.sleep(.50)
            driver.find_element_by_id("ctl00_ContentZone_txt_pan_token_txt_token_box_data").send_keys(str(settings.ranNumbr(1,99999)))
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_btn_init_tag")
            time.sleep(1.5)
            self.confirmationMessage = driver.find_element_by_id("ctl00_ContentZone_lbl_information").text
        if "ya tiene un título asignado" in self.confirmationMessage or "Este tag no está operativo" in self.confirmationMessage or "Este tag ya está asignado" in self.confirmationMessage or "Luhn incorrecto" in self.confirmationMessage:
            self.TagAssigned = True
            driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentPageErr"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentPageErr.jpeg")
            return
        else:
            self.TagAssigned = False
            tabVeh = vehCheck+2
            self.tagIdNmbr = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_m_table_members']/tbody/tr["+str(tabVeh)+"]/td[6]").text
            driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentPage.jpeg")
            
if __name__== "__main__":
    unittest.main()