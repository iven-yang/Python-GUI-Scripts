
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
    'kek',
    'glhf'
]
"""
Requirements:
1920x1080 borderless
HUD 50
Minimap 100
Client must be medium sized (use settings or ctrl + up/down to change size)
Warwick must be fully visible by default on the champ select screen
Image resources must be in ./resources/LoL_images

Notes:
Don't alt+tab or obstruct the recall button while doing a camp (script checks for it to see if game is over)
Don't move the client window around

Known Issues:
"""

images_folder = os.path.join(os.getcwd(), 'resources', 'LoL_images')

# Save a screenshot at time of failure
def fail_out():
    failures_folder = os.path.join(os.getcwd(), 'resources', 'Failures')
    pic = pyautogui.screenshot()
    pic.save(os.path.join(failures_folder, datetime.now().strftime('%I_%M_%S') + '.png'))
    print('%s Screenshot at time of failure saved in failures folder' % datetime.now().strftime('%I:%M:%S'))
    print('%s Mouse Position at time of failure:' % datetime.now().strftime('%I:%M:%S'))
    print(pyautogui.position())
    exit(0)

def recall():
    print('%s recalling' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1235, 1245, 1023, 1036)
    time.sleep(1)
    MouseClick.left_click(1235, 1245, 1023, 1036)
    time.sleep(10)

def begin_game_shop():
    recall()
    print('%s starting items' % datetime.now().strftime('%I:%M:%S'))
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
    print('%s shopping' % datetime.now().strftime('%I:%M:%S'))
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
    print('%s doing red' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1790, 1790, 1000, 1000)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1790, 1790, 1000, 1000)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(860, 900, 450, 500)

def bluebuff(slp: int):
    print('%s doing blue' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1720, 1720, 930, 930)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1720, 1720, 930, 930)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(930, 1000, 535, 585)

def gromp(slp: int):
    print('%s doing gromp' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1693, 1693, 923, 923)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1693, 1693, 923, 923)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(740, 810, 475, 520)

def golems(slp: int):
    print('%s doing golems' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1800, 1800, 1023, 1023)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1800, 1800, 1023, 1023)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(970, 1000, 450, 490)

def wolves(slp: int):
    print('%s doing wolves' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1718, 1718, 957, 957)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1718, 1718, 957, 957)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(970, 1000, 550, 570)
    
def chickens(slp: int):
    print('%s doing chickens' % datetime.now().strftime('%I:%M:%S'))
    MouseClick.left_click(1776, 1776, 978, 978)
    time.sleep(random.uniform(0.25, 0.75))
    MouseClick.right_click(1776, 1776, 978, 978)
    time.sleep(random.uniform(0.25, 0.75))
    time.sleep(slp)
    MouseClick.right_click(790, 820, 375, 400)

def play():
    timeout = datetime.now() + timedelta(seconds=3600) # 60 min

    fishlevelups()
    redbuff(69)
    time.sleep(random.uniform(25, 30))
    fishlevelups()

    while timeout > datetime.now():
        bluebuff(27)
        if check_post_game(random.uniform(25, 30)): break # keep checking if the game has ended during the 25-30 sec you are doing blue
        fishlevelups()
        
        gromp(7)
        if check_post_game(random.uniform(23, 25)): break
        fishlevelups()
        
        golems(34)
        if check_post_game(random.uniform(39, 44)): break
        fishlevelups()
        
        wolves(28)
        if check_post_game(random.uniform(20, 25)): break
        fishlevelups()
        
        chickens(20)
        if check_post_game(random.uniform(29, 34)): break
        fishlevelups()
        
        shop()
        if check_post_game(): break
        
        redbuff(30)
        if check_post_game(random.uniform(18, 23)): break
        fishlevelups()
    else:
        print('%s game timeout (60 min co-op ai game?!)' % datetime.now().strftime('%I:%M:%S'))
        fail_out()
    print('%s Game Ended' % datetime.now().strftime('%I:%M:%S'))
    print('')

def check_post_game(check_time=3) -> bool:
    timeout = datetime.now() + timedelta(seconds=check_time)
    while timeout > datetime.now():
        pyautogui.moveTo(100, 100) # move mouse so button won't be covered
        time.sleep(1)
        recall_button = pyautogui.locateOnScreen(os.path.join(images_folder, 'recall.png'), region=(1200, 985, 100, 100), grayscale=True)
        # Also check recall button picture when dead (it's a slightly different picture)
        if recall_button is None:
            recall_button = pyautogui.locateOnScreen(os.path.join(images_folder, 'recall_dead.png'), region=(1200, 985, 100, 100), grayscale=True)
            if recall_button is None:
                recall_button = pyautogui.locateOnScreen(os.path.join(images_folder, 'recall.png'), region=(1200, 985, 100, 100), grayscale=True)
                if recall_button is None:
                    return True
    return False

def play_again():
    pyautogui.moveTo(100, 100) # move mouse so buttons won't be covered
    
    print('%s checking for skip honor button' % datetime.now().strftime('%I:%M:%S'))
    # skip honor screen
    timeout = datetime.now() + timedelta(seconds=60)
    while timeout > datetime.now():
        skip_honor_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'skip_honor.png'))
        if skip_honor_button is not None:
            print('%s clicking skip honor button' % datetime.now().strftime('%I:%M:%S'))
            time.sleep(2)
            MouseClick.left_click(skip_honor_button[0], skip_honor_button[0], skip_honor_button[1], skip_honor_button[1])
    
    print('%s checking for level up ok button' % datetime.now().strftime('%I:%M:%S'))
    # check to see if level up
    timeout = datetime.now() + timedelta(seconds=10)
    while timeout > datetime.now():
        level_up_ok_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'level_up_ok.png'))
        if level_up_ok_button is not None:
            print('%s Level Up!' % datetime.now().strftime('%I:%M:%S'))
            time.sleep(1)
            MouseClick.left_click(level_up_ok_button[0], level_up_ok_button[0], level_up_ok_button[1], level_up_ok_button[1])
    
    print('%s checking for play again button' % datetime.now().strftime('%I:%M:%S'))
    # click play again
    timeout = datetime.now() + timedelta(seconds=10)
    while timeout > datetime.now():
        play_again_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'x_left_of_play_again.png')) # Using the actual play again button seems inconsistent
        if play_again_button is not None:
            print('%s clicking play again button' % datetime.now().strftime('%I:%M:%S'))
            time.sleep(1)
            MouseClick.left_click(play_again_button[0] + 50, play_again_button[0] + 100, play_again_button[1], play_again_button[1])
            break
    else:
        print('%s could not find the play again button' % datetime.now().strftime('%I:%M:%S'))
        fail_out()

def find_match():
    print('%s finding match' % datetime.now().strftime('%I:%M:%S'))
    client_top_left = None
    
    timeout = datetime.now() + timedelta(seconds=10)
    while timeout > datetime.now():
        find_match_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'x_left_of_find_match.png')) # Using the actual find match button seems inconsistent
        if find_match_button is not None:
            time.sleep(1)
            client_top_left = (find_match_button[0] - 445, find_match_button[1] - 685)
            MouseClick.left_click(find_match_button[0] + 50, find_match_button[0] + 100, find_match_button[1], find_match_button[1])
            break
    else:
        print('%s could not find the find match button' % datetime.now().strftime('%I:%M:%S'))
        fail_out()
    
    # Queue up with queue time limit of 5 min
    timeout = datetime.now() + timedelta(seconds=300) # 5 min
    while timeout > datetime.now():
        accept_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'accept.png'), region=(client_top_left[0] + 450, client_top_left[1] + 450, 400, 300))
        if accept_button is not None:
            MouseClick.left_click(accept_button[0], accept_button[0], accept_button[1], accept_button[1])
            time.sleep(1)
            return accept_button, client_top_left # someone might decline the queue, just keep clicking in same spot
    else:
        print('%s queue timed out' % datetime.now().strftime('%I:%M:%S'))
        fail_out()
    
def champ_select(accept_button, client_top_left):
    print('%s champ select' % datetime.now().strftime('%I:%M:%S'))
    # Click Warwick
    timeout = datetime.now() + timedelta(seconds=360) # 6 min
    while timeout > datetime.now():
        ww_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'warwick.png'), region=(client_top_left[0] + 340, client_top_left[1] + 130, 600, 450))
        if ww_button is not None:
            MouseClick.left_click(ww_button[0], ww_button[0], ww_button[1], ww_button[1])
            time.sleep(2)
            MouseClick.left_click(ww_button[0], ww_button[0], ww_button[1], ww_button[1])
            time.sleep(1)
            
            lock_in = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'lock_in.png'), region=(client_top_left[0] + 530, client_top_left[1] + 550, 200, 100))
            if lock_in is None:
                print('%s could not lock in warwick' % datetime.now().strftime('%I:%M:%S'))
                break
            
            MouseClick.left_click(lock_in[0], lock_in[0], lock_in[1], lock_in[1])
            time.sleep(1)
            MouseClick.left_click(lock_in[0], lock_in[0], lock_in[1], lock_in[1])
            time.sleep(10)
            break
        else:
            MouseClick.left_click(accept_button[0], accept_button[0], accept_button[1], accept_button[1]) # someone might decline the queue, just keep clicking in same spot
    else:
        print('%s could not lock in warwick - timeout' % datetime.now().strftime('%I:%M:%S'))
        fail_out()
    
    # wait for game start - check for other people dodging
    pyautogui.moveTo(100, 100) # move mouse so accept queue button won't be covered
    timeout = datetime.now() + timedelta(seconds=600) # 10 min load time
    while timeout > datetime.now():
        recall_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'recall.png'), region=(1200, 985, 100, 100))
        if recall_button is not None:
            print('%s game start' % datetime.now().strftime('%I:%M:%S'))
            time.sleep(3)
            begin_game_shop() # buy starting items
            break
        else:
            # check for a dodge
            accept_button = pyautogui.locateCenterOnScreen(os.path.join(images_folder, 'accept.png'), region=(client_top_left[0] + 450, client_top_left[1] + 450, 400, 300))
            if accept_button is not None:
                print('%s someone dodged, accepted new game' % datetime.now().strftime('%I:%M:%S'))
                MouseClick.left_click(accept_button[0], accept_button[0], accept_button[1], accept_button[1])
                time.sleep(1)
                champ_select(accept_button, client_top_left)
                break
    else:
        print('%s loading timeout' % datetime.now().strftime('%I:%M:%S'))
        fail_out()

# --------------- MAIN ---------------
try:
    print('%s starting script' % datetime.now().strftime('%I:%M:%S'))
    timeout = datetime.now() + timedelta(seconds=36000) # 10 hours
    
    while timeout > datetime.now():
        accept_button, client_top_left = find_match()
        champ_select(accept_button, client_top_left)
        play()
        play_again()

except KeyboardInterrupt:
    print('%s Stopped by User' % datetime.now().strftime('%I:%M:%S'))

print('%s 10 hours of XP farming complete' % datetime.now().strftime('%I:%M:%S'))
