# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from Settingsfields_File import  Settingsfields_File , timet, nameOp,lastNameOp,addressTec,\
    cpAdress, townC,workPhone1,sexSelc, genderS, CaCUrl
from selenium.webdriver.common.action_chains import ActionChains


          
class CAC_operatorCreation(unittest.TestCase):   
    lastCreated = ""
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\")
        try:
            driver.get(CaCUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\loginCACCVHPage.jpeg")
            settings.loginPage("00001", "00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\homeCACCVHPage.jpeg")
            BOVersion = driver.find_element_by_id("ctl00_statusRight").text
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Configuración sistema")).perform()
            time.sleep(1)            
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Operadores")).perform()
            time.sleep(.50)
            driver.find_element_by_link_text("Gestión de operadores").click()                                
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\gestionOperadoresPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\gestionOperadoresPage.jpeg")
            time.sleep(.50)        
            settings.elementClick("ctl00_ContentZone_BtnCreate")
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\crearOperadoresPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\crearOperadoresPage.jpeg")
            userSel = settings.ranNumbr(0,len(nameOp)-1)
            Select(driver.find_element_by_id("ctl00_ContentZone_cmb_title_cmb_dropdown")).select_by_visible_text(sexSelc[userSel])
            time.sleep(.100)
            Select(driver.find_element_by_id("ctl00_ContentZone_cmb_gender_cmb_dropdown")).select_by_visible_text(genderS[userSel])
            driver.find_element_by_id("ctl00_ContentZone_forename_box_data").send_keys(nameOp[userSel])
            time.sleep(.100);
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
            time.sleep(.100)
            driver.find_element_by_id("ctl00_ContentZone_txt_phone_box_data").send_keys(workPhone1[userSel])
            settings.selectDropDown("ctl00_ContentZone_group_cmb_dropdown")
            time.sleep(1)
            operatorGroup = Select(driver.find_element_by_id("ctl00_ContentZone_group_cmb_dropdown"))
            operatorG1 = operatorGroup.first_selected_option
            operatorG = operatorG1.text
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
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\userCreated.jpeg")
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
            
            settings.elementClick("ctl00_BtnLogOut")
            time.sleep(.50)
            driver.switch_to_alert().accept()
            time.sleep(1)
            settings.loginPage(self.lastCreated, "00001")
            driver.get_screenshot_as_file("E:\\Selenium\\userCreatedscreenHome"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\CAC_crearOperadores\\attachments\\userCreatedscreenHome.jpeg")        
            print("Se ha Creado el "+self.lastCreated+" con la contraseaña: 00001"+ " en el grupo de "+operatorG[4:])
            print("Se ha probado en la versión del CAC BO: " + BOVersion[1:16]+" y CAC Manager: "+BOVersion[17:])
            driver.close()
        except:
            unittest.TestCase.fail(self)
        
if __name__== "__main__":
    unittest.main()    
