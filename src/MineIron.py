
import pyautogui
import random
import math
import time

from random import randint

#Go to a world with few people
#Face north, zoomed fully out, with highest camera angle
#Stand in Dwarven Mines near Falador entrance at 3 iron stones next to the Dungeoneering entrance
'''
      o
  o   x      <- stand at the x
o
'''

runs = randint(110, 120) # 4.06-4.87 hours
pyautogui.PAUSE = 0.01

time.sleep(2.5)

try:
	while runs>0: # about 146 sec per iteration
		iron_cycles = 0
		
		#Mine irons until inv full (27)
		while iron_cycles<9: # about 13.5 sec per iteration
			#Bottom left iron
			mousex = randint(804,813)
			mousey = randint(582, 588)
			pyautogui.moveTo(mousex, mousey)
			time.sleep(random.uniform(0.1, 0.2))
		
			pyautogui.mouseDown()		
			time.sleep(random.uniform(0.08, 0.2))		
			pyautogui.mouseUp()
		
			time.sleep(random.uniform(3.85, 3.95))
			
			#Middle iron
			mousex = randint(957,963)
			mousey = randint(489, 494)
			pyautogui.moveTo(mousex, mousey)
			time.sleep(random.uniform(0.1, 0.2))
		
			pyautogui.mouseDown()		
			time.sleep(random.uniform(0.08, 0.2))		
			pyautogui.mouseUp()
		
			time.sleep(random.uniform(3.6, 3.7))
			
			#Top right iron
			mousex = randint(1064,1071)
			mousey = randint(434, 439)
			pyautogui.moveTo(mousex, mousey)
			time.sleep(random.uniform(0.1, 0.2))
		
			pyautogui.mouseDown()		
			time.sleep(random.uniform(0.08, 0.2))		
			pyautogui.mouseUp()
		
			time.sleep(random.uniform(5.1, 5.4))
			
			iron_cycles += 1
		
		#Enter dungeon to bank (you will be standing at starting location)
		mousex = randint(604,627)
		mousey = randint(730, 753)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		if random.uniform(0,14) > 13:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(6,8))
		else:
			time.sleep(random.uniform(6.45, 6.65))
		
		#Click Deposit Box
		mousex = randint(1005,1017)
		mousey = randint(392, 401)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()		
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		time.sleep(random.uniform(2.5, 2.65))
		
		#Deposit inventory
		mousex = randint(1004,1016)
		mousey = randint(631, 641)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()		
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		time.sleep(random.uniform(1.45, 1.55))
		
		#Exit
		mousex = randint(788,800)
		mousey = randint(705, 709)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()		
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		if random.uniform(0,10) > 9:
			time.sleep(random.uniform(7, 12))
		else:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(2.0,2.1))
		
		#Click top right iron and re-loop
		mousex = randint(1202,1210)
		mousey = randint(304, 309)
		pyautogui.moveTo(mousex, mousey)
		time.sleep(random.uniform(0.1, 0.2))
		
		pyautogui.mouseDown()		
		time.sleep(random.uniform(0.08, 0.2))		
		pyautogui.mouseUp()	
		
		time.sleep(random.uniform(5.1, 5.8))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')