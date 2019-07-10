import os
import pyautogui
import random
import time

from datetime import datetime, timedelta
from random import randint
from resources.mouse import MouseClick
from ZOSRS_Utils import empty_inventory, check_logged_in, fail_out, check_anchor


# Stand with ores below and right of you
# Camera zoomed in all the way with max vertical angle, facing north
# Ideally have an empty inventory, or keep items you don't want to drop in rows at top
# About 3 min per run

# Set Anchor on screen before run (Makes sure script stops if you move unexpectedly),
# Use MousePosition.py to figure out region on screen to search for anchor
# a box with x, y at top left corner: check_anchor(x, y, width, height)
# save as anchor.png in resources/osrs_images

# TODO: Use datetime instead of run #

start = datetime.now()
duration = timedelta(seconds=randint(7200, 9000)) # About 2-2.5 hours

time.sleep(2.5)
print('Start Time:', start)

inv_rows_empty = 7  # available rows in inventory
images_folder = os.path.join(os.getcwd(), 'resources', 'OSRS_images')

if not check_anchor(100, 40, 55, 55):
    raise Exception('Cannot find anchor')
try:
    invs = 0
    while start + duration > datetime.now():
        for _ in range(28):
            if randint(1, 20) == 1:
                time.sleep(random.uniform(4, 20))
            MouseClick.left_click(935, 1025, 820, 900)
            time.sleep(random.uniform(3, 4))
            MouseClick.left_click(1200, 1270, 600, 680)
            time.sleep(random.uniform(3, 4))
            
            last_inv_slot_empty = pyautogui.locateOnScreen(os.path.join(images_folder, 'empty_inv_slot.png'),
                                                     region=(1879, 962, 26, 26),
                                                     confidence=0.9)
            if last_inv_slot_empty is None:
                break
                
            if not check_logged_in():
                raise Exception('Client Logged Out')
            if not check_anchor(100, 40, 55, 55):
                raise Exception('Cannot find anchor')
        empty_inventory(inv_rows_empty)
        invs += 1
        time.sleep(random.uniform(0.5, 5))
except KeyboardInterrupt:
    print('Stopped by user\n')
except Exception as e:
    print(e)
    fail_out()
finally:
    print('Inventories of ore mined: ', invs)
    print('End Time: ', datetime.now())
    print('Elapsed: ', datetime.now() - start)
print('Script Execution Complete')
