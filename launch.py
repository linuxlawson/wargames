#!/usr/bin/env python3
#import to main (joshua.py)

import os
import time
import string
import random

os.system ('clear')

#text color
white = '\033[37m'
endc = '\033[m'
bold = "\033[1m"

def launch_code():
    time.sleep (0.5)
target = ("CPE 1704 TKS")
time.sleep (0.5)
print ("")

iscaps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
isnums = list("1234567890")
isspace = list(" ")

attemptThis = ''.join(random.choice(iscaps + isnums + isspace) for i in range(len(target)))
attemptNext = ''

completed = False
generation = 0

while completed == False:
    print(' ',bold + white + attemptThis,'\033[F' + endc)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(iscaps + isnums + isspace)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)
launch_code()


time.sleep (1)
print ("\n\n\n  Launch Code Authenticated")
time.sleep (0.8)
print ("\n  Launch Order Confirmed")
time.sleep (0.8)
print ("\n  Launch missles in T-minus " + str(generation) + " second(s)\n")
time.sleep (0.5)
print(white + '\n  -------------------------' + endc)
time.sleep (0.2)
print(white + '\n  -------------------------' + endc)
time.sleep (0.2)
print ("\n  'Turn your key, sir.'\n")
time.sleep (1)
print("")


