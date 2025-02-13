import pyautogui as pag
import random
import time
from datetime import datetime

# Get the current local time
start_time_local = datetime.now()

print("Start Time (Local): ", start_time_local.strftime('%Y-%m-%d %H:%M:%S'))

counter = 0

while True:
    counter+=1
    x=random.randint(1000, 1900)
    y=random.randint(1, 900)
    pag.moveTo(x, y)

    var = random.randint(5, 60)
    print(f"{counter}: Moving cursor to X-Axis: {x}, Y-Axis: {y}, sleeps for: {var}s")
    
    time.sleep(var)
        