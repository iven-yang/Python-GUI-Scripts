
import pyautogui
import random
import time

from random import randint

#Face north, be zoomed all the way in, with camera from highest angle
#Chop the ivy from the left of the wall (bottom right of varrock castle is a good place)

runs = randint(300,350) # 5.25-6.09 hours
pyautogui.PAUSE = 0.01

time.sleep(2.5)

try:
	while runs>0: # about 62.7 seconds per iteration
		mousex = randint(1015, 1025)
		mousey = randint(510, 535)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()
		time.sleep(random.uniform(0.08, 0.2))
		pyautogui.mouseUp()
		
		time.sleep(random.uniform(55, 70))
		
		runs -= 1

except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')