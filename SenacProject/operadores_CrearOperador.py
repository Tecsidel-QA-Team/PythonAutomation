import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  baseUrl, opIdField,emailField,hourNumber,\
    nameOp, lastNameOp,lastNameField, groupOperator, submitBtn, \
    senacSettingsMethod, repeatpwdField, pwdField, nameField


class senacBackOffice(unittest.TestCase):
    opezero = ""
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver
        driver.get(baseUrl)
        time.sleep(5)
        self.settings.loginPage("00001", "00001")           
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Configuraci\xf3n sistema")).perform()
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Operadores")).perform()
        time.sleep(1)
        ActionChains(driver).click(driver.find_element_by_link_text("Gesti\xf3n de operadores")).perform()
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_BtnCreate").click()
        time.sleep(1)
        opId = self.settings.ranNumbr(1,99999)    
        opIdnumbr = len(str(opId))    
        if (opIdnumbr < 5):
            opI = 5-len(str(opId))
            opc = chr(opI)
            for i in range(0,-opId):
                opc[i]="0"
                self.opezero = self.opezero+str(opc[i])
            self.opezero = self.opezero+str(opId)
        else:
            self.opezero = str(opId)
        time.sleep(2)
        senacBackOffice.operatorCreate(self)
        driver.find_element_by_id("ctl00_BtnLogOut").click()
        time.sleep(2)
        driver.switch_to_alert().accept()
        time.sleep(3)
        self.settings.loginPage(self.opezero,self.opezero)
        time.sleep(.50);
        print("El Operador "+self.opezero+" ha sido creado y entra correctamente a BackOffice")               
    
    def operatorCreate(self):
        driver = self.settings.driver    
        time.sleep(1);            
        driver.find_element_by_id(opIdField).send_keys(self.opezero)
        selOp = self.settings.ranNumbr(0,8)
        driver.find_element_by_id(nameField).send_keys(nameOp[selOp])
        driver.find_element_by_id(lastNameField).send_keys(lastNameOp[selOp])
        driver.find_element_by_id(emailField).send_keys(nameOp[selOp].lower()+"."+lastNameOp[selOp].lower()+"@tecsidel.es")
        self.settings.selectDropDown(groupOperator)
        driver.find_element_by_id(pwdField).send_keys(self.opezero)
        driver.find_element_by_id(repeatpwdField).send_keys(self.opezero)
        driver.find_element_by_id("ctl00_ContentZone_ChkSalde").click()
        driver.find_element_by_id("ctl00_ContentZone_ChkHistorique").click()
        driver.find_element_by_id(hourNumber).send_keys(self.settings.ranNumbr(1,999))    
        time.sleep(.50)            
        driver.find_element_by_id(submitBtn).click()
        time.sleep(3);
    
if __name__== "__main__":
    unittest.main()