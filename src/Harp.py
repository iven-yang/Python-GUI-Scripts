
import pyautogui
import random
import time

from random import randint

#Face north. zoom all the way out, with camera at highest angle possible
#Play the harp from the left

runs = randint(335,345) # around 5.2 hours
pyautogui.PAUSE = 0.01

time.sleep(2.5)

try:
	while runs>0:
		mousex = randint(893, 927)
		mousey = randint(520, 546)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()
		time.sleep(random.uniform(0.08, 0.2))
		pyautogui.mouseUp()
		
		time.sleep(random.uniform(45, 65))
		
		runs -= 1

except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')