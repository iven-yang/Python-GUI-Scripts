
import random
import time

from resources.mouse import MouseClick
from random import randint

#Face north. zoom all the way out, with camera at highest angle possible
#Play the harp from the left

runs = randint(300,315) # around 5 hours

time.sleep(2.5)

try:
	while runs>0:
		MouseClick.left_click(893, 927, 520, 546)
		time.sleep(random.uniform(45, 65))
		
		runs -= 1

except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
