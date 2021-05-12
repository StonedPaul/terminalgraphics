import time
import random
def height(n, increase, decrease):
    if n <= 1 and decrease == True:
        increase = True
        decrease = False
    elif n >= 25 and increase == True:
        increase = False
        decrease = True
    time.sleep(0.05)
    choice = random.choice('!@#$%^&*')
    if increase:
        print(n*choice)
        return height(n+1, increase, decrease)
    else:   
        print(n*choice)
        return height(n-1, increase, decrease)
height(1, True, False)