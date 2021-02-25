

import time
import random

class kumanda():
    def __init__(self,tv_durumu="kapalı",ses_durumu=0,kanal_listesi=["trt"],kanal="trt",uydu="turksat 1A"):
        print("kumanda durumu özellikleri")
        self.tv_durumu=tv_durumu
        self.ses_durumu=ses_durumu
        self.kanal=kanal
        self.kanal_listesi=kanal_listesi
        self.uydu=uydu

    def bilgileri_goster(self):
        print(f"""TV için genel bilgiler:
        tv durumu     :{self.ses_durumu}
        ses durumu    :{self.ses_durumu}
        izlenen kanal :{self.kanal}
        kanal listesi :{self.kanal_listesi}
        uydu linki    :{self.uydu}
        """)
    
    def __len__(self):
        return len(self.kanal_listesi)

    def __str__(self):
        return f"tv durumu {self.tv_durumu} ve {self.kanal} kanalını izliyorsunuz.."

    def kanal_ekle(self,yeni_kanal):
        self.kanal_listesi.append(yeni_kanal)
    
    def tv_ac(self):
        print("tv açılıyor...")
        time.sleep(1)
        self.tv_durum="açık"

    def tv_kapat(self):
        print ("tv kapatılıyor...")
        time.sleep(1)
        self.tv_durum="kapalı"

    def ses_ayar(self):
        while True:
            giris=input("""tv ses durumunu arttırmak için > tuşuna basın
            tv ses durumunu azaltmak için < tuşuna basın
            çıkmak için q tuşuna basınız...:""")
            
            if giris==">":
                if self.ses_durumu < 32:
                    self.ses_durumu +=1
                    print (self.ses_durumu)
            elif giris =="<":
                if self.ses_durumu > 0:
                    self.ses_durumu -=1
                    print(self.ses_durumu)
            
            elif giris == "q":
                print("çıkış yapılıyor...")
                time.sleep(0.5)
                break
            else:
                print("yanlış giriş")

    def rastgele_kanal(self):
        rastgele=random.randint(0,len(self.kanal_listesi)-1)
        kanal=self.kanal_listesi[rastgele]
        self.kanal = kanal
        print(self.kanal)

    def kanallar(self):
        print(f"kayıtlı kanallar:{self.kanal_listesi}")


sony = kumanda()

print("""
    kumanda kullanımı:
    Lütfen yapmak isteidğiniz işlemi seçiniz:
    1.Tv aç
    2.Tv kapat
    3.bilgileri göster
    4.Kanal ekle
    5.Ses aç-kapat
    6.Rastgele kanal seç
    7.kanal listesi
    8.kanal sayısı
    """)



while True:
    
    istek=input ("lütfen yapmak istediğiniz işlemi girin...:")

    if istek == "1":
        sony.tv_ac()
        time.sleep(0.5)
        print("tv açıldı.")

    elif istek=="2":
        sony.tv_kapat()
        print("tv kapatıldı.")

    elif istek == "3":
        print(sony.bilgileri_goster())

    elif istek == "4":
        yeni_kanal_talebi=input("""lütfem eklemek istediğiniz kanallar arasına
        (,) koyarak ayırınız""")
        talep=yeni_kanal_talebi.split(",")
        for i in talep:
            sony.kanal_ekle(i)
        time.sleep(0.5)
        print("kanallar eklendi")

    elif istek == "5":
        sony.ses_ayar()

    elif istek == "6":
        sony.rastgele_kanal()
    
    elif istek == "7":
        sony.kanallar()
            
    elif istek == "8":
        print(len(sony))
            




