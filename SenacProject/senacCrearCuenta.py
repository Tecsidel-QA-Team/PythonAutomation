import unittest
import time
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import nameOp, baseUrl, infoCuenta0, sexSelcSpan, titulofield,\
    namef, surnamef, lastNameOp, loginField, passField, loginButton, infoCuenta1,\
    companyf, contactf, addressf, addressTec, cpf, cpAdress, townf, emailf,\
    phoneCel, townC, workPhone, workPhone1, perPhone, faxPhone, countryf,\
    senacSettingsMethod, matletT, camionModels, cocheModels, cicloModels,\
    autoBusModels, furgonetaModels, colorS, matriNu, vehtypeModel, vehtypeKind,\
    confirmationMessage, tagIdNmbr, errorTagAssignment
from selenium.webdriver.support.ui import Select
import senacSettings
from _operator import or_

class senacBackOffice(unittest.TestCase):
    
    
        
    def setUp(self):
        self.settings = senacSettingsMethod()
        self.settings.setUp()

    def test(self):   
        
        settings = self.settings
        driver = settings.driver
        driver.get(baseUrl)
        time.sleep(5)
        self.settings.loginPage("00001", "00001")
        linkSel = driver.find_element_by_id("ctl00_LblUser").text
        if linkSel == "Util.:":
            self.selLink = senacSettings.frenlink
            self.sexSelc = senacSettings.sexSelcFre
        else:
            self.selLink = senacSettings.spanlink
            self.sexSelc = senacSettings.sexSelcSpan    
            
        gestionCuenta = driver.find_element_by_link_text(self.selLink[0])
        ActionChains(driver).click_and_hold(gestionCuenta).perform()
        time.sleep(5)
        crearCuenta = driver.find_element_by_link_text(self.selLink[1])
        ActionChains(driver).click_and_hold(crearCuenta).perform()
        driver.find_element_by_link_text(self.selLink[2]).click()
        time.sleep(2)
        self.accoountNumbr = driver.find_element_by_id("ctl00_SectionZone_LblTitle").text
        time.sleep(2)
        senacBackOffice.crearcuentaSub(self)
        time.sleep(2)
        self.settings.elementClick("ctl00_ButtonsZone_BtnSave")
        time.sleep(3)
        self.settings.elementClick("ctl00_ButtonsZone_BtnExecute")
        time.sleep(1)
        self.settings.elementClick("ctl00_ButtonsZone_BtnValidate")
        time.sleep(1)
        self.settings.elementClick("ctl00_ContentZone_BtnVehicles")
        time.sleep(1)
        self.settings.elementClick("ctl00_ContentZone_BtnCreate")
        time.sleep(1)
        senacBackOffice.crearVechiulo(self)
        time.sleep(1)
        senacBackOffice.vehicleFieldsfill(self, self.matriNu,self.vehtypeModel,self.vehtypeKind,colorS[self.settings.ranNumbr(0,len(colorS)-1)])
        time.sleep(3);
        driver.find_element_by_id("ctl00_ButtonsZone_BtnSubmit").click()
        time.sleep(1.5)
        driver.find_element_by_id("ctl00_ButtonsZone_BtnBack").click()
        time.sleep(1.5)
        driver.find_element_by_id("ctl00_ButtonsZone_BtnValidate").click()
        time.sleep(2.5)
        senacBackOffice.tagAssignment(self)
        if errorTagAssignment==True:
            print("ERROR AL ASIGNAR TAG a la cuenta: "+self.accoountNumbr[7:15]+", "+self.confirMsg)
            self.fail("Tag Invalido: No se puede asignar un Tag al Vehiculo "+self.matriNu+" de la cuenta "+self.accoountNumbr[7:-15])
            return
        else: 
            print("Se ha creado la cuenta: "+self.accoountNumbr[7:15]+" con un Vehiculo con la matricula "+self.matriNu+" y el tag asignado No.: "+ self.tagIdNumbrT);
            time.sleep(3)
        
    def tearDown(self):
        driver = self.settings.driver
        driver.close()
        
    def crearcuentaSub(self):
        driver = self.settings.driver
        selOpt1 = self.settings.ranNumbr(0,1)      
        selOpt = self.settings.ranNumbr(0,8)
        selOpt2 = self.settings.ranNumbr(0,8)
        if (selOpt1 == 0):            
            driver.find_element_by_id(infoCuenta0).click()
            time.sleep(1)
            Select (driver.find_element_by_id(titulofield)).select_by_visible_text(self.sexSelc[selOpt])
            driver.find_element_by_id(namef).send_keys(nameOp[selOpt])
            driver.find_element_by_id(surnamef).send_keys(lastNameOp[selOpt])
            driver.find_element_by_id(addressf).send_keys(addressTec[selOpt]);
            driver.find_element_by_id(cpf).send_keys(cpAdress[selOpt]);
            driver.find_element_by_id(townf).send_keys(townC[selOpt]);
            driver.find_element_by_id(countryf).send_keys("Espa\xf1a");
            driver.find_element_by_id(emailf).send_keys(nameOp[selOpt].lower()+"."+lastNameOp[selOpt].lower()+"@tecsidel.es");
            driver.find_element_by_id(phoneCel).send_keys(self.settings.ranNumbr(600000000,699999999));
            driver.find_element_by_id(workPhone).send_keys(workPhone1[selOpt])
            driver.find_element_by_id(perPhone).send_keys(self.settings.ranNumbr(900000000,999999999));
            driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOpt]);                
            time.sleep(1);
        else:
            driver.find_element_by_id(infoCuenta1).click()                
            time.sleep(1)
            driver.find_element_by_id(companyf).send_keys("Tecsidel, S.A")
            driver.find_element_by_id(contactf).send_keys(nameOp[selOpt]+" "+lastNameOp[selOpt]+", "+nameOp[selOpt2]+" "+lastNameOp[selOpt2])
            driver.find_element_by_id(addressf).send_keys(addressTec[2])
            driver.find_element_by_id(cpf).send_keys(cpAdress[2])
            driver.find_element_by_id(townf).send_keys(townC[2])                
            driver.find_element_by_id(emailf).send_keys("info@tecsidel.es")
            driver.find_element_by_id(phoneCel).send_keys(self.settings.ranNumbr(600000000,699999999))
            driver.find_element_by_id(workPhone).send_keys(workPhone1[2])
            driver.find_element_by_id(perPhone).send_keys(self.settings.ranNumbr(900000000,999999999))
            driver.find_element_by_id(faxPhone).send_keys(workPhone1[selOpt])
            time.sleep(1)
            
        selOpt1 = self.settings.ranNumbr(0,1)
        if (selOpt1==1):
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_discount_0").click()
        else:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_discount_1").click()
            selOpt1 = self.settings.ranNumbr(0,1)
            if (selOpt1==0):
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_typeOfDiscount_0").click()
                selOpt1 = self.settings.ranNumbr(0,1)
                if (selOpt1==0):
                    driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_for_0").click()                    
                else:
                    driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_for_1").click()   
            else:
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_rd_typeOfDiscount_1").click()
        time.sleep(2)
        self.settings.selectDropDown("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMode_cmb_dropdown");
        time.sleep(2)
        PayMode = Select(driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMode_cmb_dropdown"))
        self.PayModeT = PayMode.first_selected_option   
        if self.PayModeT.text == "Prepago" or self.PayModeT.text == "Pr\xe9-paiement":
            selOpt1 = self.settings.ranNumbr(0,1);            
            if selOpt1 > 0:
                time.sleep(1)
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_chk_show_low_in_lane").click()
                time.sleep(1)
            self.settings.selectDropDown("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMethod_cmb_dropdown")
            time.sleep(1)
            PayMethod = Select (driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMethod_cmb_dropdown"))
            PayMetthodT = PayMethod.first_selected_option            
            if PayMetthodT.text == "preautorizado" or PayMetthodT.text == "Pre-autoris\xe9":
                time.sleep(1)                                
                ##driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_topup_txt_formated").clear()
                ##driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_topup_txt_formated").send_keys (self.settings.ranNumbr(1000,200000))
                time.sleep(1)
                selOpt1 = self.settings.ranNumbr(0,1)
                if selOpt1 > 0:
                    driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_chk_fixed").click()
                else:
                    self.settings.selectDropDown("ctl00_ContentZone_ctrlAccountStandard_cmb_topupDay_cmb_dropdown")   
                time.sleep(1)                
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_bankAccount_box_data").send_keys("ES0"+str(self.settings.ranNumbr(10,200))+"-"+str(self.settings.ranNumbr(1000,3000))+"-"+str(self.settings.ranNumbr(100,200))+"-"+str(self.settings.ranNumbr(1000,5000))+"-"+str(self.settings.ranNumbr(50000,90000)))
                time.sleep(1)
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_holderName_box_data").send_keys(nameOp[selOpt]+" "+lastNameOp[selOpt])                
            time.sleep(5)
        else:
            self.settings.selectDropDown("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMethod_cmb_dropdown")
            time.sleep(1);                        
            PayMethod = Select(driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_cmb_paymentMethod_cmb_dropdown"))
            PayMetthodT = PayMethod.first_selected_option                        
            if PayMetthodT.text== "preautorizado" or PayMetthodT.text == "Pre-autoris\xe9":
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_bankAccount_box_data").send_keys("ES0"+str(self.settings.ranNumbr(10,200))+"-"+str(self.settings.ranNumbr(1000,3000))+"-"+str(self.settings.ranNumbr(100,200))+"-"+str(self.settings.ranNumbr(1000,5000))+"-"+str(self.settings.ranNumbr(50000,90000)))
                time.sleep(1)
                driver.find_element_by_id("ctl00_ContentZone_ctrlAccountStandard_txt_holderName_box_data").send_keys(nameOp[selOpt]+" "+lastNameOp[selOpt])
                time.sleep(5)
        if self.settings.ranNumbr(0,1) >0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_check_itemised_billing").click() ##factura detallada click
        time.sleep(1)
        self.settings.selectDropDown("ctl00_ContentZone_ctrlAccountNotes_combo_statement_date")
        time.sleep(1)
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_check_statement_email_notice").click()
        time.sleep(1)
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_check_statement_post_notice").click()
        time.sleep(1);
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_radio_notification_1").click()
        time.sleep(1);
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_chk_receive_info").click()
        time.sleep(1);
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_chk_receive_ads").click()
        time.sleep(1);
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_check_suspension_state").click()
        time.sleep(1);
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_ctrlAccountNotes_chk_internet_access").click()
        time.sleep(3);
    
    def crearVechiulo (self):
        driver = self.settings.driver
        time.sleep(2)
        matNum = self.settings.ranNumbr(5000,9999);
        matlet = self.settings.ranNumbr(1,len(matletT))
        matlet1 = self.settings.ranNumbr(1,len(matletT))
        matlet2 = self.settings.ranNumbr(1,len(matletT))
        self.settings.selectDropDown("ctl00_ContentZone_cmb_vehicle_type")
        self.matriNu = str(matNum)+matletT[matlet:matlet+1]+matletT[matlet1:matlet1+1]+matletT[matlet2:matlet2+1]
        vehtype = Select(driver.find_element_by_id("ctl00_ContentZone_cmb_vehicle_type"))
        self.vehTypeS = vehtype.first_selected_option
        if self.vehTypeS.text =="Coche" or self.vehTypeS.text == "Voiture":
            carSel = self.settings.ranNumbr(0,3)
            carModel = self.settings.ranNumbr(1,2)
            if cocheModels[0][carSel]=="Seat":
                carModelSel = 0
            if cocheModels[0][carSel]=="Volkswagen":
                carModelSel = 1
            if cocheModels[0][carSel]=="Ford":
                carModelSel = 2
            if cocheModels[0][carSel]=="Fiat":
                carModelSel = 3
            self.vehtypeModel = cocheModels[0][carSel]
            self.vehtypeKind = cocheModels[carModel][carModelSel]    
            
        if self.vehTypeS.text =="Ciclomotor" or self.vehTypeS.text =="Cyclomoteur":
            carSel = self.settings.ranNumbr(0,1)
            carModel = self.settings.ranNumbr(1,2)
            if cicloModels[0][carSel]=="Yamaha":
                carModelSel = 0
            if cicloModels[0][carSel]=="Honda":
                carModelSel = 1
            self.vehtypeModel = cicloModels[0][carSel]
            self.vehtypeKind = cicloModels[carModel][carModelSel]
            
        if  self.vehTypeS.text =="Autob\xfas" or self.vehTypeS.text =="Bus":
            carSel = self.settings.ranNumbr(0,1)
            carModel = self.settings.ranNumbr(1,2)
            if autoBusModels[0][carSel]=="DAIMLER-BENZ":
                carModelSel = 0
            if autoBusModels[0][carSel]=="VOLVO":
                carModelSel = 1
            self.vehtypeModel = autoBusModels[0][carSel]
            self.vehtypeKind = autoBusModels[carModel][carModelSel]
            
        if self.vehTypeS.text == "Cami\xf3n" or self.vehTypeS.text == "Camion":
            carSel = self.settings.ranNumbr(0,1)
            carModel = self.settings.ranNumbr(1,2)
            if camionModels[0][carSel]=="Mercedes-Benz":
                carModelSel = 0
            if camionModels[0][carSel]=="Scania":
                carModelSel = 1
            self.vehtypeModel = camionModels[0][carSel]
            self.vehtypeKind = camionModels[carModel][carModelSel]
            
        if self.vehTypeS.text =="Furgoneta" or self.vehTypeS.text =="Van":
            carSel = self.settings.ranNumbr(0,1)
            carModel = self.settings.ranNumbr(1,2)
            if furgonetaModels[0][carSel]=="Mercedes-Benz":
                carModelSel = 0;
            if furgonetaModels[0][carSel]=="Fiat":
                carModelSel = 1
            self.vehtypeModel = furgonetaModels[0][carSel]
            self.vehtypeKind = furgonetaModels[carModel][carModelSel]
    
    def vehicleFieldsfill(self, Matricul, vehtypeM, vehtypeK, ColorT):
        driver = self.settings.driver
        time.sleep(1);
        driver.find_element_by_id("ctl00_ContentZone_text_plate_number").send_keys(Matricul)
        driver.find_element_by_id("ctl00_ContentZone_text_make").send_keys(vehtypeM)
        driver.find_element_by_id("ctl00_ContentZone_text_model").send_keys(vehtypeK)
        driver.find_element_by_id("ctl00_ContentZone_text_colour").send_keys(ColorT)            
        
    def tagAssignment(self):
        driver = self.settings.driver
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_BtnTags").click()
        time.sleep(0.50)
        driver.find_element_by_id("ctl00_ContentZone_chk_0").click()
        time.sleep(0.50)
        driver.find_element_by_id("ctl00_ContentZone_btn_tag_assignment").click()
        time.sleep(0.50)
        driver.find_element_by_id("ctl00_ContentZone_btn_tag_assignment").click()
        if self.settings.ranNumbr(0,1)>0:
            driver.find_element_by_id("ctl00_ContentZone_radio_dist_how_0").click()                
        time.sleep(0.50)
        driver.find_element_by_id("ctl00_ContentZone_txt_pan_tag").send_keys(self.settings.ranNumbr(1,99999))
        time.sleep(0.50)
        driver.find_element_by_id("ctl00_ContentZone_btn_init_tag").click()
        time.sleep(2)
        confirmationMessage = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_lbl_operation']")        
        self.confirMsg = confirmationMessage.text        
        time.sleep(5)
        if "ya tiene un tag asignado" in str(self.confirMsg) or "Este tag no est\x0e1 operativo" in str(self.confirMsg) or "Este tag ya est\x0e1 asignado al veh\xedculo" in str(self.confirMsg) or "Luhn incorrecto" in str(self.confirMsg):
            errorTagAssignment = True
        else:           
            tagIdNmbr = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_m_table_vehicles']/tbody/tr[2]/td[6]")
            self.tagIdNumbrT = tagIdNmbr.text            
        time.sleep(1)
    
if __name__== "__main__":
    unittest.main()

    
