
import random
import math
import time

from resources.mouse import MouseClick
from resources.keyboard import Keyboard
from random import randint

# Go to a world with few people
# Face north, zoomed fully out, with highest camera angle
# Stand in Dwarven Mines near Falador entrance at 3 iron stones next to the Dungeoneering entrance
'''
      o
  o   x      <- stand at the x
o
'''

runs = randint(30, 35) # 1.25-1.46 hours
# runs = randint(50, 55) # 2.08-2.29 hours

time.sleep(2.5)

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
	'i am super cool',
	'ugh',
	'kill me',
	'this is gey',
	'i hate mining',
	'kek',
	'how do ppl max mining lol',
	'time to stick my hard pickaxe in this rocks crack',
	'just keep mining just keep mining',
	'if i had 1 dollar for every iron ore ive mined i would have at least 10 dollars',
	'i like men',
	'fuk u geodude',
	'i love talking to myself',
	'im lonely'
]

try:
	while runs>0: # About 150 sec per iteration
		iron_cycles = 0
		
		# Mine irons until inv full (27)
		while iron_cycles<8: # About 15 sec per iteration
			# Bottom left iron
			MouseClick.left_click(804, 813, 582, 588)
			time.sleep(random.uniform(3.9, 4.25))
			
			# Middle iron
			MouseClick.left_click(957, 963, 489, 494)
			time.sleep(random.uniform(3.8, 4.15))
			
			# Top right iron
			MouseClick.left_click(1064, 1071, 434, 439)
			time.sleep(random.uniform(5.1, 5.45))
			
			if random.uniform(0,16)>15:
				option = randint(0, len(chat_options)-1)
				block = chat_options[option]
				
				if random.uniform(0,5) > 4:
					block = 'wave2:%s' % block
				if random.uniform(0,5) > 4:
					block = 'flash2:%s' % block
				
				Keyboard.chat(block)
				
				time.sleep(random.uniform(2,4))
			
			iron_cycles += 1
		
		# Enter dungeon to bank (you will be standing at starting location)
		MouseClick.left_click(604, 627, 730, 753)
		if random.uniform(0,14) > 13:
			time.sleep((2.0+abs(random.uniform(0,1)-random.uniform(0,1)))*random.uniform(10,13))
		else:
			time.sleep((2.0+random.uniform(0,1)*random.uniform(0,1))*5)
		
		# Click Deposit Box
		MouseClick.left_click(1005, 1017, 392, 401)
		time.sleep(random.uniform(5, 5.35))
		
		# Deposit inventory
		MouseClick.left_click(1004, 1016, 631, 641)
		time.sleep(random.uniform(1.8, 2))
		
		# Exit
		MouseClick.left_click(788, 800, 705, 709)
		if random.uniform(0,10) > 9:
			time.sleep(random.uniform(10, 15))
		else:
			time.sleep((2.0+random.uniform(0,1)*random.uniform(0,1))*4.5)
		
		# Click top right iron and re-loop
		MouseClick.left_click(1202, 1210, 304, 309)
		time.sleep(random.uniform(6.4, 6.75))
		
		runs -= 1
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
