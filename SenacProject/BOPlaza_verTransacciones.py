import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , PlazabaseUrl


class senacBackOffice(unittest.TestCase):
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver        
        driver.get(PlazabaseUrl)        
        settings.loginPage("00001", "00001")
        time.sleep(2)   
        linkSel = driver.find_element_by_id("ctl00_LblUser").text
        if linkSel == "Util.:":
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestion des transactions")).perform()
            driver.find_element_by_link_text("Voir transactions").click()
        else:   
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
        print("Hay "+ elementsFound[-4:]+ " transacciones desde la fecha 15/05/2017 hasta la fecha "+endDate)
        time.sleep(1);
        
if __name__== "__main__":
    unittest.main()