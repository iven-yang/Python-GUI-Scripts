
import pyautogui
import random
import time

from random import randint


class Keyboard:
	@classmethod
	def __init__(cls):
		pyautogui.PAUSE = 0
	
	@classmethod
	def push(cls, key: str):
		pyautogui.PAUSE = 0
		
		pyautogui.keyDown(key)
		time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.09)
		pyautogui.keyUp(key)
	
	@classmethod
	def chat(cls, text: str):
		pyautogui.PAUSE = 0
		
		pyautogui.keyDown('enter')
		time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.09)
		pyautogui.keyUp('enter')
		time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.03)
		
		for c in text:
			pyautogui.keyDown(c)
			time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.085)
			pyautogui.keyUp(c)
			time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.03)
		
		pyautogui.keyDown('enter')
		time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.09)
		pyautogui.keyUp('enter')
		time.sleep((0.78+random.uniform(0,1)*random.uniform(0,1))*0.03)
