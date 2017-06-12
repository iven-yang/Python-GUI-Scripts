
import random
import math
import time

from resources.mouse import MouseClick
from random import randint

#Have at least 82,500 each of feathers and shafts
#Put shafts in very top left of inventory

runs = randint(200, 225) # 1-1.15 hours

time.sleep(2.5)

try:
	while runs>0: # about 17.5 sec per iteration
		#Very Upper Left Inv Slot
		MouseClick.left_click(1734, 1742, 735, 748)
		time.sleep(random.uniform(2.1, 2.3))
		
		#Button to Start Fletching
		MouseClick.left_click(1024, 1112, 670, 685)
		
		#Rando Stuff
		time.sleep((4.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(1.65,1.75))
		
		if random.uniform(0,9) > 8:
			MouseClick.left_click(1505, 1516, 1015, 1025)
			time.sleep(random.uniform(2,4))
			
			MouseClick.left_click(1567, 1576, 1015, 1025)
			time.sleep(random.uniform(4.6,6))
			
		elif random.uniform(0,8) > 7:
			MouseClick.left_click(1595, 1605, 1015, 1025)
			time.sleep(random.uniform(1.5,2))
			
			MouseClick.left_click(1567, 1576, 1015, 1025)
			time.sleep(random.uniform(5.1,6))
			
		else:
			time.sleep((4.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(1.65,1.75))
		
		if random.uniform(0,15) > 14:
			MouseClick.left_click(1881, 1890, 739, 745)
			time.sleep(random.uniform(1.1, 1.3))
		if random.uniform(0,18) > 17:
			time.sleep(random.uniform(20,30))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
