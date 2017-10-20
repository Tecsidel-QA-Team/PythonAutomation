# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from Settingsfields_File import  Settingsfields_File , CaCUrl, timet, infoCuenta0, infoCuenta1, \
        companyf,RUCid,titulofield,namef, surnamef,addressf,cpf,countryf,emailf,nameOp, \
        lastNameOp,sexSelc,addressTec, cpAdress, phoneCel, workPhone, workPhone1,perPhone, \
        faxPhone, contactf


class CAC_accountCreationOnly(unittest.TestCase):
    accountClosed = False
    NumbVeh= False    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        CAC_accountCreationOnly.accountCreation(self)
        time.sleep(1)
        print("Se ha creado la cuenta: "+self.accountNumbr[7:16]+" correctamente")
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])
        
    def accountCreation(self):
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\CAC_accountCreationAlone\\attachments\\")
        try:
            driver.get(CaCUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_accountCreationAlone\\attachments\\loginCACCVHPage.jpeg")
            settings.loginPage("00001","00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_accountCreationAlone\\attachments\\homeCACCVHPage.jpeg")
            self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
            time.sleep(1)
            ActionChains(driver).move_to_element(driver.find_element_by_link_text("Seleccionar cuenta"))
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Crear cuenta")).perform()
            time.sleep(.50)
            driver.find_element_by_link_text("Prepago").click()                                
            time.sleep(1)
            self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
            driver.get_screenshot_as_file("E:\\Selenium\\accountCreationPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_accountCreationAlone\\attachments\\accountCreation.jpeg")
            time.sleep(.50)    
            selOpt = settings.ranNumbr(0,1)
            selOp = settings.ranNumbr(0,8)
            selOp2 = settings.ranNumbr(0,8)
            if selOpt==0:
                settings.elementClick(infoCuenta0)
                time.sleep(1)
                driver.find_element_by_id(RUCid).send_keys(str(settings.ranNumbr(10000000,90000000))+""+str(settings.ranNumbr(100000,9000000))+"")
                Select (driver.find_element_by_id(titulofield)).select_by_visible_text(sexSelc[selOp])
                driver.find_element_by_id(namef).send_keys(nameOp[selOp])
                driver.find_element_by_id(surnamef).send_keys(lastNameOp[selOp])
                driver.find_element_by_id(addressf).send_keys(addressTec[selOp])
                driver.find_element_by_id(cpf).send_keys(cpAdress[selOp])            
                driver.find_element_by_id(countryf).send_keys("España")
                driver.find_element_by_id(emailf).send_keys(nameOp[selOpt].lower()+"."+lastNameOp[selOpt].lower()+"@tecsidel.es")
                driver.find_element_by_id(phoneCel).send_keys(str(settings.ranNumbr(600000000,699999999)))
                driver.find_element_by_id(workPhone).send_keys(workPhone1[selOp])
                driver.find_element_by_id(perPhone).send_keys(str(settings.ranNumbr(900000000,999999999)))
                driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOp])                
                time.sleep(4)
            else:
                driver.find_element_by_id(infoCuenta1).click()
                driver.find_element_by_id(RUCid).send_keys(str(settings.ranNumbr(10000000,90000000))+""+str(settings.ranNumbr(100000,9000000)))
                time.sleep(1)
                driver.find_element_by_id(companyf).send_keys("Tecsidel, S.A")
                driver.find_element_by_id(contactf).send_keys(nameOp[selOp]+" "+lastNameOp[selOp]+", "+nameOp[selOp2]+" "+lastNameOp[selOp2])
                driver.find_element_by_id(addressf).send_keys(addressTec[2]);
                driver.find_element_by_id(cpf).send_keys(cpAdress[2]);
                driver.find_element_by_id(countryf).send_keys("España")
                driver.find_element_by_id(emailf).send_keys("info@tecsidel.es")
                driver.find_element_by_id(phoneCel).send_keys(str(settings.ranNumbr(600000000,699999999)))
                driver.find_element_by_id(workPhone).send_keys(workPhone1[2])
                driver.find_element_by_id(perPhone).send_keys(str(settings.ranNumbr(900000000,999999999)))
                driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOp])
                time.sleep(1) 
                
            settings.selectDropDown("ctl00_ContentZone_ctrlAccountData_cmb_groupFare_cmb_dropdown")
            time.sleep(1)        
            driver.get_screenshot_as_file("E:\\Selenium\\dataFilled"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_accountCreationAlone\\attachments\\dataFilled.jpeg")
            settings.elementClick("ctl00_ButtonsZone_BtnSave_IB_Label")
            time.sleep(3)
            nextPage = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
            time.sleep(3)
            self.assertEqual("Detalles del pago", nextPage)            
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
            time.sleep(2)
                            
        except : 
                unittest.TestCase.fail(self,Exception)

if __name__== "__main__":
    unittest.main()
        