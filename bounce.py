import time
import os
import random

def switch(boolean):
    if boolean:
        return False
    return True

def hitWall(string):
    if '-' in string:
        return '000'
    return '---'

def printBlock(x,y,row):
    print(int(y-1)*'\n')
    print(int(x-2)*' '+ row)
    print(int(x-2)*' '+ row)
    print(int(x-2)*' '+ row)

def nextFrame(x,y,up,side,wall,row):
    amount = random.randint(1, 3)
    if x < 204 and side:
        x+= 1
    elif x > 0 and not(side):
        x-= 1
    else:
        side = switch(side)
        wall = True
    if y < 61 and up:
        y+= 1
    elif y > 0 and not(up):
        y-= 1
    else:
        up = switch(up)
        wall = True

    time.sleep(0.01)
    os.system("clear")
    if wall:
        row = hitWall(row)
        wall = False
    printBlock(x,y,row)
    nextFrame(x, y, up, side, wall, row)
nextFrame(1, 1, True, True, True, '***')
