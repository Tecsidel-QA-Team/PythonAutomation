# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from Settingsfields_File import  Settingsfields_File , matletT, timet, cocheModels, camionModels,\
    colorS
    
        
import CAC_accountCreationOnly


class CAC_accountCreationWithVehicle(unittest.TestCase):
    accountClosed = False
    NumbVeh= False    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver                
        CAC_accountCreationOnly.CAC_accountCreationOnly.accountCreation(self)
        time.sleep(1)
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(5)
        CAC_accountCreationWithVehicle.accountCreationWithVehicle(self)
        time.sleep(1)
        CAC_accountCreationWithVehicle.vehicleFieldsfilled(self, self.matriNu,self.vehtypeModel,self.vehtypeKind,colorS[settings.ranNumbr(0,len(colorS)-1)])
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\vehicleDataFilledPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationVehicle\\attachments\\vehicleDataFilledPage.jpeg")
        time.sleep(1);                                                
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(1.50);
        settings.elementClick("ctl00_ButtonsZone_BtnBack_IB_Label")
        time.sleep(1.50)
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(1.50)
        driver.get_screenshot_as_file("E:\\Selenium\\accountCreated"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationVehicle\\attachments\\accountCreated.jpeg")
        print("Se ha creado la cuenta: "+self.accountNumbr[7:16]+" correctamente y con el vehículo creado con la matricula: "+str(self.matriNu))
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:]);
        driver.close()
        
    def accountCreationWithVehicle (self):        
        settings = self.settings
        settings.elementClick("ctl00_ContentZone_BtnVehicles");
        driver = settings.driver
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\vehiclePage"+timet+".jpeg");
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountCreationVehicle\\attachments\\vehiclePage.jpeg");
        settings.elementClick("ctl00_ContentZone_BtnCreate");
        matNum = settings.ranNumbr(5000,9999);
        matlet = settings.ranNumbr(1,len(matletT))
        matlet1 = settings.ranNumbr(1,len(matletT))
        matlet2 = settings.ranNumbr(1,len(matletT))
        settings.selectDropDown("ctl00_ContentZone_cmb_vehicle_type")
        self.matriNu = str(matNum)+matletT[matlet:matlet+1]+matletT[matlet1:matlet1+1]+matletT[matlet2:matlet2+1]
        vehtype = Select(driver.find_element_by_id("ctl00_ContentZone_cmb_vehicle_type"))
        self.vehTypeS = vehtype.first_selected_option
        if self.vehTypeS.text =="Liviano":
            carSel = settings.ranNumbr(0,3)
            carModel = settings.ranNumbr(1,2)
            if cocheModels[0][carSel]=="Seat":
                carModelSel = 0
            if cocheModels[0][carSel]=="Volkswagen":
                carModelSel = 1
            if cocheModels[0][carSel]=="Ford":
                carModelSel = 2
            if cocheModels[0][carSel]=="Fiat":
                carModelSel = 3
            self.vehtypeModel = cocheModels[0][carSel]
            self.vehtypeKind = cocheModels[carModel][carModelSel]
        else:
            carSel = settings.ranNumbr(0,1)
            carModel = settings.ranNumbr(1,2)
            if camionModels[0][carSel]=="Mercedes-Benz":
                carModelSel = 0
            if camionModels[0][carSel]=="Scania":
                carModelSel = 1
            self.vehtypeModel = camionModels[0][carSel]
            self.vehtypeKind = camionModels[carModel][carModelSel]
        
        
    def vehicleFieldsfilled(self, Matricul, vehtypeM, vehtypeK, ColorT):
            driver = self.settings.driver
            time.sleep(1);
            driver.find_element_by_id("ctl00_ContentZone_text_plate_number").send_keys(Matricul)
            driver.find_element_by_id("ctl00_ContentZone_text_make").send_keys(vehtypeM)
            driver.find_element_by_id("ctl00_ContentZone_text_model").send_keys(vehtypeK)
            driver.find_element_by_id("ctl00_ContentZone_text_colour").send_keys(ColorT)
            
if __name__== "__main__":
    unittest.main()