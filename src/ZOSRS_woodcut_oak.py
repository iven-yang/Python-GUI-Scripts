import os
import pyautogui
import random
import time

from datetime import datetime
from random import randint
from resources.mouse import MouseClick
from ZOSRS_Utils import empty_inventory, check_logged_in, fail_out, check_anchor


# Stand with ores below and right of you
# Camera zoomed in all the way with max vertical angle, facing north
# Ideally have an empty inventory, or keep items you don't want to drop in rows at top
# About 24 sec per run

# Set Anchor on screen before run (Makes sure script stops if you move unexpectedly),
# Use MousePosition.py to figure out region on screen to search for anchor
# a box with x, y at top left corner: check_anchor(x, y, width, height)
# save as anchor.png in resources/osrs_images

start = datetime.now()
duration = timedelta(seconds=randint(7200, 9000)) # About 2-2.5 hours

time.sleep(2.5)
print('Start Time:', start)

inv_rows_empty = 7  # available rows in inventory
images_folder = os.path.join(os.getcwd(), 'resources', 'OSRS_images')

anchor_img = 'minimap_tree.png'
if not check_anchor(1750, 25, 160, 160, img=anchor_img):
    raise Exception('Cannot find anchor')
try:
    invs = 0
    while start + duration > datetime.now():
        if randint(1, 20) == 1:
            time.sleep(random.uniform(60, 120))
        MouseClick.left_click(920, 1020, 200, 250)
        time.sleep(random.uniform(10, 20))
        
        last_inv_slot_empty = pyautogui.locateOnScreen(os.path.join(images_folder, 'empty_inv_slot.png'),
                                                 region=(1879, 962, 26, 26),
                                                 confidence=0.9)
        if last_inv_slot_empty is None:
            empty_inventory(inv_rows_empty)
            time.sleep(random.uniform(0.5, 5))
            invs += 1
            
        if not check_logged_in():
            raise Exception('Client Logged Out')
        if not check_anchor(1750, 25, 160, 160, img=anchor_img):
            raise Exception('Cannot find anchor')
except KeyboardInterrupt:
    print('Stopped by user\n')
except Exception as e:
    print(e)
    fail_out()
finally:
    print('Inventories of logs cut: ', invs)
    print('End Time: ', datetime.now())
    print('Elapsed: ', datetime.now() - start)
print('Script Execution Complete')
