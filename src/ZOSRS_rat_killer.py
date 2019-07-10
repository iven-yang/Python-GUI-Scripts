import os
import pyautogui
import random
import time

from datetime import datetime, timedelta
from random import randint
from resources.mouse import MouseClick
from ZOSRS_Utils import empty_inventory, check_logged_in, fail_out, check_anchor


# Stand with swamp shack on minimap
# Middle of lumbridge swamp with the map link icon on it on world map

# Camera zoomed out midway (doesnt have to be perfect) with max vertical angle, facing north (click on compass)
# Have food matching food.png in inventory if low def/armor

start = datetime.now()
duration = timedelta(seconds=randint(9000, 10800))  # 2.5-3 hours

print('Start Time:', start)

time.sleep(2.5)

inv_rows_empty = 7  # available rows in inventory
images_folder = os.path.join(os.getcwd(), 'resources', 'OSRS_images')

def find_enemy():
    found = False
    timeout = datetime.now() + timedelta(seconds=120)
    while not found:
        time.sleep(random.uniform(0, 1))
        rats = list(pyautogui.locateAllOnScreen(os.path.join(images_folder, 'rat1.png'),
                                                region=(350, 400, 1250, 600),
                                                confidence=0.9))
        for rat in ['rat2.png']:
            rats.extend(list(pyautogui.locateAllOnScreen(os.path.join(images_folder, rat),
                                                         region=(350, 400, 1250, 600),
                                                         confidence=0.9)))
        print('Possible enemies found: ', len(rats))
        
        if len(rats) != 0:
            random.shuffle(rats)
            
            rat = rats[0]  # Pick one potential rat randomly
            MouseClick.random_right_click(rat[0], rat[1])
            attack = pyautogui.locateOnScreen(os.path.join(images_folder, 'attack.png'),
                                              region=(rat[0]-200, rat[1]+5, 200, 200))
            if attack is not None:
                found = True
                print('Enemy found!')
                time.sleep(random.uniform(0.2, 0.4))
                MouseClick.random_left_click(attack[0]+50, attack[1]+4, dx=15, dy=2)
            
        time.sleep(random.uniform(0.3, 0.5))
        if datetime.now() > timeout:
            raise TimeoutError('Timed out while finding enemy')

def walk_to_shack():
    timeout = datetime.now() + timedelta(seconds=30)
    while timeout > datetime.now():
        shack = pyautogui.locateOnScreen(os.path.join(images_folder, 'swamp_shack.png'),
                                         region=(1775, 35, 140, 150),
                                         confidence=0.99)
        print(shack)
        if shack is not None:
            MouseClick.random_left_click(shack[0]-7, shack[1]+22, dx=2, dy=2)
            return
    else:
        raise Exception('Unable to find swamp shack')

def eat_food():
    food = pyautogui.locateOnScreen(os.path.join(images_folder, 'food.png'),
                                    region=(1720, 730, 190, 270),
                                    confidence=0.99)
    if food is None:
        raise Exception('Out of food')
    MouseClick.random_left_click(food[0], food[1], dx=3, dy=3)
    print('Eating Food')
    
def check_hp():
    hp = pyautogui.locateOnScreen(os.path.join(images_folder, 'hp.png'),
                                  region=(1737, 85, 3, 3),
                                  confidence=0.99)
    while hp is None:
        print('HP too low!')
        eat_food()
        time.sleep(random.uniform(1.5, 2))

try:
    kills = 0
    while start + duration > datetime.now():
        if not check_logged_in():
            raise Exception('Client Logged Out')
        walk_to_shack()
        time.sleep(random.uniform(3, 4))
        find_enemy()
        time.sleep(random.uniform(8, 10))
        check_hp()
        time.sleep(random.uniform(0.4, 1))
        if randint(1, 25) == 1:
            time.sleep(random.uniform(25, 40))
        
        kills += 1
except KeyboardInterrupt:
    print('Stopped by user')
except Exception as e:
    print(e)
    fail_out()
finally:
    print('%s enemies killed\n' % kills)
    print('End Time: ', datetime.now())
    print('Elapsed: ', datetime.now() - start)
print('Script Execution Complete')
