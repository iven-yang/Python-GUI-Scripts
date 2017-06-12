
import random
import math
import time

from resources.mouse import MouseClick
from random import randint

#Go to a world with few people
#Face north, zoomed fully out, with highest camera angle
#Stand in Dwarven Mines near Falador entrance at 3 iron stones next to the Dungeoneering entrance
'''
      o
  o   x      <- stand at the x
o
'''

runs = randint(30, 35) # 1.22-1.42 hours
# runs = randint(110, 120) # 4.2-5.2 hours

time.sleep(2.5)

try:
	while runs>0: # about 146 sec per iteration
		iron_cycles = 0
		
		#Mine irons until inv full (27)
		while iron_cycles<9: # about 13.5 sec per iteration
			#Bottom left iron
			MouseClick.left_click(804, 813, 582, 588)
			time.sleep(random.uniform(3.75, 4.05))
			
			#Middle iron
			MouseClick.left_click(957, 963, 489, 494)
			time.sleep(random.uniform(3.5, 3.8))
			
			#Top right iron
			MouseClick.left_click(1064, 1071, 434, 439)
			time.sleep(random.uniform(4.9, 5.4))
			
			if random.uniform(0,13)>12:
				time.sleep(random.uniform(20,40))
			
			iron_cycles += 1
		
		#Enter dungeon to bank (you will be standing at starting location)
		MouseClick.left_click(604, 627, 730, 753)
		if random.uniform(0,14) > 13:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(10,13))
		else:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(4,4.5))
		
		#Click Deposit Box
		MouseClick.left_click(1005, 1017, 392, 401)
		time.sleep(random.uniform(4.75, 5.25))
		
		#Deposit inventory
		MouseClick.left_click(1004, 1016, 631, 641)
		time.sleep(random.uniform(1.8, 2))
		
		#Exit
		MouseClick.left_click(788, 800, 705, 709)
		if random.uniform(0,10) > 9:
			time.sleep(random.uniform(10, 15))
		else:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(2.4,2.5))
		
		#Click top right iron and re-loop
		MouseClick.left_click(1202, 1210, 304, 309)
		time.sleep(random.uniform(5.1, 5.8))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
