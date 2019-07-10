import pyautogui
import time

time.sleep(0.5)
pyautogui.PAUSE = 0

x = 0
while x<500:
    time.sleep(0.05)
    pyautogui.click()
    x += 1
