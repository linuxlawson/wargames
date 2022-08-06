#!/usr/bin/env python3
#target to main (joshua)

import os
import string
import random
import time
os.system ('clear')

#text color
red = '\033[1;31m'
white = '\033[37m'
yellow ='\033[93m' 
endc = '\033[m'
bold = "\033[1m"


results = string.ascii_uppercase + string.digits + ' '

time.sleep (0.5)
#print ("Launch Code scan in progress")
target = ("CPE 1704 TKS")
time.sleep (0.5)
print ("")

attemptThis = ''.join(random.choice(results) for i in range(len(target)))
attemptNext = ''

completed = False
generation = 0

while completed == False:
    print(' ', white +  attemptThis,'\033[F' + endc)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(results)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

time.sleep (1)
print ("\n\n\n  " + attemptThis + " [Sys Check]")
time.sleep (1)
print ("\n  Launch Code: [Authentic]")
time.sleep (1)
print ("\n  Launch Order [Confirmed]")
time.sleep (1)
print ("\n  Launch missles in T-minus " + str(generation) + " second(s)\n")
time.sleep (1)
print(white + '\n   -------------------------' + endc)
time.sleep (.2)
print(white + '\n   -------------------------' + endc)
time.sleep (.1)
print ("\n  Turn your key, sir.\n")
time.sleep (.8)
print("")
