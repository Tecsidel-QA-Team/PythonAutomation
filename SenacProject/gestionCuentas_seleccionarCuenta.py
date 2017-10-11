import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl
from test.test_deque import fail

class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver        
        try:  
            driver.get(HostbaseUrl)
            time.sleep(1)            
            settings.loginPage("00001", "00001")
            time.sleep(2)            
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gesti\xf3n de cuentas")).perform()
            time.sleep(1)
            ActionChains(driver).click(driver.find_element_by_link_text("Seleccionar cuenta")).perform()
            time.sleep(1)
            tagNumbr = "68989"
            driver.find_element_by_id("ctl00_ContentZone_Textbox_byTag").send_keys(tagNumbr)
            time.sleep(0.5)
            driver.find_element_by_id("ctl00_ButtonsZone_BtnSearch").click()
            time.sleep(3)
            nextPageS = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text            
            time.sleep(0.20);
            if nextPageS =="Selecci\xf3n de cuenta":
                errorSearch = driver.find_element_by_id("ctl00_LblError").text 
                if errorSearch.equal("Luhn incorrecto"):
                    time.sleep(0.50);
                    print("ERROR AL TRATAR DE BUSCAR TAG, debido a: " + errorSearch)
                    fail("ERROR BUSQUEDA TAG: "+errorSearch)
            else:
                time.sleep(3)
                driver.find_element_by_id("ctl00_ContentZone_BtnVehicles").click()
                time.sleep(1)                
                print("La cuenta se ha visualizado correctamente");
                time.sleep(1);                                    
            
        except:           
            unittest.TestCase.fail(self, Exception)
            

if __name__== "__main__":
    unittest.main()        
