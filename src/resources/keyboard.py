
import pyautogui
import random
import time

from random import randint


class Keyboard:
	@classmethod
	def __init__(cls):
		pyautogui.PAUSE = 0.01
		
	@classmethod
	def chat(cls, text: str):
		for c in text:
			print(c, end = '   ')
			sleeptime = (0.78+random.uniform(0,1)*random.uniform(0,1))*0.1
			print(sleeptime)
			time.sleep(sleeptime)
		print('\n')
