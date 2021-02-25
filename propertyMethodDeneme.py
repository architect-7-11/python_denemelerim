
class musician:

    def __init__(self,age,income=0):
        self.__age = age
        self.__income = income
        self.__validataion = False



    def enter_club(self):
        if self.__age >= 21:
            self.__validataion = True
        return self.__validataion

    def play_show(self):
        if self.__validataion:
            self.__income += 500



    def test(self,value):
        return  musician(self.__age + value)

    @property               
    def income(self):
        return self.__income 

    @income.setter                 
    def income(self,value):
        if self.__validataion :
            self.__income = value


muzisyen = musician(14)

if muzisyen.enter_club():
    print("kulübe hoşgelsiniz...")
    muzisyen.play_show()
    print(f"müzisyenin maaşı {muzisyen.income} ")
    muzisyen.play_show()
    print(f"müzisyenin maaşı {muzisyen.income} ")
    muzisyen.income = 1000
    print(f"müzisyenin maaşı {muzisyen.income} ")

else:
    print("yaşınız uygun değil")



































