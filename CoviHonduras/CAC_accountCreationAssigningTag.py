# -*- coding: utf-8 -*-

import unittest
import time
from Settingsfields_File import  Settingsfields_File, timet
import CAC_accountCreationOnly
import CAC_accountCreationWithVehicle


class CAC_accountCreationAssigningTag(unittest.TestCase):
    errorTagAssignment = False
    tagIdNmbr = ""   
    
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings        
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\")
        CAC_accountCreationOnly.CAC_accountCreationOnly.accountCreation(self)
        time.sleep(1)         
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(5)
        CAC_accountCreationWithVehicle.CAC_accountCreationWithVehicle.accountCreationWithVehicle(self)
        time.sleep(1)
        CAC_accountCreationAssigningTag.accountCreationAssigningTag(self)
        time.sleep(1)
        if self.errorTagAssignment==True:
            print("ERROR AL ASIGNAR TAG a la cuenta: "+self.accountNumbr.substring(7, 16)+", "+self.confirmationMessage)
            self.fail("Tag Invalido: No se puede asignar un Tag al Vehiculo "+self.matriNu+" de la cuenta "+self.accountNumbr[7:16])
            return        
        print("Se ha creado la cuenta: "+self.accountNumbr[7:16]+" con un Vehiculo con la matricula "+self.matriNu+" y el tag asignado No.: "+ self.tagIdNmbr)
        time.sleep(3)
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])

    def accountCreationAssigningTag(self):
        settings = self.settings
        driver = settings.driver
        time.sleep(2)
        driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentMainPage"+timet+".jpeg");
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentMainPage.jpeg");
        settings.elementClick("ctl00_ContentZone_BtnTags")
        time.sleep(.5)
        settings.elementClick("ctl00_ContentZone_chk_0")
        time.sleep(.5)
        settings.elementClick("ctl00_ContentZone_btn_token_assignment")
        time.sleep(.5)
        driver.find_element_by_id("ctl00_ContentZone_txt_pan_token_txt_token_box_data").send_keys(str(settings.ranNumbr(1,99999)))
        time.sleep(.50)
        settings.elementClick("ctl00_ContentZone_btn_init_tag")
        time.sleep(.50)
        self.confirmationMessage = driver.find_element_by_id("ctl00_ContentZone_lbl_operation").text
        if "ya tiene un tag asignado" in str(self.confirmationMessage) or "Este tag no está operativo" in str(self.confirmationMessage) or "Este tag ya está asignado" in str(self.confirmationMessage) or "Luhn incorrecto" in str(self.confirmationMessage):
            self.errorTagAssignment = True
            driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentPageErr"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentPageErr.jpeg")
            return 
        else:
            self.tagIdNmbr = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_m_table_members']/tbody/tr[2]/td[6]").text
            driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationAssigningTag\\attachments\\tagAssignmentPage.jpeg")            
        time.sleep(1)
    
if __name__== "__main__":
    unittest.main()