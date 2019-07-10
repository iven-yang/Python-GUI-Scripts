import os
import pyautogui
import random
import time

from datetime import datetime, timedelta
from resources.mouse import MouseClick

# Runescape Client must be maximized windowed

images_folder = os.path.join(os.getcwd(), 'resources', 'OSRS_images')

def empty_inventory(rows:int):
    """
    
    Note that shift click drop must be turned on in runescape settings for this to work
    
    Empties player inventory (assumes a 4 width x 7 height inventory) by n rows
    starting from bottom, with slots emptied in random order
    
    :param rows: number of rows to drop, starting from bottom row
    """
    x_coords = [1750, 1794, 1837, 1877]
    y_coords = [758, 796, 833, 870, 908, 944, 980]
    
    pyautogui.keyDown('shift')
    time.sleep(0.01)
    
    target_coords = []
    for y in range(6, 6-rows, -1):
        y = y_coords[y]
        new_row = []
        for x in x_coords:
            new_row.append((x, y))
        random.shuffle(new_row)
        target_coords.extend(new_row)
    
    for coord in target_coords:
        x = coord[0]
        y = coord[1]
        MouseClick.left_click(x-5, x+5, y-5, y+5)
        time.sleep(random.uniform(0.15, 0.6))
    
    pyautogui.keyUp('shift')

def check_logged_in():
    """
    
    Makes sure user is logged in
    """
    quest_menu_icon = pyautogui.locateOnScreen(os.path.join(images_folder, 'quest_menu_icon.png'),
                                               region=(1550, 995, 50, 50),
                                               confidence=0.9)
    if quest_menu_icon is not None:
        return True
    else:
        return False

def check_anchor(x, y, width, height, tries=3, img='anchor.png'):
    """
    
    Makes sure user does not move
    """
    if tries==0:
        return False
    quest_menu_icon = pyautogui.locateOnScreen(os.path.join(images_folder, img),
                                               region=(x, y, width, height),
                                               confidence=0.9)
    if quest_menu_icon is not None:
        return True
    else:
        time.sleep(2)
        return check_anchor(x, y, width, height, tries-1)
        
def fail_out():
    """
    
    Captures failures
    """
    failures_folder = os.path.join(os.getcwd(), 'resources', 'Failures')
    pic = pyautogui.screenshot()
    pic.save(os.path.join(failures_folder, datetime.now().strftime('%I_%M_%S') + '.png'))
    print('%s Screenshot at time of failure saved in failures folder' % datetime.now().strftime('%I:%M:%S'))
    print('%s Mouse Position at time of failure:' % datetime.now().strftime('%I:%M:%S'))
    print(pyautogui.position())
    exit(0)
