
import random
import math
import time
import pyautogui
import os

from resources.mouse import MouseClick
from resources.keyboard import Keyboard
from random import randint
from datetime import datetime, timedelta

time.sleep(2.5)

chat_options = [
    'lol',
    'ugh',
    'kek'
]
"""
1920x1080 borderless
HUD 50
Minimap 100
"""

images_folder = r'C:\Users\risin\Desktop\DefNotBottin\Python-GUI-Scripts\src\resources\LoL_images'

def recall():
    print('recalling')
    MouseClick.left_click(1235, 1245, 1023, 1036)
    time.sleep(1)
    MouseClick.left_click(1235, 1245, 1023, 1036)
    time.sleep(10)

def begin_game_shop():
    recall()
    print('starting items')
    # open shop
    MouseClick.left_click(825, 925, 175, 250)
    time.sleep(random.uniform(0.75, 1.0))
    
    # hp regen bead
    MouseClick.right_click(650, 725, 255, 280)
    time.sleep(random.uniform(0.75, 1.0))
    
    # machete
    MouseClick.right_click(435, 500, 255, 280)
    time.sleep(random.uniform(0.75, 1.0))
    
    # exit shop
    MouseClick.left_click(1570, 1585, 80, 95)
    time.sleep(random.uniform(0.75, 1.0))
    
def shop():
    recall()
    print('shopping')
    # open shop
    MouseClick.left_click(825, 925, 175, 250)
    time.sleep(random.uniform(0.75, 1.0))
    
    # stalker's blade
    MouseClick.right_click(850, 950, 390, 425)
    time.sleep(random.uniform(0.75, 1.0))
    
    # boots
    MouseClick.right_click(625, 725, 390, 425)
    time.sleep(random.uniform(0.75, 1.0))
    
    # cinderhulk
    MouseClick.right_click(390, 490, 530, 565)
    time.sleep(random.uniform(0.75, 1.0))
    
    # botrk
    MouseClick.right_click(850, 950, 675, 720)
    time.sleep(random.uniform(0.75, 1.0))
    
    # wit's end
    MouseClick.right_click(390, 490, 675, 720)
    time.sleep(random.uniform(0.75, 1.0))
    
    # exit shop
    MouseClick.left_click(1570, 1585, 80, 95)
    time.sleep(random.uniform(0.75, 1.0))

def fishlevelups():
    MouseClick.left_click(950, 960, 940, 955)
    time.sleep(random.uniform(0.5, 0.75))
    MouseClick.left_click(780, 795, 940, 955)
    time.sleep(random.uniform(0.5, 0.75))
    MouseClick.left_click(840, 860, 940, 955)
    time.sleep(random.uniform(0.5, 0.75))
    MouseClick.left_click(895, 915, 940, 955)
    time.sleep(random.uniform(0.5, 0.75))
    
def redbuff(slp: int):
    print('doing red')
    MouseClick.left_click(1790, 1790, 1000, 1000)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1790, 1790, 1000, 1000)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(860, 900, 450, 500)

def bluebuff(slp: int):
    print('doing blue')
    MouseClick.left_click(1720, 1720, 930, 930)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1720, 1720, 930, 930)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(930, 1000, 535, 585)

def gromp(slp: int):
    print('doing gromp')
    MouseClick.left_click(1693, 1693, 923, 923)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1693, 1693, 923, 923)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(740, 810, 475, 520)

def golems(slp: int):
    print('doing golems')
    MouseClick.left_click(1800, 1800, 1023, 1023)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1800, 1800, 1023, 1023)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(970, 1000, 450, 490)

def wolves(slp: int):
    print('doing wolves')
    MouseClick.left_click(1718, 1718, 957, 957)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1718, 1718, 957, 957)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(970, 1000, 550, 570)
    
def chickens(slp: int):
    print('doing chickens')
    MouseClick.left_click(1776, 1776, 978, 978)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1776, 1776, 978, 978)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(790, 820, 375, 400)

def play():
    # wait for game start
    # buy starting items
    timeout = datetime.now() + timedelta(seconds=600) # 10 min load time
    while timeout > datetime.now():
        recall_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'recall.png'))
        if recall_button is not None:
            print('game start')
            time.sleep(3)
            begin_game_shop()
            break
    else:
        print('loading timeout')
        exit(0)
    
    timeout = datetime.now() + timedelta(seconds=3600) # 60 min

    fishlevelups()
    redbuff(70)
    time.sleep(random.uniform(30, 35))
    fishlevelups()

    while timeout > datetime.now():
        bluebuff(35)
        time.sleep(random.uniform(30, 35))
        fishlevelups()
        if check_post_game():
            break
        
        gromp(10)
        time.sleep(random.uniform(30, 35))
        fishlevelups()
        if check_post_game():
            break
        
        golems(40)
        time.sleep(random.uniform(55, 60))
        fishlevelups()
        if check_post_game():
            break
        
        wolves(31)
        time.sleep(random.uniform(27, 32))
        fishlevelups()
        if check_post_game():
            break
        
        chickens(25)
        time.sleep(random.uniform(31, 36))
        fishlevelups()
        if check_post_game():
            break
        
        shop()
        time.sleep(random.uniform(15, 20))
        if check_post_game():
            break
        
        redbuff(35)
        time.sleep(random.uniform(25, 30))
        fishlevelups()
        if check_post_game():
            break
    else:
        print('game timeout (60 min co-op ai game?!)')
        exit(0)
    print('Game Ended')
    print('')

def check_post_game() -> bool:
    skip_honor_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'skip_honor.png'))
    play_again_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'x_left_of_play_again.png')) # Using the actual play again button seems inconsistent
    if skip_honor_button is not None:
        time.sleep(1)
        MouseClick.left_click(skip_honor_button[0], skip_honor_button[0], skip_honor_button[1], skip_honor_button[1])
        return True
    if play_again_button is not None:
        return True
    return False

def play_again():
    # check for level up ok button
    pyautogui.moveTo(10, 10) # move mouse so level up ok button won't be covered
    time.sleep(3)
    level_up_ok_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'level_up_ok.png'))
    if level_up_ok_button is not None:
        MouseClick.left_click(level_up_ok_button[0], level_up_ok_button[0], level_up_ok_button[1], level_up_ok_button[1])
        time.sleep(2)
    
    # click play again
    timeout = datetime.now() + timedelta(seconds=30)
    while timeout > datetime.now():
        play_again_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'x_left_of_play_again.png')) # Using the actual play again button seems inconsistent
        if play_again_button is not None:
            time.sleep(1)
            MouseClick.left_click(play_again_button[0] + 50, play_again_button[0] + 100, play_again_button[1], play_again_button[1])
            time.sleep(5)
            break
    else:
        print('could not find the play again button')
        exit(0)

def find_match():
    print('finding match')
    
    timeout = datetime.now() + timedelta(seconds=10)
    while timeout > datetime.now():
        find_match_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'x_left_of_find_match.png')) # Using the actual find match button seems inconsistent
        if find_match_button is not None:
            MouseClick.left_click(find_match_button[0] + 50, find_match_button[0] + 100, find_match_button[1], find_match_button[1])
            break
    else:
        print('could not find the find match button')
        exit(0)
    
    # Queue up with queue time limit of 5 min
    timeout = datetime.now() + timedelta(seconds=300) # 5 min
    while timeout > datetime.now():
        accept_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'accept.png'))
        if accept_button is not None:
            time.sleep(0.5)
            MouseClick.left_click(accept_button[0], accept_button[0], accept_button[1], accept_button[1])
            time.sleep(1)
            return accept_button # someone might decline the queue, just keep clicking in same spot
    else:
        print('queue timed out')
        exit(0)
    
def champ_select(accept_button):
    print('champ select')
    # Click Warwick
    timeout = datetime.now() + timedelta(seconds=30)
    while timeout > datetime.now():
        ww_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'warwick.png'))
        if ww_button is not None:
            MouseClick.left_click(ww_button[0], ww_button[0], ww_button[1], ww_button[1])
            time.sleep(2)
            MouseClick.left_click(ww_button[0], ww_button[0], ww_button[1], ww_button[1])
            time.sleep(1)
            
            lock_in = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'lock_in.png'))
            if lock_in is None:
                print('could not lock in warwick')
                exit(0)
            
            MouseClick.left_click(lock_in[0], lock_in[0], lock_in[1], lock_in[1])
            time.sleep(1)
            MouseClick.left_click(lock_in[0], lock_in[0], lock_in[1], lock_in[1])
            time.sleep(10)
            break
        else:
            MouseClick.left_click(accept_button[0], accept_button[0], accept_button[1], accept_button[1]) # someone might decline the queue, just keep clicking in same spot
    else:
        print('could not lock in warwick - timeout')
        exit(0)

try:
    print('starting script')
    timeout = datetime.now() + timedelta(seconds=36000) # 10 hours
    
    while timeout > datetime.now():
        accept_button = find_match()
        champ_select(accept_button)
        play()
        play_again()

except KeyboardInterrupt:
    print('Stopped')

print('10 hours of XP farming complete')
