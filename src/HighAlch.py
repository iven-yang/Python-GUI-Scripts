
import random
import time

from resources.mouse import MouseClick
from random import randint

#Have at least 331 of the stuff you are alching
#Have the stuff being alched under the bottom of the high alch spell

runs = randint(715,740) # 17-17.5 min

time.sleep(2.5)

try:
	while runs>0: # about 1.4 sec per iteration
		MouseClick.left_click(1732, 1743, 836, 842)
		time.sleep(random.uniform(1.113, 1.424))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
