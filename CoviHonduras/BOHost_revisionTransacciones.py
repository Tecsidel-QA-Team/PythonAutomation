import unittest
import time
from Settingsfields_File import  Settingsfields_File , timet, BoHostUrl
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoAlertPresentException

  
        
class BOHost_revisionTransacciones(unittest.TestCase):   
    
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver
        settings.borrarArchivos("E:\\workspace\\Mari_Repository\\BOHost_revisionTransacciones\\attachments\\")
        try:
            driver.get(BoHostUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginBOCVHPage"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mari_Repository\\BOHost_revisionTransacciones\\attachments\\loginBOCVHPage.jpeg")                    
            settings.loginPage("00001","00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homepageCVH_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mari_Repository\\BOHost_revisionTransacciones\\attachments\\homepageCVH.jpeg")
            time.sleep(2)
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Transacciones")).perform()
            time.sleep(1)
            driver.find_element_by_link_text("Revisión de Transacciones").click()                                
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\revisionTransicionesPage_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_revisionTransacciones\\attachments\\revisionTransicionesPage.jpeg")
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").clear()
            driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").send_keys("01/01/2017")
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_Button_transactions")
            time.sleep(3)
            driver.get_screenshot_as_file("E:\\Selenium\\revisionTransicionesResults_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\BOHost_revisionTransacciones\\attachments\\revisionTransicionesResults.jpeg")
            if "No hay transacciones para la selección actual" in driver.page_source:
                print ("No hay transacciones para la selección actual")
                self.fail("No hay transacciones para la selección actual")
                time.sleep(2000)
                return
            elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text                
            time.sleep(1.5)
            print("Busqueda Completa: "+ elementsFound)
            time.sleep(1)
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