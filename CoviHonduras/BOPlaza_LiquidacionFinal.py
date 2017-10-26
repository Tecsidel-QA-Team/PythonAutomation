# -*- coding: utf-8 -*-

import unittest
import time
from Settingsfields_File import  Settingsfields_File , timet, BoPlazaUrl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException
  
        
class BOPlaza_LiquidacionFinal(unittest.TestCase):   
    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\LiquidacionFinal\\attachments\\")
        BOPlaza_LiquidacionFinal.accountLiquidacionFinal(self)
        time.sleep(1) 
        print("Se ha cerrado una Liquidación Final correctamente")
        print("Se ha probado en la versión del CAC BO: " + self.BOVersion[1:16]+" y CAC Manager: "+self.BOVersion[17:])        

    def accountLiquidacionFinal(self):
        settings = self.settings
        driver = settings.driver
        driver.get(BoPlazaUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\LiquidacionFinal\\attachments\\loginCACCVHPage.jpeg")
        settings.loginPage("00001", "00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\LiquidaciónFinal\\attachments\\homeCACCVHPage.jpeg")
        self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
        time.sleep(2)                 
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cobrador")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Liquidación final").click()
        time.sleep(2)
        if "La operación ha fallado por un error desconocido" in driver.page_source:
            self.fail("No se puede generar una liquidación final debido a un error desconocido")
        settings.selectDropDown("ctl00_ContentZone_cmb_shiftGroup_cmb_dropdown")
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N50000_1").send_keys(str(settings.ranNumbr(1,4)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N10000_1").send_keys(str(settings.ranNumbr(1,4)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N5000_1").send_keys(str(settings.ranNumbr(1,4)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N2000_1").send_keys(str(settings.ranNumbr(1,4)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N1000_1").send_keys(str(settings.ranNumbr(1,10)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N500_1").send_keys(str(settings.ranNumbr(1,20)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N200_1").send_keys(str(settings.ranNumbr(1,50)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N100_1").send_keys(str(settings.ranNumbr(1,100)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C50_1").send_keys(str(settings.ranNumbr(1,200)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C20_1").send_keys(str(settings.ranNumbr(1,500)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C10_1").send_keys(str(settings.ranNumbr(1,1000)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C5_1").send_keys(str(settings.ranNumbr(1,2000)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_NumberCD201").send_keys(str(settings.ranNumbr(1,5)))
        ActionChains(driver).click(driver.find_element_by_id("ctl00_ContentZone_NumberCD202_txt_formated")).perform()
        ActionChains(driver).send_keys(str(settings.ranNumbr(10000,99999))).perform()
        time.sleep(.50)
        driver.get_screenshot_as_file("E:\\Selenium\\LiquidacionParcialPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\LiquidaciónFinal\\attachments\\LiquidacionParcialPage.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(.50)
        if self.isAlertPresent()==True:
            driver.switch_to.alert.accept()
            time.sleep(2)
        if self.isAlertPresent()==True:
            driver.switch_to.alert.accept()
            time.sleep(12)
        driver.get_screenshot_as_file("E:\\Selenium\\LiquidacionInvoice"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\LiquidaciónFinal\\attachments\\LiquidacionInvoice.jpeg")
        time.sleep(1)
    

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