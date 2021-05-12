import time
import random
def bounce(tn, n, right, left):
    lenN = 5
    if right and n == tn - lenN:
        right = False
        left = True
    elif left and n <= 1:
        right = True
        left = False
    time.sleep(0.03)
    choice = random.choice('!@#$%^&*')
    if right:
        print(n*' '+ lenN*choice)
        return bounce(tn, n+1, right, left)
    elif left:
        print(n*' '+ lenN*choice)
        return bounce(tn, n-1, right, left)
bounce(55, 0, True, False)