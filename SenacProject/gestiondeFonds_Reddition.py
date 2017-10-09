import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod, PlazabaseUrl
from selenium.webdriver.support.ui import Select
from test.test_deque import fail



class senacBackOffice(unittest.TestCase):
    
    isAlertPresent = False
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver        
        try:
            driver.get(PlazabaseUrl)
            time.sleep(1)
            settings.loginPage("00001","00001")
            time.sleep(2)                    
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestion des fonds")).perform()
            time.sleep(1)
            driver.find_element_by_link_text("Reddition").click()
            time.sleep(1)            
            settings.selectDropDown("ctl00_ContentZone_cmb_numBags_cmb_dropdown")
            time.sleep(1)
            bagsnumbr = Select(driver.find_element_by_id("ctl00_ContentZone_cmb_numBags_cmb_dropdown"))
            bagNum = bagsnumbr.first_selected_option.text
            
            time.sleep(1)  
            i = 1;          
            for i in range (1,int(bagNum)+1):
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C5_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C10_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C25_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C50_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C100_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C200_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)                        
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C250_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01C500_"+str(i)).send_keys(str(settings.ranNumbr(1,4)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N500_"+str(i)).send_keys(str(settings.ranNumbr(1,5)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N1000_"+str(i)).send_keys(str(settings.ranNumbr(1,5)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N2000_"+str(i)).send_keys(str(settings.ranNumbr(1,5)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N5000_"+str(i)).send_keys(str(settings.ranNumbr(1,5)))
                time.sleep(.20)
                driver.find_element_by_id("ctl00_ContentZone_NumberCASH01N10000_"+str(i)).send_keys(str(settings.ranNumbr(1,5)))               
                time.sleep(.50)
            driver.find_element_by_id("ctl00_ContentZone_NumberCH201").send_keys(str(settings.ranNumbr(1,5)))
            time.sleep(.20)
            driver.find_element_by_id("ctl00_ContentZone_NumberCH202").send_keys(str(settings.ranNumbr(1000,10000)))
            time.sleep(.20)
            driver.find_element_by_id("ctl00_ContentZone_NumberVO01201").send_keys(str(settings.ranNumbr(1,5)))
            time.sleep(.20)
            driver.find_element_by_id("ctl00_ContentZone_NumberVO01202").send_keys(str(settings.ranNumbr(1000,10000)))
            time.sleep(.20)
            driver.find_element_by_id("ctl00_ContentZone_NumberOM201").send_keys(str(settings.ranNumbr(1,5)))
            time.sleep(.20)
            driver.find_element_by_id("ctl00_ContentZone_NumberOM202").send_keys(str(settings.ranNumbr(1000,10000)))
            time.sleep(1)
            driver.find_element_by_id("ctl00_ButtonsZone_BtnSubmit").click()
            time.sleep(2);                        
            if self.isAlertPresent(alert=True):
                driver.switch_to_alert().accept()           
                time.sleep(3);
                
            if self.isAlertPresent==False:
                time.sleep(3)
                nextPTitle = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
                if nextPTitle.contains("Reddition"):
                    errorLev = driver.find_element_by_id("ctl00_LblError").text
                    if (errorLev.contains("une erreur interne")):                        
                        print(errorLev)
                        time.sleep(1)
                        fail(errorLev)
                        return
            if self.isAlertPresent==True:
                driver.switch_to_alert().accept()        
                time.sleep(4)
                nextPTitle = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
                if nextPTitle.equals("Reddition"):
                    time.sleep(1)
                    print("Se ha creado correctamente Reddition")
                    return
                if (nextPTitle.contains("erreur interne")):
                    time.sleep(1.5)
                    errorLev = driver.find_element_by_id("ctl00_ContentZone_lblMsg").text
                    time.sleep(1)
                    print(errorLev)
                    time.sleep(1)
                    driver.quit()
                    fail(errorLev)
                    return                 
            else:
                time.sleep(.50)
                nextPTitle = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text                                            
                if "Reddition"== nextPTitle:
                    errorLev = driver.find_element_by_id("ctl00_LblError").text 
                    time.sleep(1.5)                    
                    print(errorLev)
                    time.sleep(1)
                    fail(errorLev)
                    return
            time.sleep(5);
            
        except:            
            fail(unittest)
    
    def isAlertPresent (self, alert):        
        driver = self.settings.driver
        try:
            driver.switch_to_alert()
            return alert == True
        except:
            return alert == False
            
if __name__== "__main__":
    unittest.main()      
