# -*- coding: utf-8 -*-

import unittest
import time

from Settingsfields_File import  Settingsfields_File , CaCUrl, timet
from selenium.webdriver.common.action_chains import ActionChains
    
        
class CAC_accountReload(unittest.TestCase):
    accountClosed = False
    optionclick1 = 0    
    Saldo = ""
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        time.sleep(1)
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\")
        CAC_accountReload.accountReload(self)
        time.sleep(1)
        if self.accountClosed == True:
            print("No se puede hacer Recarga a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            self.fail("No se puede hacer Recarga a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            return
       
        time.sleep(1)
        print("Se Recargado la cuenta "+self.accountNumbr[7:16]+" correctamente y posee un saldo de: "+self.Saldo)
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])
    
    def accountReload(self):
        settings = self.settings
        driver = settings.driver
        driver.get(CaCUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\loginCACCVHPage.jpeg")
        settings.loginPage("00001", "00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\homeCACCVHPage.jpeg")
        self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
        time.sleep(2)                    
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")
        table = tableres.find_elements_by_tag_name("tr")
        self.selectAccount = settings.ranNumbr(2,len(table))
        driver.get_screenshot_as_file("E:\\Selenium\\accountSearchPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\accountSearchPage.jpeg")
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(self.selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\accountPage.jpeg")
        time.sleep(1)
        if "CUENTA CERRADA" in "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        settings.elementClick("ctl00_ContentZone_BtnLoads")
        time.sleep(1)    
        self.optionclick = settings.ranNumbr(0,3)
        settings.elementClick("ctl00_ContentZone_CtType_radioButtonList_payBy_"+str(self.optionclick))
        optionclick1 = settings.ranNumbr(0,1)
        if optionclick1==1:
            settings.elementClick("ctl00_ContentZone_CtType_chk_present")
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_CtType_text_total_txt_formated")
        ActionChains(driver).send_keys(str(settings.ranNumbr(100000,900000))).perform()
        ##driver.find_element_by_id("ctl00_ContentZone_CtType_text_total_txt_formated").send_keys(str(settings.ranNumbr(100000,900000)))
        time.sleep(.50)
        driver.get_screenshot_as_file("E:\\Selenium\\accountReloadPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\accountReloadPage.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        time.sleep(3)
        driver.get_screenshot_as_file("E:\\Selenium\\accountReloadConfirmationPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\accountReloadConfirmationPage.jpeg")
        if self.optionclick == 0:
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==1:  
            driver.find_element_by_id("ctl00_ContentZone_CtbyCard_BoxAuthCode_box_data").send_keys(str(settings.ranNumbr(100000,999999)))
            time.sleep(2)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==2:
            driver.find_element_by_id("ctl00_ContentZone_CtbyCheque_txt_number_box_data").send_keys(str(settings.ranNumbr(100000,9999999)))
            time.sleep(2)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==3:  
            driver.find_element_by_id("ctl00_ContentZone_CtbyDepoBancario_BoxReference_box_data").send_keys("REF. "+str(settings.ranNumbr(10000,99999)))
            time.sleep(2)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")       
        time.sleep(3)
        driver.get_screenshot_as_file("E:\\Selenium\\accountReloadInvoicePage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\accountReload\\attachments\\accountReloadInvoicePage.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnBack_IB_Label")
        time.sleep(2)
        self.Saldo = driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_label_balance_pounds").text              

if __name__== "__main__":
    unittest.main()