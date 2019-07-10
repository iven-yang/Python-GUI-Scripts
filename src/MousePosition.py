
import pyautogui
import time
import os

try:
	while True:
		os.system('cls')
		print(pyautogui.position())
		time.sleep(0.025)
		
		
except KeyboardInterrupt:
	print('Stopped, %s runs left\n' % runs)
print('Script Execution Complete')
