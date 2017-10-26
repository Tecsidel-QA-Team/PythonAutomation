import unittest
import time
from Settingsfields_File import  Settingsfields_File , timet, BoHostUrl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

  
        
class BOHost_VerTransacciones(unittest.TestCase):   
    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()   
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
        self.dateverTransacciones = "01/09/2017"
        BOHost_VerTransacciones.verTransacciones(self)
        elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text                
        time.sleep(1.5)
        print("Busqueda Completa: "+ elementsFound)
        time.sleep(1)
            
    def verTransacciones(self):
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\BOHost_VerTranscciones\\attachments\\")
        try:
            driver.get(BoHostUrl)
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\loginBOCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_VerTranscciones\\attachments\\loginBOCVHPage.jpeg")
            settings.loginPage("00001","00001")    
            driver.get_screenshot_as_file("E:\\Selenium\\homeHostCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_VerTranscciones\\attachments\\homeHostCVHPage.jpeg")    
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Transacciones")).perform()                    
            time.sleep(1)
            driver.find_element_by_link_text("Ver transacciones").click()                                
            time.sleep(1)
            driver.get_screenshot_as_file("E:\\Selenium\\verTransaccionesPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_VerTranscciones\\attachments\\verTransaccionesPage.jpeg")
            time.sleep(.50)
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").clear()
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").send_keys(self.dateverTransacciones)
            time.sleep(1)        
            settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Button")
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\verTransaccionesResults"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_VerTranscciones\\attachments\\verTransaccionesRetults.jpeg")
            time.sleep(1)
        except:
            unittest.TestCase.fail(self)
                    
if __name__== "__main__":
    unittest.main()    