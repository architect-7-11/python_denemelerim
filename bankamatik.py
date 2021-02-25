



kemal = {"adı":"kemal",
"hesapno":22645216,
"hesap":2000,
"yedekhesap":1500
} 


ali = {"adı":"ali",
"hesapno":15400563,
"hesap":3000,
"yedekhesap":2500
} 


liste = [kemal,ali]


class Banka_islemleri:

    def __init__(self,adı,hesapno,hesap,yedekhesap):
        self.adı = adı
        self.hesapno = hesapno
        self.hesap = hesap
        self.yedekhesap = yedekhesap

    def paraCek(self):
        miktar = int(input("ne kadar para çekmek istiyorsunuz?"))
        if self.hesap < miktar:
            sor = input("""ana hesap bakiyeniz yetersiz!!!
            yedek hesapdan para kullanmak ister misiniz?(e/h)""")
            sor = sor.lower()

            if sor == "e":
                yedekdenMiktar = miktar - self.hesap
                self.hesap = 0
                self.yedekhesap -= yedekdenMiktar
            
            else:
                print("şuan paranızı veremiyoruz")
        
        else:
            self.hesap -=miktar 
            print("paranızı alabilirsiniz")
                

    def paraEkle(self):
        miktar = int(input("Lütfen eklemek istediğiniz paranın miktarını girin..."))
        hesapTercih = input("hangi hesaba eklemek isteyorsunuz?(A/Y)")
        hesapTercih = hesapTercih.lower()
        if hesapTercih == "a":
            self.hesap +=miktar
        else:
            self.yedekhesap +=miktar 

    def bakiyeSorgula(self):
        tercih = input("hangi hasabı görüntülemek istiyorsunuz?(A/Y)")
        tercih = tercih.lower()
        if tercih == "a":
            print(f"Ana hesap bakiyeniz : {self.hesap}")

        else:
            print(f"Yedek hesap bakiyeniz : {self.yedekhesap}")

    def bilgileriSorgula(self):
        print(f"""
        adı:{self.adı}
        hesapno:{self.hesapno}
        hesap:{self.hesap}
        yedekhesap:{self.yedekhesap}
        """)


while True:

    kullanıcı = input("hangi kullanıcı için işlem yapıcaksınız?")
    kullanıcı = kullanıcı.lower()
    if kullanıcı == "kamil":
        kullanıcı = liste[1]
    else:
        kullanıcı = liste[0]

    while True:
        islem = input("""
        lütfen yapmak istediğiniz işlemi seçiniz :
        1 : Para çek
        2 : Para ekleme
        3 : Bakiye sorgulama
        4 : Bilgileri sorgulama
        Q : çıkış yap
        """)

        bankamatik = Banka_islemleri(kullanıcı["adı"],kullanıcı["hesapno"],kullanıcı["hesap"],kullanıcı["yedekhesap"])

        if islem == "1":
            bankamatik.paraCek()
            
            sor = input("başka bir işlem yapmak istiyor musunuz? (e/h) ")
            sor = sor.lower()
            if sor == "e":
                continue
            else:
                break

        elif islem == "2":
            bankamatik.paraEkle()
            sor = input("başka bir işlem yapmak istiyor musunuz? (e/h) ")
            sor = sor.lower()
            if sor == "e":
                continue
            else:
                break
        elif islem == "3":
            bankamatik.bakiyeSorgula()
            sor = input("başka bir işlem yapmak istiyor musunuz? (e/h) ")
            sor = sor.lower()
            if sor == "e":
                continue
            else:
                break
        elif islem == "4":
            bankamatik.bilgileriSorgula()
            sor = input("başka bir işlem yapmak istiyor musunuz? (e/h) ")
            sor = sor.lower()
            if sor == "e":
                continue
            else:
                break
        
        elif (islem=="q") or (islem == "Q"):
            break

    break
            













