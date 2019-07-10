
import random
import time

from ZOSRS_Utils import empty_inventory

rows = input('Num Rows from bottom: ')
time.sleep(1)
empty_inventory(int(rows))
