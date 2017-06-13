
import random
import time

from resources.mouse import MouseClick
from resources.keyboard import Keyboard
from random import randint

#Have at least 331 of the stuff you are alching
#Have the stuff being alched under the bottom of the high alch spell

runs = 20 # 17-17.5 min

time.sleep(1)

chat_options = [
	'mining in this game is cancer',
	'lol',
	'its so stupid that mining iron and granite is the fastest way to level',
	'mining is so stupid jagex sucks at designing skills lol',
	'fu k',
	'i want to kil myself',
	'mining pisses me off',
	'this is so dumb',
	'f dis',
	'fk this sht im out',
	'i am man woman',
	'i am super cool'
]

try:
	while runs > 0:
		option = randint(0, len(chat_options)-1)
		Keyboard.chat(chat_options[option])
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
