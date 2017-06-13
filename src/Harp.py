
import random
import time

from resources.mouse import MouseClick
from random import randint

# Face north. zoom all the way out, with camera at highest angle possible
# Play the harp from the left
# Leave first inventory slot empty

runs = randint(300,315) # Around 5 hours

time.sleep(2.5)

try:
	while runs>0:
		MouseClick.left_click(893, 927, 520, 546)
		time.sleep(random.uniform(45, 65))
		
		# Random stuff
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
		
		if random.uniform(0,15) > 14:
			MouseClick.left_click(1732, 1745, 739, 745)
			time.sleep(random.uniform(1.1, 1.3))
		
		runs -= 1

except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
