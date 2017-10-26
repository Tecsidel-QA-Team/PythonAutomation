# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from Settingsfields_File import  Settingsfields_File , timet, nameOp,lastNameOp,addressTec,\
    cpAdress, townC,workPhone1,sexSelc, genderS, BoHostUrl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
import pypyodbc
          
class BOHost_operatorCreation(unittest.TestCase):   
    lastCreated = ""
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\")
        try:
            driver.get(BoHostUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginBOCVHPage"+timet+".jpg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\loginBOCVHPage.jpeg")
            settings.loginPage("00001", "00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homeBOVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\homeBOVHPage.jpeg")
            self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
            time.sleep(2)     
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Configuración sistema")).perform()
            time.sleep(1)
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Operadores")).perform()
            time.sleep(.50)
            driver.find_element_by_link_text("Gestión de operadores").click()                                
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\gestionOperadoresPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\gestionOperadoresPage.jpeg")
            time.sleep(.50)        
            settings.elementClick("ctl00_ContentZone_BtnCreate")
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\crearOperadoresPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\crearOperadoresPage.jpeg")
            userSel = settings.ranNumbr(0,len(nameOp)-1)
            Select(driver.find_element_by_id("ctl00_ContentZone_cmb_title_cmb_dropdown")).select_by_visible_text(sexSelc[userSel])
            time.sleep(.100)
            Select(driver.find_element_by_id("ctl00_ContentZone_cmb_gender_cmb_dropdown")).select_by_visible_text(genderS[userSel])
            driver.find_element_by_id("ctl00_ContentZone_forename_box_data").send_keys(nameOp[userSel])
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_surname_box_data").send_keys(lastNameOp[userSel])
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_txt_address_box_data").send_keys(addressTec[userSel])
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_txt_postcode_box_data").send_keys(cpAdress[userSel])
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_txt_city_box_data").send_keys(townC[userSel])
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_txt_country_box_data").send_keys("España")
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_email_box_data").send_keys(nameOp[userSel].lower()+"."+lastNameOp[userSel].lower()+"@tecsidel.es")
            driver.find_element_by_id("ctl00_ContentZone_txt_phone_box_data").send_keys(workPhone1[userSel])
            settings.selectDropDown("ctl00_ContentZone_group_cmb_dropdown")
            time.sleep(.100)
            settings.selectDropDown("ctl00_ContentZone_cmb_typeDoc_cmb_dropdown")
            time.sleep(1)
            Docselected = Select (driver.find_element_by_id("ctl00_ContentZone_group_cmb_dropdown"))
            DocSelectedText  = Docselected.first_selected_option.text
            if DocSelectedText == "TI":
                driver.find_element_by_id("ctl00_ContentZone_txt_numberDoc_box_data").send_keys(str(settings.ranNumbr(1000000,90000000))+str(settings.ranNumbr(1000000,9000000)))
            else:
                driver.find_element_by_id("ctl00_ContentZone_txt_numberDoc_box_data").send_keys(str(settings.ranNumbr(10000000,900000000))+str(settings.ranNumbr(1000000,9000000)))
            time.sleep(1)
            operatorGroup = Select (driver.find_element_by_id("ctl00_ContentZone_group_cmb_dropdown"))
            self.operatorG = operatorGroup.first_selected_option.text        
            driver.find_element_by_id("ctl00_ContentZone_dt_birth_box_date").clear()
            driver.find_element_by_id("ctl00_ContentZone_dt_birth_box_date").send_keys('{:%d/%m/%Y}'.format(settings.dateSel("01/01/1970", "31/12/1980","%d/%m/%Y")))
            time.sleep(3)
            driver.find_element_by_id("ctl00_ContentZone_password_box_data").send_keys("00001")
            driver.find_element_by_id("ctl00_ContentZone_password2_box_data").send_keys("00001")
            time.sleep(5)
            driver.get_screenshot_as_file("E:\\Selenium\\allfilleddata"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\allfilleddata.jpeg")
            settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\userCreated"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\suserCreated.jpeg")
            tableResult = driver.find_element_by_id("ctl00_ContentZone_TblResults")
            userResults = tableResult.find_elements_by_tag_name("tr")
            
            if len(userResults)< 14:
                for i in range (1,len(userResults)):
                    if i ==len(userResults):
                        self.lastCreated = driver.find_element_by_xpath("//table[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(i)+"]/td[2]").text
            else:
                settings.elementClick("ctl00_ContentZone_tablePager_BtnLast")
                time.sleep(1.5)
                tableResult = driver.find_element_by_id("ctl00_ContentZone_TblResults")
                userResults = tableResult.find_elements_by_tag_name("tr")
                self.lastCreated = driver.find_element_by_xpath("//table[@id='ctl00_ContentZone_TblResults']/tbody/tr[" + str(len(userResults)) + "]/td[2]").text
        
            settings.elementClick("ctl00_ButtonsZone_BtnDownload_IB_Label")
            if self.isAlertPresent()==True:
                driver.switch_to_alert().accept()     
            time.sleep(5)
            enviarViaLbl = driver.find_element_by_id("ctl00_LblError").text        
            if "OK" in enviarViaLbl:
                self.enviarViaVer = enviarViaLbl[41:].replace("'", "")
                print("La telecarga de Operadores se ha enviado a Vía con la versión "+self.enviarViaVer)
            else:
                self.fail("Hay un error en enviar telecargas a vía")
                
            settings.elementClick("ctl00_BtnLogOut")
            time.sleep(1)
            if self.isAlertPresent()==True:
                driver.switch_to_alert().accept()
            time.sleep(1)
            settings.loginPage(self.lastCreated, "00001")
            print("Se ha Creado el operador "+self.lastCreated+" con la contraseaña: 00001"+ " en el grupo de "+self.operatorG[4:])
            print("Se ha probado en la versión del BO Host: " + self.BOVersion[1:7]+" y Host Manager: "+self.BOVersion[8:])
            driver.get_screenshot_as_file("E:\\Selenium\\userCreatedscreenHome"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_crearOperadores\\attachments\\userCreatedscreenHome.jpeg")
            time.sleep(6)            
            self.cnn = pypyodbc.connect("DRIVER={SQL Server};"
                                        "SERVER=172.18.130.188;"
                                        "DATABASE=COVIHONDURAS_QA_TOLLPLAZA;"
                                        "UID=sa;"
                                        "PWD=lediscet")
            cursor = self.cnn.cursor()
            time.sleep(20)
            cursor.execute("select version, filename from dbo.atable where tabletype='operators' and version='"+self.enviarViaVer+"'")
            rows = cursor.fetchall()  
            if rows == []:
                self.fail("la telecarga de operadores versión "+self.enviarViaVer+" no ha bajado a plaza todavía")
            else:  
                for row in rows:
                    print("La telecarga de operadores con la version: "+row[0]+" ha bajado a la plaza con el nombre de archivo: "+row[1])
        
            self.cnn.commit()
            self.cnn.close()
       
        except:        
            unittest.TestCase.fail(self)
    
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
