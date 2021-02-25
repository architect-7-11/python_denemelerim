import requests
from win10toast import ToastNotifier
import json
import time

"""
bilgisayar bildirim ayarları açık olmalı !!!

"""

url = "https://coronavirus-19-api.herokuapp.com/all"

def update():
    source = requests.get(url)
    data = json.loads(source.text)
    data = source.json()
    text = f"onaylanmış hasta sayısı : {data['cases']} \nölüm : {data['deaths']} \niyileşen : {data['recovered']} "

    while True:
        toast = ToastNotifier()
        toast.show_toast("covid 19 güncelleme",text,duration=20)
        time.sleep(60)



update()














