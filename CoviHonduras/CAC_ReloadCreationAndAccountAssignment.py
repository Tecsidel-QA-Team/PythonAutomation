# -*- coding: utf-8 -*-

import unittest
import time
from selenium.webdriver.support.ui import Select
from Settingsfields_File import  Settingsfields_File, CaCUrl, timet, infoCuenta0, RUCid, sexSelc,\
    titulofield,namef,lastNameOp, surnamef,nameOp, addressf,addressTec, cpf, cpAdress, \
    phoneCel, countryf, emailf,workPhone, workPhone1, perPhone, faxPhone, infoCuenta1, companyf,\
    contactf
from selenium.webdriver.common.action_chains import ActionChains
import CAC_accountCreationWithVehicle

          
class CAC_ReloadCreationAndAccountAssignment(unittest.TestCase):   
    accountClosed = False
    reloadCreated = False      
    applicationType=""
    applicationTypeText=""
    reloadDescription=""
    optionclickP=0
        
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):  
        settings = self.settings        
        settings.borrarArchivos("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\")
        CAC_ReloadCreationAndAccountAssignment.accountReload(self)
        time.sleep(1)
        if self.accountClosed==True:
            print("No se puede asignar un Recargo a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
            self.fail("No se puede asignar un Recargo a la cuenta "+self.accountNumbr[7:16]+" porque está cerrada")
        
        if self.reloadCreated==True:
            print("Se ha creado un Recargo para "+self.applicationType+" y se ha aplicado a la cuenta "+self.accountNumbr[7:16]+" correctamente")
            time.sleep(1)
            return
        else:
            self.fail("El recargo se ha creado pero no se ha podido aplicar a la cuenta "+self.accountNumbr[7:16]+" por un error")
            print("El recargo se ha creado pero no se ha podido aplicar a la cuenta "+self.accountNumbr[7:16]+" por un error, verificar pantallazo o log de error")
        
    def accountReload(self):
        settings = self.settings
        driver = settings.driver
        driver.get(CaCUrl)
        driver.get_screenshot_as_file("E:\\Selenium\\loginCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\loginCACCVHPage.jpeg")        
        settings.loginPage("00001","00001")
        driver.get_screenshot_as_file("E:\\Selenium\\homeCACCVHPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\homeCACCVHPage.jpeg");
        self.BOVersion = driver.find_element_by_id("ctl00_statusRight").text
        time.sleep(2)                    
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Configuración sistema")).perform()
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Parámetros de cuenta")).perform()
        time.sleep(1.5)
        driver.find_element_by_link_text("Recargos").click()
        time.sleep(2)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPage.jpeg")
        settings.elementClick("ctl00_ContentZone_BtnCreate")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadCreatioPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadCreatioPage.jpeg")
        time.sleep(.50)
        selopt = settings.ranNumbr(0,3)
        settings.selectDropDown("ctl00_ContentZone_cmb_type_cmb_dropdown")
        Select(driver.find_element_by_id("ctl00_ContentZone_cmb_type_cmb_dropdown")).select_by_index(selopt)
        time.sleep(.50)
        applicationT = Select(driver.find_element_by_id("ctl00_ContentZone_cmb_type_cmb_dropdown"))
        self.applicationType = applicationT.first_selected_option.text
        self.applicationTypeText = self.applicationType+"-"+timet[4:14]
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_txt_name_box_data").send_keys(self.applicationTypeText)
        time.sleep(2)
        self.reloadDescription = "Recargo para "+self.applicationTypeText            
        driver.find_element_by_id("ctl00_ContentZone_txt_description_box_data").send_keys(self.reloadDescription)
        if not self.applicationType=="Creación de cuenta":
            settings.selectDropDown("ctl00_ContentZone_cmb_applicationType_cmb_dropdown")
        ActionChains(driver).click(driver.find_element_by_id("ctl00_ContentZone_money_amount_txt_formated")).perform()
        ActionChains(driver).send_keys(str(settings.ranNumbr(10000,20000))).perform()
        time.sleep(3)
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(3)
        applicationTypeS = {
            "Creación de cuenta":       CAC_ReloadCreationAndAccountAssignment.accountCreation,                                                
            "Actualización de cuenta":  CAC_ReloadCreationAndAccountAssignment.accountUpdate,                                                
            "Creación de vehículo":     CAC_ReloadCreationAndAccountAssignment.vehicleCreation,                                                
            "Pérdida de Tag":           CAC_ReloadCreationAndAccountAssignment.tagMissed,                                                
        }
        applicationTypeS["Pérdida de Tag"](self)##self.applicationType
        
    def accountCreation(self):
        settings = self.settings
        driver = settings.driver
        time.sleep(2)                    
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Crear cuenta")).perform()
        time.sleep(.5)
        driver.find_element_by_link_text("Prepago").click()                                
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountCreationPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountCreation.jpeg")
        settings.elementClick("ctl00_ContentZone_BtnFees")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPage"+timet+".jpeg");
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPage.jpeg")
        time.sleep(1)
        Select(driver.find_element_by_id("ctl00_ContentZone_list_all_fees")).select_by_visible_text(self.applicationTypeText)
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_btn_add")
        time.sleep(.5)
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(.100)
        selOpt = settings.ranNumbr(0,1)
        selOp = settings.ranNumbr(0,8)
        selOp2 = settings.ranNumbr(0,8)
        if selOpt==0:
            settings.elementClick(infoCuenta0)            
            time.sleep(1)
            driver.find_element_by_id(RUCid).send_keys(str(settings.ranNumbr(10000000,90000000))+str(settings.ranNumbr(100000,9000000)))
            Select (driver.find_element_by_id(titulofield)).select_by_visible_text(sexSelc[selOp])
            driver.find_element_by_id(namef).send_keys(nameOp[selOp])
            driver.find_element_by_id(surnamef).send_keys(lastNameOp[selOp])
            driver.find_element_by_id(addressf).send_keys(addressTec[selOp])
            driver.find_element_by_id(cpf).send_keys(cpAdress[selOp]);            
            driver.find_element_by_id(countryf).send_keys("España");
            driver.find_element_by_id(emailf).send_keys(nameOp[selOp].lower()+"."+lastNameOp[selOp].lower()+"@tecsidel.es")
            driver.find_element_by_id(phoneCel).send_keys(str(settings.ranNumbr(600000000,699999999)))
            driver.find_element_by_id(workPhone).send_keys(workPhone1[selOp])
            driver.find_element_by_id(perPhone).send_keys(str(settings.ranNumbr(900000000,999999999)))
            driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOp])                
            time.sleep(4)
        else:
            driver.find_element_by_id(infoCuenta1).click()
            driver.find_element_by_id(RUCid).send_keys(str(settings.ranNumbr(10000000,90000000))+str(settings.ranNumbr(100000,9000000)))
            time.sleep(1)
            driver.find_element_by_id(companyf).send_keys("Tecsidel, S.A")
            driver.find_element_by_id(contactf).send_keys(nameOp[selOp]+" "+lastNameOp[selOp]+", "+nameOp[selOp2]+" "+lastNameOp[selOp2])
            driver.find_element_by_id(addressf).send_keys(addressTec[2])
            driver.find_element_by_id(cpf).send_keys(cpAdress[2])
            driver.find_element_by_id(countryf).send_keys("España")
            driver.find_element_by_id(emailf).send_keys("info@tecsidel.es")
            driver.find_element_by_id(phoneCel).send_keys(str(settings.ranNumbr(600000000,699999999)))
            driver.find_element_by_id(workPhone).send_keys(workPhone1[2])
            driver.find_element_by_id(perPhone).send_keys(str(settings.ranNumbr(900000000,999999999)))
            driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOp])
            time.sleep(1)        
        settings.selectDropDown("ctl00_ContentZone_ctrlAccountData_cmb_groupFare_cmb_dropdown")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\dataFilled"+timet+".jpeg");
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\dataFilled.jpeg");
        settings.elementClick("ctl00_ButtonsZone_BtnSave_IB_Label")
        CAC_ReloadCreationAndAccountAssignment.reloadConfirmation(self)

    def accountUpdate(self):    
        settings = self.settings
        driver = settings.driver    
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")
        table = tableres.find_elements_by_tag_name("tr")
        selectAccount = settings.ranNumbr(2,len(table))
        driver.get_screenshot_as_file("E:\\Selenium\\accountSearchPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountSearchPage.jpeg");
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountPage.jpeg")                
        time.sleep(1)
        if "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(.50)
        settings.elementClick("ctl00_ContentZone_BtnFees")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPage.jpeg")
        time.sleep(1)
        Select (driver.find_element_by_id("ctl00_ContentZone_list_all_fees")).select_by_visible_text(self.applicationTypeText)
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_btn_add")
        time.sleep(.50)
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(1)
        driver.find_element_by_id(RUCid).clear()
        driver.find_element_by_id(RUCid).send_keys(str(settings.ranNumbr(10000000,90000000))+str(settings.ranNumbr(100000,9000000)))
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\dataChangeded"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\dataChanged.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label");
        CAC_ReloadCreationAndAccountAssignment.reloadConfirmation(self)

    def vehicleCreation(self):
        settings = self.settings
        driver = settings.driver
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")
        table = tableres.find_elements_by_tag_name("tr")
        selectAccount = settings.ranNumbr(2,len(table))
        driver.get_screenshot_as_file("E:\\Selenium\\accountSearchPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountSearchPage.jpeg")
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountPage.jpeg")                
        time.sleep(1)
        if "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(.50)
        settings.elementClick("ctl00_ContentZone_BtnFees")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPage.jpeg")
        time.sleep(1)
        Select(driver.find_element_by_id("ctl00_ContentZone_list_all_fees")).select_by_visible_text(self.applicationTypeText)
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_btn_add")
        time.sleep(.50)
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(2)
        CAC_accountCreationWithVehicle.CAC_accountCreationWithVehicle.accountCreationWithVehicle(self)
        CAC_ReloadCreationAndAccountAssignment.reloadConfirmation(self)
    
    def tagMissed(self):
        settings = self.settings
        driver = settings.driver
        time.sleep(1)
        ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Gestión de cuentas")).perform()
        time.sleep(1)
        driver.find_element_by_link_text("Seleccionar cuenta").click()
        time.sleep(2)
        settings.elementClick("ctl00_ButtonsZone_BtnSearch_IB_Label")
        tableres = driver.find_element_by_id("ctl00_ContentZone_TblResults")
        table = tableres.find_elements_by_tag_name("tr")
        selectAccount = settings.ranNumbr(2,len(table))
        driver.get_screenshot_as_file("E:\\Selenium\\accountSearchPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountSearchPage.jpeg")
        driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_TblResults']/tbody/tr["+str(selectAccount)+"]/td[1]/a").click()
        time.sleep(1)
        self.accountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        driver.get_screenshot_as_file("E:\\Selenium\\accountPage"+timet+".jpg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountPage.jpeg")                
        time.sleep(1)
        if "CUENTA CERRADA" in driver.page_source:
            self.accountClosed = True
            return
        
        settings.elementClick("ctl00_ButtonsZone_BtnValidate_IB_Label")
        time.sleep(.50)
        settings.elementClick("ctl00_ContentZone_BtnFees")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPage.jpeg")
        time.sleep(1)
        Select(driver.find_element_by_id("ctl00_ContentZone_list_all_fees")).select_by_visible_text(self.applicationTypeText)
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_btn_add")
        time.sleep(.50)
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit_IB_Label")
        time.sleep(2)
        numberVehicles = driver.find_element_by_id("ctl00_ContentZone_lbl_vehicles").text
        NumbVeh = int(numberVehicles)
        if NumbVeh==0:
            CAC_accountCreationWithVehicle.CAC_accountCreationWithVehicle.accountCreationWithVehicle(self)
        else:
            driver.find_element_by_id("ctl00_ButtonsZone_BtnValidate_IB_Label").click()
            time.sleep(1.5)
        
        nextPage = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        time.sleep(1)
        if nextPage=="Detalles del pago":
            CAC_ReloadCreationAndAccountAssignment.reloadConfirmation(self)
        
        settings.elementClick("ctl00_ContentZone_BtnTags")
        driver.get_screenshot_as_file("E:\\Selenium\\tagAssignmentMainPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\tagAssignmentMainPage.jpeg")
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_chk_0")
        tagid = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_m_table_members']/tbody/tr[2]/td[6]").text
        if tagid=="":
            settings.elementClick("ctl00_ContentZone_btn_token_assignment")
            time.sleep(.50)
            driver.find_element_by_id("ctl00_ContentZone_txt_pan_token_txt_token_box_data").send_keys(str(settings.ranNumbr(1,99999)))
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_btn_init_tag")
            time.sleep(.50)
            settings.elementClick("ctl00_ContentZone_chk_0")       
        settings.elementClick("ctl00_ContentZone_btn_token_stolen")
        time.sleep(1)
        settings.elementClick("ctl00_ContentZone_btn_stolen")
        time.sleep(1.5)
        CAC_ReloadCreationAndAccountAssignment.reloadConfirmation(self)        
        
    def reloadConfirmation(self):
        settings = self.settings
        driver = settings.driver
        time.sleep(3)
        tablereload = driver.find_element_by_id("ctl00_ContentZone_CtNumbers_m_table_fees")
        tablere = tablereload.find_elements_by_tag_name("tr")              
        driver.get_screenshot_as_file("E:\\Selenium\\PayDetailPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\PayDetailPage.jpeg")
        if len(tablere)>1:
            i = 2
            while i <= len(tablere):              
                self.reload = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_CtNumbers_m_table_fees']/tbody/tr["+str(i)+"]/td[1]").text
                if self.reloadDescription in self.reload:
                    self.reloadCreated = True
                    break                                
                if i == len(tablere) and not self.reloadDescription in self.reload:
                        self.reloadCreated = False
                        return
                i+=1                                
        if len(tablere)<2:
            self.reloadCreated = False
            return
        
        settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        time.sleep(1)
        if not self.applicationTypeText=="Pérdida de Tag":
            self.optionclick = settings.ranNumbr(0,3)
        else:
            self.optionclick = settings.ranNumbr(0,2)
                
        settings.elementClick("ctl00_ContentZone_CtType_radioButtonList_payBy_"+str(self.optionclick))
        optionclick1 = settings.ranNumbr(0,1)
        if optionclick1==1:
            settings.elementClick("ctl00_ContentZone_CtType_chk_present")
        
        time.sleep(1)        
        driver.get_screenshot_as_file("E:\\Selenium\\ReloadPageDetail"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\ReloadPageDetail.jpg")
        settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        time.sleep(3)
        driver.get_screenshot_as_file("E:\\Selenium\\accountReloadConfirmationPage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadCreation\\attachments\\accountReloadConfirmationPage.jpeg")
        if self.optionclick==0:
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==1:
            driver.find_element_by_id("ctl00_ContentZone_CtbyCard_BoxAuthCode_box_data").send_keys(str(settings.ranNumbr(100000,999999)))
            time.sleep(.50)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==2:
            driver.find_element_by_id("ctl00_ContentZone_CtbyCheque_txt_number_box_data").send_keys(str(settings.ranNumbr(1000000,9999999)))
            time.sleep(.50)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        if self.optionclick==3:
            driver.find_element_by_id("ctl00_ContentZone_CtbyDepoBancario_BoxReference_box_data").send_keys("REF. "+str(settings.ranNumbr(1000000,9999999)))
            time.sleep(.50)
            settings.elementClick("ctl00_ButtonsZone_BtnExecute_IB_Label")
        
        time.sleep(4)
        driver.get_screenshot_as_file("E:\\Selenium\\accountReloadInvoicePage"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Maria_Repository\\ReloadPage\\attachments\\accountReloadInvoicePage.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnBack_IB_Label")
        time.sleep(2)
        
if __name__== "__main__":
    unittest.main()    