
import random
import math
import time

from resources.mouse import MouseClick
from resources.keyboard import Keyboard
from random import randint

# Have at least 42,150 each of feathers and shafts
# Put shafts in very top left of inventory, feathers in second slot
# Leave third and fourth inventory slot empty (headless shafts made will go in third slot)

runs = randint(250, 281) # 1.04-1.17 hours

time.sleep(2.5)

try:
	while runs>0: # About 15 sec per iteration
		# Very Upper Left Inv Slot
		MouseClick.left_click(1734, 1742, 735, 748)
		
		# Button to Start Fletching (Space or click)
		if random.uniform(0, 7) > 6:
			time.sleep(random.uniform(1.9, 2.2))
			MouseClick.left_click(1024, 1112, 670, 685)
		else:
			time.sleep(random.uniform(1.5, 1.7))
			# Press the space key a random amount of times between 1 and 6 times
			presses = int(round( (0.21+random.uniform(0,1)*random.uniform(0,1))*5 )) 
			while presses > 0:
				Keyboard.push('space')
				presses -= 1
				time.sleep(random.uniform(0.2, 0.3))
		
		time.sleep((4.0+random.uniform(0,1)*random.uniform(0,1))*1.35)
		
		# Random Stuff
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
			time.sleep((4.0+random.uniform(0,1)*random.uniform(0,1))*1.35)
		
		# Click where key token would be if one spawned
		if random.uniform(0,15) > 14:
			MouseClick.left_click(1881, 1890, 739, 745)
			time.sleep(random.uniform(1.1, 1.3))
		if random.uniform(0,18) > 17:
			time.sleep(random.uniform(20,30))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
