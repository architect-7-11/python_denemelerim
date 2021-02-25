
import time
import pyautogui


def screenShot():
    number = int(round(time.time() * 1000))
    name = f"{number}.png"
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()


screenShot()














