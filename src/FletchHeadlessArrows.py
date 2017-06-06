
import pyautogui
import random
import math
import time

from random import randint

#Have at least 82,500 each of feathers and shafts
#Put shafts in very top left of inventory

runs = randint(520, 550) # 2.53-2.67 hours
pyautogui.PAUSE = 0.01

time.sleep(2.5)

try:
	while runs>0: # about 17.5 sec per iteration
		#Very Upper Left Inv Slot
		mousex = randint(1734,1742)
		mousey = randint(735, 748)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()		
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		time.sleep(random.uniform(2.113, 2.524))
		
		#Button to Start Fletching
		mousex = randint(1024,1112)
		mousey = randint(670, 685)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()
		time.sleep(random.uniform(0.08, 0.2))
		pyautogui.mouseUp()
		
		time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(6.5,7.8))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')