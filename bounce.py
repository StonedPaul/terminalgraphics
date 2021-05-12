import time
import os
import random

def switch(boolean):
    if boolean:
        return False
    return True

def nextFrame(x,y,up,side,wall,row):
    amount = random.randint(1, 3)
    if x < 200 and side:
        x+= random.randint(amount, 4)
    elif x > 0 and not(side):
        x-= random.randint(amount, 4)
    else:
        side = switch(side)
        wall = True
    if y < 60 and up:
        y+= random.randint(amount, 4)
    elif y > 0 and not(up):
        y-= random.randint(amount, 4)
    else:
        up = switch(up)
        wall = True

    time.sleep(0.1)
    os.system("clear")
    if wall:
        row = 3*(random.choice('*#%'))
        wall = False
    print(int(y-1)*'\n')
    print(int(x-2)*' '+ row)
    print(int(x-2)*' '+ row)
    print(int(x-2)*' '+ row)
    nextFrame(x, y, up, side, wall, row)
nextFrame(1, 1, True, True, True, '***')