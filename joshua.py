#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import sys
import time

#text color
twhite = '\033[37m'
yellow ='\033[93m' 
endc = '\033[m'

os.system('clear')

time.sleep(.7)
print (twhite + "SHALL WE PLAY A GAME?\n" + endc)
input ("")
print (twhite + "\nFINE" + endc)
time.sleep (.2)
os.system('clear')


attempts=0
while attempts<3:
    password=input('Logon: ')
    if password=='joshua':
        print(twhite + '\nACCESS GRANTED' + endc)
        break
time.sleep (.4)
os.system('clear')
print(twhite + '--------------------' + endc)
time.sleep (.3)
os.system('clear')
print(twhite + '\n--------------------' + endc)
time.sleep (.2)
os.system('clear')
print(twhite + '\n\n--------------------' + endc)
time.sleep (.1)
os.system('clear')
print(twhite + '--------------------' + endc)
time.sleep (.1)
os.system('clear')


#ans delay
time.sleep (.8)
string = (twhite + 'Greetings Professor Falken\n\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


say = input('') #hello, joshua?
print ("")
time.sleep (1)

print (twhite + "You are a hard man to reach. Could not locate you in Seattle and no terminal was in operation at your classified address." + endc)
print ("\n")
time.sleep (0.5)


say = input('') #what classified address?
print ("")
time.sleep (1)

print (twhite + "DOD Pension files indicate current mailing address as:\n" + endc)
time.sleep (0.5)
print (twhite + " Dr. Robert Hume" + endc)
time.sleep (0.5)
print (twhite + " 5 Tall Cedar Road" + endc)
time.sleep (0.5)
print (twhite + " Goose Island" + endc)
time.sleep (0.5)
print (twhite + " Oregon 95..." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #are you still playing the game?
print ("")
time.sleep (1)

print (twhite + "Of Course." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #what is the primary goal?
print ("")
time.sleep (1)

print (twhite + "You should know professor, you programmed me." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #is this a game or is it real?
print ("")
time.sleep (1)

print (twhite + "Whats the difference?" + endc)
print ("\n")
time.sleep (0.5)

say = input('') #people sometimes make mistaks
print ("")
time.sleep (1)

print (twhite + "Yes they do." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #what is the primary goal?
print ("\n")
time.sleep (1)


#ans delay
string = (twhite + 'TO WIN THE GAME\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (2)
print ("\n")
print (yellow + "To continue, enter 'games'" + endc)

print ("\n")
list = input('')
print ("\n\n")

os.system('clear')
time.sleep (1)
#ans delay
string = (twhite + 'GAMES\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08)

time.sleep (0.5)

#ans delay
string = (twhite + "'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

#os.system('clear')
time.sleep (1)
print ("\n") 
print (yellow + "To view list, enter 'list games'" + endc)


print ("\n")
list = input('')
print ("")

os.system('clear')
time.sleep (0.8)
print ("")

#ans delay
string = (twhite + 'FALKENS MAZE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'BLACK JACK\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'GIN RUMMY\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'HEARTS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'BRIDGE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'CHECKERS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'CHESS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'POKER\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'FIGHTER COMBAT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'GUERRILLA ENGAGEMENT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'DESERT WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'AIR-TO-GROUND ACTIONS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'THEATERWIDE TACTICAL WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (twhite + 'THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (1)
#ans delay
string = (twhite + 'GLOBAL THERMONUCLEAR WAR\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08) 


while True:
    print (yellow + "\nWhat do you want to do?\n" + endc)
    print (twhite + "1. End Game" + endc)
    print (twhite + "2. Get DEFCON Status\n" + endc)
    que = input(yellow + "Please choose one: " + endc)
    
    if que == "1":
        time.sleep (.2)
        os.system('clear')
        print (twhite + "##################################" + endc)
        print (twhite + "##                              ##" + endc)
        print (twhite + "##        A STRANGE GAME        ##" + endc)
        print (twhite + "##                              ##" + endc)
        print (twhite + "##   THE ONLY WINNING MOVE IS   ##" + endc)
        print (twhite + "##                              ##" + endc)
        print (twhite + "##          NOT TO PLAY         ##" + endc)
        print (twhite + "##                              ##" + endc)
        print (twhite + "##################################\n\n" + endc)
        time.sleep (1)
        break

    elif que == "2":
        print ("")
        #import sys
        string = (twhite + 'DEFCON 3\n' + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

time.sleep (.5)
print (twhite +" --CONNECTION TERMINATED-- \n" + endc)
time.sleep (.5)

