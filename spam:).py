import pyautogui as auto
from time import sleep

for i in range(20):
        auto.write("That's not me...It's Neo")
        auto.press('enter')
        sleep(0.4)