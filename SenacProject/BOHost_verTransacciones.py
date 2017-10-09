import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl


class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver        
        driver.get(HostbaseUrl)        
        settings.loginPage("00001", "00001")
        time.sleep(2)                    
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Transacciones")).perform()        
        driver.find_element_by_link_text("Ver transaciones").click()                                
        time.sleep(1)        
        driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").clear()
        driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_from_box_date").send_keys("15/05/2017")
        time.sleep(1);
        settings.selectDropDown("ctl00_ContentZone_cmb_vehicle_class_cmb_dropdown")
        time.sleep(0.5)
        driver.find_element_by_id("ctl00_ButtonsZone_BtnSearch").click()
        time.sleep(2)        
        elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text    
        endDate = driver.find_element_by_id("ctl00_ContentZone_dateSelector_dt_to_box_date").get_attribute("value")            
        time.sleep(1.5);        
        print("Hay "+ elementsFound[-5:]+ " transacciones desde la fecha 15/05/2017 hasta la fecha "+endDate)
        time.sleep(1);
        
if __name__== "__main__":
    unittest.main()