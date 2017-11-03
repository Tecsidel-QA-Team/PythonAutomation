# -*- coding: utf-8 -*-

import unittest
import time
from Settingsfields_File import  Settingsfields_File 

import BOHost_VerTransacciones
import pypyodbc
from time import gmtime, strftime 
          
class BO_verConfirmacion_TransitosSubidos(unittest.TestCase):    
            
    def setUp(self):
        self.settings = Settingsfields_File()
        self.settings.setUp()
        
    def test(self):   
        settings = self.settings
        driver = settings.driver       
        self.dateverTransacciones = strftime("%d/%m/%Y", gmtime()) ##"21/09/2017" 
        self.transSearch = strftime("%Y%m%d", gmtime()) ##"20170921"
        try:
            BO_verConfirmacion_TransitosSubidos.conexionBaseDatos(self, "Plaza")
            BO_verConfirmacion_TransitosSubidos.conexionBaseDatos(self, "Host")
            time.sleep(1)
            BOHost_VerTransacciones.BOHost_VerTransacciones.verTransacciones(self)
            tablResult = driver.find_element_by_id("ctl00_ContentZone_tbl_logs")
            transResult = tablResult.find_elements_by_tag_name("tr")
            if len(transResult)<3:
                print("No hay Transacciones en el BackOffice Web con fecha de hoy")
                self.fail("No hay Transacciones en el BackOffice Web con fecha de hoy")
                return                                
            elementsFound = driver.find_element_by_id("ctl00_ContentZone_tablePager_LblCounter").text
            elementBg=24
            elementEd=25
            if len(transResult)>11:
                elementBg = 25
                elementEd=27
            if len(transResult)<19:
                transRes = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_tbl_logs']/tbody/tr["+str(len(transResult))+"]/td[1]/a").text                                    
                if transRes == self.transactionListH[0][1]:
                    print("Hay "+elementsFound[elementBg:elementEd]+" transacciones y el último tránsito: "+self.transactionListH[0][1]+" ha subido satisfactoriamente el dia de hoy "+self.dateverTransacciones+" "+self.transactionListH[0][0][8:10]+":"+self.transactionListH[0][0][10:12]+":"+self.transactionListH[0][0][12:14])
                    return
                else:
                    print("No se ha subido el último tránsito a BackOffice Web desde HostManage de hoy")
                    self.fail("No se ha subido el último tránsito a BackOffice Web HostManage con fecha de hoy");
                    return
                           
            else:
                settings.elementClick("ctl00_ContentZone_tablePager_BtnLast")
                tablResult = driver.find_element_by_id("ctl00_ContentZone_tbl_logs")
                transResult = tablResult.find_elements_by_tag_name("tr")
                transRes = driver.find_element_by_xpath("//*[@id='ctl00_ContentZone_tbl_logs']/tbody/tr["+str(len(transResult))+"]/td[1]/a").text
                if transRes == self.transactionListH[0][1]:
                    print("Hay "+elementsFound[elementBg:elementEd]+" transacciones y el último tránsito: "+self.transactionListH[0][1]+" ha subido satisfactoriamente el dia de hoy "+self.dateverTransacciones+" "+self.transactionListH[0][0][8:10]+":"+self.transactionListH[0][0][10:12]+":"+self.transactionListH[0][0][12:14])
                    driver.close()
                    return
                    
                else:
                    print("No se ha subido el último tránsito a BackOffice Web desde HostManage de hoy")
                    self.fail("No se ha subido el último tránsito a BackOffice Web HostManage con fecha de hoy")
                    driver.close()
                    return           
        except:
            unittest.TestCase.fail(self)

    def conexionBaseDatos(self, Bd):
        self.cnn = pypyodbc.connect("DRIVER={SQL Server};"
                                        "SERVER=172.18.130.188;"
                                        "DATABASE=COVIHONDURAS_QA_TOLL"+str(Bd).upper()+";"
                                        "UID=sa;"
                                        "PWD=lediscet")
        query = self.cnn.cursor()
        time.sleep(2)
        query.execute("select passagetime,transactionid  from dbo.atransaction where passagetime like '"+self.transSearch+"%' ORDER BY passagetime DESC")
        transactions= query.fetchall()
               
        if transactions == []:
            self.fail("No han subido tránsitos a "+str(Bd)+" con fecha de hoy: "+self.dateverTransacciones)
        else:  
            print("En "+str(Bd)+ " han subido hoy: "+str(len(transactions)))            
            self.transactionListP=[]
            self.transactionListH=[]
            if Bd == "Plaza":
                for transactions in transactions:
                    self.transactionListP.append(transactions)
            else:
                for transactions in transactions:
                    self.transactionListH.append(transactions)
                
        self.cnn.commit()
        self.cnn.close()
        
if __name__== "__main__":
    unittest.main()    
