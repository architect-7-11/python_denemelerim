
import json
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
from bilgiler import kişi


class E_okul():

    url = "https://eokulyd.meb.gov.tr/"

    def __init__(self,ad_soyad,tc,öğrenci_no,gün,ay,yıl,il,ilçe,şube,sınıf=0):
        self.ad_soyad = ad_soyad
        self.tc = tc
        self.öğrenci_no = öğrenci_no
        self.gün = gün
        self.ay = ay
        self.yıl = yıl
        self.il = il
        self.ilçe = ilçe
        self.şube = şube
        self.sınıf = sınıf
        self.browser = webdriver.Chrome()
        self.tumBilgiler = dict()
        self.aşama_1()
        self.vbs_güvenlik()
        self.notları_al()
        self.devamsızlık_al()
        self.json_yazdır()
        self.browser.close()


    def aşama_1(self):

        self.browser.get(E_okul.url)
        self.browser.find_element_by_xpath("//*[@id='information']/div/div/a[2]/img").click()
        time.sleep(2)
        sayilar = int(input(("görünen sayıyı girin : ")))
        self.browser.find_element_by_xpath("//*[@id='txtVBSImage']").send_keys(sayilar)
        time.sleep(2)
        self.browser.find_element_by_xpath("//*[@id='VBSKullanici']").send_keys(self.tc)
        time.sleep(1)
        self.browser.find_element_by_xpath("//*[@id='VBSpassword']").send_keys(self.öğrenci_no)
        self.browser.find_element_by_xpath("//*[@id='btnVBSGiris']").click()
        time.sleep(5)


    def vbs_güvenlik(self):
        
        alan1 = self.browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[3]/td[2]/span").text
        alan2 = self.browser.find_element_by_xpath("/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[5]/td[2]/span").text

        alan1_input = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[3]/td[4]/input"
        alan1_select = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[3]/td[4]/select"


        alan2_input = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[5]/td[4]/input"
        alan2_select = "/html/body/form/table/tbody/tr/td/table/tbody/tr/td[2]/table/tbody/tr[2]/td[2]/font/table/tbody/tr[5]/td[4]/select"


        if alan1 == "Öğrencinin doğum yılı nedir?":
            self.browser.find_element_by_xpath(alan1_input).send_keys(self.yıl)

        elif alan1 == "Öğrencinin nüfusa kayıtlı olduğu il hangisidir?":
            self.browser.find_element_by_xpath(alan1_select).send_keys(self.il)

        elif alan1 == "Öğrencinin nüfusa kayıtlı olduğu ilçe hangisidir?":
            self.browser.find_element_by_xpath(alan1_select).send_keys(self.ilçe)

        elif alan1 == "Öğrencinin doğum ayı hangisidir?":
            self.browser.find_element_by_xpath(alan1_select).send_keys(self.ay)

        elif alan1 == "Öğrencinin doğum günü hangisidir?":
            self.browser.find_element_by_xpath(alan1_select).send_keys(self.gün)
            

        elif alan1 == "Öğrencinin okuduğu şube hangisidir?":
            self.browser.find_element_by_xpath(alan1_select).send_keys(self.şube)

        time.sleep(2)

        if alan2 == "Öğrencinin doğum yılı nedir?":
            self.browser.find_element_by_xpath(alan2_input).send_keys(self.yıl)

        elif alan2 == "Öğrencinin nüfusa kayıtlı olduğu il hangisidir?":
            self.browser.find_element_by_xpath(alan2_select).send_keys(self.il)

        elif alan2 == "Öğrencinin nüfusa kayıtlı olduğu ilçe hangisidir?":
            self.browser.find_element_by_xpath(alan2_select).send_keys(self.ilçe)

        elif alan2 == "Öğrencinin doğum ayı hangisidir?":
            self.browser.find_element_by_xpath(alan2_select).send_keys(self.ay)

        elif alan2 == "Öğrencinin doğum günü hangisidir?":
            self.browser.find_element_by_xpath(alan2_select).send_keys(self.gün)
            
        elif alan2 == "Öğrencinin okuduğu şube hangisidir?":
            self.browser.find_element_by_xpath(alan2_select).send_keys(self.şube)

        time.sleep(5)
        self.browser.find_element_by_xpath("//*[@id='btnTamam']").click()
        time.sleep(5)

    def notları_al(self):
        self.browser.find_element_by_xpath("//*[@id='IOV02000']/tbody/tr[3]/td").click()
        if self.sınıf != 0:
            self.browser.find_element_by_xpath("//*[@id='IOVMenu1_ddlOgrenciSiniflari']").send_keys(self.sınıf,Keys.ENTER)
        time.sleep(1)
        source = self.browser.page_source
        soup = BeautifulSoup(source,"html.parser")
        tablo = soup.find("table",id="tblNotlarIDonem")
        dönem = tablo.find("table",id="Table3")
        satırlar = dönem.find_all("tr")
        liste2 = list()
        start = 0
        for s in satırlar:

            if start >= 2:
                veriler = s.find_all("td")

                for v in veriler:
                    veri = v.text.strip().lower()
                    liste2.append(veri)
                    if len(liste2) == 11:
                        self.tumBilgiler[liste2[0]] = liste2[1:]
                        liste2 = list()
            else:
                start +=1
        print(self.tumBilgiler)
        
    def devamsızlık_al(self):
        self.browser.find_element_by_xpath("//*[@id='IOV02000']/tbody/tr[2]/td").click()
        if self.sınıf != 0:
            self.browser.find_element_by_xpath("//*[@id='IOVMenu1_ddlOgrenciSiniflari']").send_keys(self.sınıf,Keys.ENTER)
        time.sleep(1)
        devamsızlıklar = self.browser.page_source
        time.sleep(1)
        kaynak = BeautifulSoup(devamsızlıklar,"html.parser")
        ösüz = kaynak.find(id="tblOzursuzDevamsizlikToplam")
        özürsüz_D = ösüz.text.split()

        ölü = kaynak.find(id="tblOzurluDevamsizlikToplam")
        özürlü_D = ölü.text.split()

        geckalinan = kaynak.find(id="tblGecDevamsizlikToplam")
        gecKalma_D = geckalinan.text.split()

        try:
            self.tumBilgiler['özürsüz devamsızlıklar '] = özürsüz_D[8] + " " + özürsüz_D[9] 
        except Exception as er:
            self.tumBilgiler['özürsüz devamsızlıklar '] = 'devamsızlık bulunmuyor.'
        
        try:
            self.tumBilgiler['özürlü devamsızlıklar'] = özürlü_D[5] + " " + özürlü_D[6] 
        except Exception as er:
            self.tumBilgiler['özürlü devamsızlıklar'] = 'devamsızlık bulunmuyor.'

        try:
            self.tumBilgiler['geç devamsızlık toplam'] = gecKalma_D[5] + " " + gecKalma_D[6] 
        except Exception as er:
            self.tumBilgiler['geç devamsızlık toplam'] = 'devamsızlık bulunmuyor.'

    def json_yazdır(self):    
        json_info = json.dumps(self.tumBilgiler,ensure_ascii=False)
        with open(f"{self.ad_soyad}.json" , "a" ,encoding="utf8") as file:
            json.dump(json_info,file,ensure_ascii=False)



print(E_okul(kişi["adı_soyadı"],kişi["tc"],kişi["öğrenci_no"],kişi["gün"],kişi["ay"],kişi["yıl"],kişi["il"],kişi["ilçe"],kişi["şube"]))












