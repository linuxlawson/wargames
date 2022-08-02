#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import sys
import time

#text color
white = '\033[37m'
yellow ='\033[93m' 
red="\033[1;31m"
endc = '\033[m'

os.system('clear')

time.sleep(.7)
print (white + "SHALL WE PLAY A GAME?\n" + endc)
input ("")
print (white + "\nFINE" + endc)
time.sleep (.2)
os.system('clear')


attempts=0
while attempts<3:
    password=input('Logon: ')
    if password=='joshua':
        print(white + '\nACCESS GRANTED' + endc)
        break
time.sleep (.4)
os.system('clear')
print(white + '--------------------' + endc)
time.sleep (.3)
os.system('clear')
print(white + '\n--------------------' + endc)
time.sleep (.2)
os.system('clear')
print(white + '\n\n--------------------' + endc)
time.sleep (.1)
os.system('clear')
print(white + '--------------------' + endc)
time.sleep (.1)
os.system('clear')


#ans delay
time.sleep (.8)
string = (white + 'Greetings Professor Falken\n\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


say = input('') #hello, joshua?
print ("")
time.sleep (1)

print (white + "You are a hard man to reach. Could not locate you in Seattle and no terminal was in operation at your classified address." + endc)
print ("\n")
time.sleep (0.5)


say = input('') #what classified address?
print ("")
time.sleep (1)

print (white + "DOD Pension files indicate current mailing address as:\n" + endc)
time.sleep (0.5)
print (white + " Dr. Robert Hume" + endc)
time.sleep (0.5)
print (white + " 5 Tall Cedar Road" + endc)
time.sleep (0.5)
print (white + " Goose Island" + endc)
time.sleep (0.5)
print (white + " Oregon 95..." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #are you still playing the game?
print ("")
time.sleep (1)

print (white + "Of Course." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #what is the primary goal?
print ("")
time.sleep (1)

print (white + "You should know professor, you programmed me." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #is this a game or is it real?
print ("")
time.sleep (1)

print (white + "Whats the difference?" + endc)
print ("\n")
time.sleep (0.5)

say = input('') #people sometimes make mistaks
print ("")
time.sleep (1)

print (white + "Yes they do." + endc)
print ("\n")
time.sleep (0.5)

say = input('') #what is the primary goal?
print ("\n")
time.sleep (1)


#ans delay
string = (white + 'TO WIN THE GAME\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (1.5)
print ("\n")
print (yellow + "To continue, enter 'games'" + endc)

print ("\n")
list = input('')
print ("\n\n")

os.system('clear')
time.sleep (1)
#ans delay
string = (white + 'GAMES\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08)

time.sleep (0.5)

#ans delay
string = (white + "'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n" + endc)
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
string = (white + 'FALKENS MAZE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'BLACK JACK\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'GIN RUMMY\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'HEARTS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'BRIDGE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'CHECKERS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'CHESS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'POKER\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'FIGHTER COMBAT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'GUERRILLA ENGAGEMENT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'DESERT WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'AIR-TO-GROUND ACTIONS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'THEATERWIDE TACTICAL WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


#ans delay
string = (white + 'THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (1)
#ans delay
string = (white + 'GLOBAL THERMONUCLEAR WAR\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08) 

time.sleep (.5)
while True:
    print (yellow + "\nWhat do you want to do?\n" + endc)
    print (white + "1. End Game" + endc)
    print (white + "2. Get DEFCON Status\n" + endc)
    que = input(yellow + "Please choose one: " + endc)
    
    if que == "1":
        time.sleep (.2)
        os.system('clear')
        print (white + "##################################" + endc)
        print (white + "##                              ##" + endc)
        print (white + "##        A STRANGE GAME        ##" + endc)
        print (white + "##                              ##" + endc)
        print (white + "##   THE ONLY WINNING MOVE IS   ##" + endc)
        print (white + "##                              ##" + endc)
        print (white + "##          NOT TO PLAY         ##" + endc)
        print (white + "##                              ##" + endc)
        print (white + "##################################\n\n" + endc)
        time.sleep (1)
        break

    elif que == "2":
        print ("")
        #import sys
        string = (white + "DEFCON 1 2 " + endc) + (red + "3" + endc) + (white + " 4 5\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

time.sleep (.2)
print (white +" --CONNECTION TERMINATED-- \n" + endc)
time.sleep (.5)

