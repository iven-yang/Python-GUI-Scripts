
import random
import time

from resources.mouse import MouseClick
from random import randint

#Face north, be zoomed all the way in, with camera from highest angle
#Chop the ivy from the left of the wall (bottom right of varrock castle is a good place)

runs = randint(225,250) # 3.91-4.35 hours

time.sleep(2.5)

try:
	while runs>0: # about 62.7 seconds per iteration
		MouseClick.left_click(1015, 1025, 510, 535)
		
		time.sleep(random.uniform(40, 60))
		
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
		
		runs -= 1

except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
