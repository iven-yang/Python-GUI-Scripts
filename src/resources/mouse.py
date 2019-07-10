
import pyautogui
import random
import time

from random import randint


class MouseClick:
    @classmethod
    def __init__(cls):
        pyautogui.PAUSE = 0.01
    
    @classmethod
    def random_left_click(cls, x: int, y: int, dx: int = 5, dy: int = 5):
        cls.left_click(x-dx, x+dx, y-dy, y+dy)
    
    @classmethod
    def random_right_click(cls, x: int, y: int, dx: int = 5, dy: int = 5):
        cls.right_click(x-dx, x+dx, y-dy, y+dy)
    
    @classmethod
    def left_click(cls, x1: int, x2: int, y1: int, y2: int):
        pyautogui.PAUSE = 0
        mousex = randint(x1, x2)
        mousey = randint(y1, y2)
        pyautogui.moveTo(mousex, mousey)
        time.sleep((10+random.uniform(0, 1)*random.uniform(0, 1))*0.0045)
        
        pyautogui.mouseDown()
        time.sleep((1+random.uniform(0, 1)*random.uniform(0, 1))*0.075)
        pyautogui.mouseUp()

    @classmethod
    def right_click(cls, x1: int, x2: int, y1: int, y2: int):
        pyautogui.PAUSE = 0
        mousex = randint(x1, x2)
        mousey = randint(y1, y2)
        pyautogui.moveTo(mousex, mousey)
        time.sleep((10+random.uniform(0, 1)*random.uniform(0, 1))*0.0045)
        
        pyautogui.mouseDown(button='right')
        time.sleep((1+random.uniform(0, 1)*random.uniform(0, 1))*0.075)
        pyautogui.mouseUp(button='right')
    
    @classmethod
    def shift_click(cls, x1: int, x2: int, y1: int, y2: int):
        pyautogui.PAUSE = 0
        pyautogui.keyDown('shift')
        time.sleep(0.01)
        cls.left_click(x1, x2, y1, y2)
        pyautogui.keyUp('shift')
        time.sleep(0.02)
