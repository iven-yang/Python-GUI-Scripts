
import pyautogui
import random
import time

from random import randint

#Have at least 331 of the stuff you are alching
#Have the stuff being alched under the bottom of the high alch spell

runs = randint(730,750) # 17-17.5 min
pyautogui.PAUSE = 0.01

time.sleep(2.5)

try:
	while runs>0: # about 1.4 sec per iteration
		mousex = randint(1732,1743)
		mousey = randint(836, 842)
		pyautogui.moveTo(mousex, mousey)		
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()
		time.sleep(random.uniform(0.08, 0.2))
		pyautogui.mouseUp()
		
		time.sleep(random.uniform(1.113, 1.324))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')