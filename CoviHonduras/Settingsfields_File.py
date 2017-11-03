# -*- coding: utf-8 -*-

from selenium import webdriver
import os
import random
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import Select

BoHostUrl="http://virtualbo-qa/BOQAHostCoviHonduras/web/forms/core/login.aspx"
BoPlazaUrl="http://virtualbo-qa/BOQAPlazaCoviHonduras/web/forms/core/login.aspx"
RUCid = "ctl00_ContentZone_ctrlAccountData_txt_RUC_box_data"
infoCuenta0 = "ctl00_ContentZone_ctrlAccountData_radio_company_0"
infoCuenta1 = "ctl00_ContentZone_ctrlAccountData_radio_company_1"
titulofield = "ctl00_ContentZone_ctrlAccountData_cmb_title_cmb_dropdown"
namef = "ctl00_ContentZone_ctrlAccountData_txt_forname_box_data"
surnamef ="ctl00_ContentZone_ctrlAccountData_txt_surname_box_data"
addressf = "ctl00_ContentZone_ctrlAccountData_txt_address_box_data"
cpf = "ctl00_ContentZone_ctrlAccountData_txt_postcode_box_data"
townf = "ctl00_ContentZone_ctrlAccountData_txt_town_box_data"
countryf = "ctl00_ContentZone_ctrlAccountData_txt_country_box_data"
emailf ="ctl00_ContentZone_ctrlAccountData_txt_email_box_data"
phoneCel = "ctl00_ContentZone_ctrlAccountData_txt_mobile_box_data"
workPhone = "ctl00_ContentZone_ctrlAccountData_txt_daytimephone_box_data"
perPhone = "ctl00_ContentZone_ctrlAccountData_txt_homephone_box_data"
faxPhone = "ctl00_ContentZone_ctrlAccountData_txt_fax_box_data"
companyf = "ctl00_ContentZone_ctrlAccountData_txt_company_box_data"
contactf = "ctl00_ContentZone_ctrlAccountData_txt_contact_box_data"
carSel=0
carModel=0
mcsVersion = "lbl_version" 
confirmationMessage=""
errorTagAssignment = False
colorS = ["Blanco", "Negro", "Azul", "Rojo", "Verde", "Amarillo"]
matletT = "TRWAGMYFPDXBNJZSQVHLCKE";
accountNumbrT="" 
carSel=0
carModel=0
matriNu=""
vehtypeModel=""
vehtypeKind=""
cocheModels = [["Seat","Volkswagen","Ford","Fiat"],["Ibiza","Polo","Fiesta","Punto"],["León","Passat","Focus","Stilo"]]
camionModels = [["Mercedes-Benz","Scania"],["Axor","R500"],["Actros","P400"]]
furgonetaModels = [["Mercedes-Benz","Fiat"],["Vito","Scudo"],["Citan","Ducato"]]
cicloModels = [["Yamaha","Honda"],["XT1200Z","Forza 300"],["T-MAX SX","X-ADV"]]
autoBusModels = [["DAIMLER-BENZ","VOLVO"],["512-CDI","FM-12380"],["DB 605","FM 300"]]
Letter_Comb = "TRWAGMYFPDXBNJZSQVHLCKE"
timet = ('{:%Y%m%d%H%M%S}'.format(datetime.now()))   
CaCUrl="http://virtualcac-qa/CACQACovihonduras/web/forms/core/login.aspx"    
acceptNextAlert = True;
numbering=0
Types=""
tipoSel=""
loginField = "BoxLogin";
passField = "BoxPassword";
loginButton = "BtnLogin";
opIdField = "ctl00_ContentZone_operatorId_box_data";
nameField = "ctl00_ContentZone_forename_box_data";
lastNameField = "ctl00_ContentZone_surname_box_data";
emailField = "ctl00_ContentZone_email_box_data";
groupOperator = "ctl00_ContentZone_group_cmb_dropdown";
pwdField = "ctl00_ContentZone_password_box_data";
repeatpwdField = "ctl00_ContentZone_password2_box_data";
hourNumber = "ctl00_ContentZone_TxtNomHousr_box_data";
submitBtn = "ctl00_ButtonsZone_BtnSubmit";
MCSUrl="http://virtualmcs-qa/MCS_CoviHonduras";
MCSVersion=""
BOVersion=""
HMVersion=""
nameOp = ["Pilar", "Mavi", "Franklyn", "Gemma", "Fatima", "Marc", "Miguel", "Francisco", "Oscar", "Maria"]
genderS = ["Femenino", "Femenino", "Masculino", "Femenino", "Femenino", "Masculino", "Masculino", "Masculino", "Masculino", "Femenino"]
sexSelc = ["Sra", "Sra", "Sr", "Sra", "Sra", "Sr", "Sr", "Sr", "Sr", "Sra"]
addressTec = ["CALLE SAN MAXIMO, 3","CALLE SAN MAXIMO, 3","Castanyer 29", "CALLE SAN MAXIMO, 3","CALLE SAN MAXIMO, 3","Catanyer 29","Edificio Tecsidel, P.T. de Boecillo","Edificio Tecsidel, P.T. de Boecillo","Edificio Tecsidel, P.T. de Boecillo","Edificio Tecsidel, P.T. de Boecillo"]
cpAdress = ["28041", "28041", "08022", "28041", "28041","08022","47151","47151","47151","47151"]
townC = ["Madrid", "Madrid", "Barcelona", "Madrid", "Madrid", "Barcelona", "Valladolid","Valladolid","Valladolid","Valladolid"]
workPhone1 = ["913530810","913530810","932922110","913530810","913530810","932922110","983546603","983546603","983546603","983546603"]
lastNameOp = ["Bonilla", "Garrido", "Garcia", "Arjonilla", "Romano", "Navarro", "Sanchez", "Castro", "Bailon", "Blanco"]
                
 
class Settingsfields_File():
    def setUp(self):    
        self.driver = webdriver.Chrome("C:/Selenium/chromedriver")        
        ##self.driver.maximize_window()
             
 
    def borrarArchivos(self,ruta):
        for ruta, subdirs, files in os.walk(ruta):
            for name in files:
                os.remove(ruta+name , dir_fd=None)            
            
    def selectDropDown(self, By):        
        driver = self.driver
        vDropdown = Select(driver.find_element_by_id(By))
        dd = vDropdown.options
        vdd = random.randint(0,len(dd)-1)
        if vdd<0:
            vdd= 0
        if vdd>=len(dd):
            vdd = len(dd)-1
        Select(driver.find_element_by_id(By)).select_by_index(vdd)
    
    def loginPage(self, usr,pwd):
        driver = self.driver
        driver.find_element_by_id(loginField).send_keys(usr)
        driver.find_element_by_id(passField).send_keys(pwd)
        driver.find_element_by_id(loginButton).click()
        time.sleep(2)
        
    def loginPageMCS(self, usr,pwd):
        driver = self.driver
        driver.find_element_by_id("txt_login").send_keys(usr)
        driver.find_element_by_id("txt_password").send_keys(pwd)
        driver.find_element_by_id("btn_login").click()
        time.sleep(2)
    
    def ranNumbr(self, val1, val2):
        return (random.randint(val1, val2))
    
    def elementClick(self, By):
        driver = self.driver
        driver.find_element_by_id(By).click()

    def dateSel(self, start, end, fmt):
        s = datetime.strptime(start, fmt)
        e = datetime.strptime(end, fmt)
        delta = e - s
        return s + timedelta(days=(random.random() * delta.days))