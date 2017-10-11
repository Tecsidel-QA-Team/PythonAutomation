import unittest
import time
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from senacSettings import  senacSettingsMethod , HostbaseUrl, timet
from test.test_deque import fail
from selenium.common.exceptions import NoAlertPresentException
from _overlapped import NULL



class senacBackOffice(unittest.TestCase):
    dateS = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    telP = ["ctl00_ContentZone_Prepay", "ctl00_ContentZone_Postpay"]
    promoSel = ["En funci\xf3n de recarga", "En funci\xf3n de tr\xe1nsitos", "En funci\xf3n del horario"]
    weekDay = ["ctl00_ContentZone_chk_lundi","ctl00_ContentZone_chk_mardi","ctl00_ContentZone_chk_mercredi","ctl00_ContentZone_chk_jeudi","ctl00_ContentZone_chk_vendredi","ctl00_ContentZone_chk_samedi","ctl00_ContentZone_chk_dimanche"]    
        
    def setUp(self):
        self.settings = senacSettingsMethod()        
        self.settings.setUp()

    def test(self):
        settings = self.settings
        driver = settings.driver      
        promoSel = self.promoSel                         
        try:
            driver.get(HostbaseUrl)
            driver.get_screenshot_as_file("E:\\Selenium\\loginpageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\loginpageSenac.jpg")                
            settings.loginPage("00001","00001")
            self.dateMFromR = '{:%d/%m/%Y}'.format(settings.dateSel("01/1/2017","01/1/2019", "%d/%m/%Y"))
            self.dateMFrom = self.dateMFromR[3:3+2]
            self.dateFromR2 = int(self.dateMFrom)-1
            driver.get_screenshot_as_file("E:\\Selenium\\homepageSenac_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\homepageSenac.jpeg")
            time.sleep(1)
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Configuraci\xf3n sistema")).perform()
            time.sleep(1)
            ActionChains(driver).click_and_hold(driver.find_element_by_link_text("Promociones")).perform()
            time.sleep(1)
            self.linkSel = 2##settings.ranNumbr(0,2)
            driver.find_element_by_link_text(promoSel[self.linkSel]).click()
            time.sleep(2)
            selectLink = {
                0: senacBackOffice.enfuncionRecarga,
                1: senacBackOffice.enfunciontransitos,
                2: senacBackOffice.enfuncionhorario
            }
            selectLink[self.linkSel](self)                    
        except:
            print( "No se puede crear Telecarga Promociones "+ promoSel[self.linkSel]+ " debido a: "+self.errorText)
            unittest.TestCase.fail(self,"No se puede crear Telecarga Promociones "+ promoSel[self.linkSel]+ " debido a: "+self.errorText)
                    
            
    def enfuncionRecarga(self):
        settings = self.settings
        driver = settings.driver
        driver.find_element_by_id("ctl00_ContentZone_BtnCreate").click()
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionRecarga_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionRecarga.jpeg")
        time.sleep(1.5)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionRecargaCreate_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionRecargaCreate.jpg")        
        driver.find_element_by_id("ctl00_ContentZone_txtNom_box_data").send_keys("PROMO_"+self.dateS[self.dateFromR2])
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").clear() 
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").send_keys(self.dateMFromR)
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").clear()
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").send_keys('{:%d/%m/%Y}'.format(settings.dateSel("01/01/2017", "31/12/2018","%d/%m/%Y")))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXtMsgPromotion_box_data").send_keys("Nueva Promoci\xf3n para "+self.dateS[self.dateFromR2])
        time.sleep(.50)
        settings.selectDropDown("ctl00_ContentZone_CboType")
        time.sleep(1)
        lanetype = Select(driver.find_element_by_id("ctl00_ContentZone_CboType"))
        lanetypeS = lanetype.first_selected_option.text        
        if lanetypeS == "V\xedas":
            settings.selectDropDown("ctl00_ContentZone_Vias")
            time.sleep(1)
            settings.selectDropDown("ctl00_ContentZone_Vias")
        time.sleep(1.5)
        ActionChains(driver).click(driver.find_element_by_id("ctl00_ContentZone_BtnCreate")).perform()
        time.sleep(1.5)
        driver.find_element_by_id("ctl00_ContentZone_TxtBoxImporte_box_data").clear()
        driver.find_element_by_id("ctl00_ContentZone_TxtBoxImporte_box_data").send_keys(str(settings.ranNumbr(1000,10000)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TxtboxPorcentaje_box_data").clear()
        driver.find_element_by_id("ctl00_ContentZone_TxtboxPorcentaje_box_data").send_keys(str(settings.ranNumbr(1,100)))
        time.sleep(.50)
        settings.elementClick("ctl00_ContentZone_BtnApply")
        time.sleep(2)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionRecargaCreateDataFill_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionRecargaCreateDataFill.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit")
        time.sleep(3)
        if self.isAlertPresent()==True:
            self.errorText = driver.switch_to_alert().text                        
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionRecargaErr_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionRecargaCreateErr.jpeg")            
            return
        else:
            time.sleep(1)
            settings.elementClick("ctl00_ButtonsZone_BtnDownload")
            time.sleep(1)
            driver.switch_to_alert().accept()
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionRecargaSuccess_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionRecargaSuccess.jpeg")
            successMessage = driver.find_element_by_id("ctl00_LblError").text
            time.sleep(3)
            print("Telecarga de Promociones "+ self.promoSel[self.linkSel]+" ha sido creada y Envio de Telecarga: "+successMessage);
            return;
            
    def enfunciontransitos(self):
        settings = self.settings
        telP = self.telP
        driver = settings.driver  
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionTransito_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionTransito.jpeg")
        settings.elementClick("ctl00_ContentZone_BtnCreate")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionTransitoCreate_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionTransitoCreate.jpg")
        driver.find_element_by_id("ctl00_ContentZone_txtNom_box_data").send_keys("PROMO_"+self.dateS[self.dateFromR2])
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").clear() 
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").send_keys(self.dateMFromR)
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").clear()
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").send_keys('{:%d/%m/%Y}'.format(settings.dateSel("01/01/2017", "31/12/2018","%d/%m/%Y")))            
        time.sleep(1)
        if (settings.ranNumbr(1,2)<2):
            driver.find_element_by_id(telP[settings.ranNumbr(0,1)]).click()
        else:
            driver.find_element_by_id(telP[0]).click()
            time.sleep(1)
            driver.find_element_by_id(telP[1]).click()                        
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXTNombrePassage_box_data").send_keys(str(settings.ranNumbr(1,999)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXTPassageGratuit_box_data").send_keys(str(settings.ranNumbr(1,999)))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXtMsgPromotionTFI_box_data").send_keys("Promoci\xf3n de "+self.dateS[self.dateFromR2])
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXtMsgPromotion_box_data").send_keys("La Nueva Promoci\xf3n de "+self.dateS[self.dateFromR2])
        time.sleep(.50)
        settings.selectDropDown("ctl00_ContentZone_Vias")
        time.sleep(.50)
        settings.selectDropDown("ctl00_ContentZone_Categoria")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionTransitoCreateFillData_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionTransitoCreateFillData.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit")
        time.sleep(3)                
        if self.isAlertPresent()==True:
            self.errorText = driver.switch_to_alert().text
            time.sleep(1)
            print("No se puede crear Telecarga Promociones "+ self.promoSel[self.linkSel]+ " debido a: "+self.errorText)                        
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionTransitoErr_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionTransitoErr.jpeg")
            return
        else:
            time.sleep(1)
            settings.elementClick("ctl00_ButtonsZone_BtnDownload")
            time.sleep(1)
            driver.switch_to_alert().accept();
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionTransitoSuccess_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionTransitoSuccess.jpeg")
            successMessage = driver.find_element_by_id("ctl00_LblError").text
            time.sleep(3)
            print("Telecarga de Promociones "+ self.promoSel[self.linkSel]+" ha sido creada y Envio de Telecarga: "+successMessage)
            time.sleep(1)
            return
            
    def enfuncionhorario(self):        
        settings = self.settings
        weekDays = self.weekDay
        driver = settings.driver
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionhorario_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionhorario.jpeg")
        settings.elementClick("ctl00_ContentZone_BtnCreate")
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionhorarioCreate_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionhorarioCreate.jpeg")
        driver.find_element_by_id("ctl00_ContentZone_txtNom_box_data").send_keys("PROMO_"+self.dateS[self.dateFromR2])
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").clear() 
        driver.find_element_by_id("ctl00_ContentZone_dtmfrom_box_date").send_keys(self.dateMFromR)
        time.sleep(1)
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").clear()
        driver.find_element_by_id("ctl00_ContentZone_dtmTo_box_date").send_keys('{:%d/%m/%Y}'.format(settings.dateSel("01/01/2017", "31/12/2018","%d/%m/%Y")))
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_TXtMsgPromotion_box_data").send_keys("La Nueva Promoci\xf3n de "+self.dateS[self.dateFromR2]);
        time.sleep(.50)
        settings.selectDropDown("ctl00_ContentZone_Vias")
        time.sleep(.50)
        settings.selectDropDown("ctl00_ContentZone_Categoria")                
        time.sleep(.50)
        weekS = settings.ranNumbr(1,8)                
        if (weekS < 8):
            for i in range(1,weekS):
                selW = settings.ranNumbr(1,i)
                time.sleep(.5)                
                settings.elementClick(weekDays[selW])                                
        time.sleep(.50)
        HourS = settings.ranNumbr(0,22)
        if HourS < 10:
            driver.find_element_by_id("ctl00_ContentZone_horainio_box_data").send_keys("0"+str(HourS)+"00")
            time.sleep(.50)
            if HourS+1<10:
                driver.find_element_by_id("ctl00_ContentZone_horafinal_box_data").send_keys("0"+str(HourS)+1+"00")
            else:
                driver.find_element_by_id("ctl00_ContentZone_horafinal_box_data").send_keys(str(HourS)+1+"00");                 
        else:
            driver.find_element_by_id("ctl00_ContentZone_horainio_box_data").send_keys(str(HourS)+"00");
            time.sleep(.50);
            driver.find_element_by_id("ctl00_ContentZone_horafinal_box_data").send_keys(str(HourS)+str(1)+"00");
                
        time.sleep(.50)
        driver.find_element_by_id("ctl00_ContentZone_porce_promotion_box_data").send_keys(str(settings.ranNumbr(1,100)))
        time.sleep(1)
        driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionhorarioCreateFillData_"+timet+".jpeg")
        driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionhorarioCreateFillData.jpeg")
        settings.elementClick("ctl00_ButtonsZone_BtnSubmit");
        time.sleep(3);
        if self.isAlertPresent()==True:
            self.errorText = driver.switch_to_alert().text
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionhorarioErr_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionhorarioErr.jpeg")
            return
        else:
            time.sleep(1)
            settings.elementClick("ctl00_ButtonsZone_BtnDownload")
            time.sleep(1)
            driver.switch_to_alert().accept()
            time.sleep(2)
            driver.get_screenshot_as_file("E:\\Selenium\\promoenFuncionhorarioSuccess_"+timet+".jpeg")
            driver.get_screenshot_as_file("E:\\workspace\\Mavi_Repository\\telecargas_Promociones\\attachments\\promoenFuncionhorarioSuccess.jpeg")
            successMessage = driver.find_element_by_id("ctl00_LblError").text
            time.sleep(3)
            print("Telecarga de Promociones "+ self.promoSel[self.linkSel]+" ha sido creada y Envio de Telecarga: "+successMessage)
            time.sleep(1)
            return
        
    def isAlertPresent (self):                                
        try:
            alert = self.settings.driver.switch_to_alert()
            alert.text
            if not alert == NULL:
                return True
            else:
                return False                 
        except NoAlertPresentException:
            time.sleep(2)
            return False    

if __name__== "__main__":
    unittest.main()
                    