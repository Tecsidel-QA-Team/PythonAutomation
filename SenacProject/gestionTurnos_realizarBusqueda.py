import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl, timet
from test.test_deque import fail


class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = self.settings.driver
        settings.borrarArchivos("E:\\workspace\\Mavi_Repository\\gestionTurnos_realizarBusqueda\\attachments\\")
        try:
            driver.get(HostbaseUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginpageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionTurnos_realizarBusqueda\\attachments\\loginpageSenac.jpeg")
            settings.loginPage("00001", "00001")
            driver.get_screenshot_as_file("E:\\Selenium\\homepageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionTurnos_realizarBusqueda\\attachments\\homepageSenac.jpeg")
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gesti\xf3n de turno")).perform()
            time.sleep(1)
            driver.find_element_by_xpath("(//a[contains(text(),'Gesti\xf3n de turno')])[2]").click()                                
            time.sleep(1);
            driver.find_element_by_id("ctl00_ContentZone_dt_from_box_date").clear()
            driver.find_element_by_id("ctl00_ContentZone_dt_from_box_date").send_keys("01/01/2017")
            time.sleep(0.50)
            driver.find_element_by_id("ctl00_ButtonsZone_BtnSearch").click()
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\searchResults_"+timet+".jpeg");
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\gestionTurnos_realizarBusqueda\\attachments\\searchResults.jpeg");
            time.sleep(1);
            elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text;                
            time.sleep(1.5)
            print(elementsFound)
            time.sleep(1)
            
        except:                    
            unittest.TestCase.fail(self, Exception)
                    
if __name__== "__main__":
    unittest.main() 