
import random
import time

import pyautogui

# For 3x6 snake game, starting point at (2,2)
# 0.07 sec per frame

pyautogui.PAUSE = 0
time.sleep(2)

pyautogui.press('up')
time.sleep(0.07)
pyautogui.press('left')
time.sleep(0.07)

while True:
    for x in range(2):
        pyautogui.press('down')
        time.sleep(0.07)
        pyautogui.press('right')
        time.sleep(0.07)
        pyautogui.press('down')
        time.sleep(0.07)
        pyautogui.press('left')
        time.sleep(0.07)
    # We are now at bottom left
    pyautogui.press('down')
    time.sleep(0.07)
    pyautogui.press('right')
    time.sleep(0.14) # Go right 2
    pyautogui.press('up')
    time.sleep(0.355) # Go up 6
    pyautogui.press('left')
    time.sleep(0.14) # Go left 2

