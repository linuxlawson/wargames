#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import time
import string
import random
import importlib
import target as targ
import sys

#text color
red='\033[1;31m'
white = '\033[37m'
yellow ='\033[93m' 
endc = '\033[m'

os.system('clear')
time.sleep(.7)
print (white + "\nSHALL WE PLAY A GAME?\n" + endc)
input ("")
print (white + "\nFINE" + endc)
time.sleep (.2)
os.system('clear')


#pass
attempts=0
while attempts<3:
    password=input('\nLogon: ')
    if password=='joshua':
        print (white + '\nACCESS GRANTED' + endc)
        break
    else:
        print (white + "\nIDENTIFICATION NOT RECOGNIZED BY SYSTEM\n" + endc)
        
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


#greet
time.sleep (.8)
string = (white + "\nGREETINGS PROFESSOR FALKEN\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

#ques
say = input('') #hello, joshua?
print ("")
time.sleep (1)

#answer
print (white + "YOU ARE A HARD MAN TO REACH. COULD NOT FIND \nYOU IN SEATTLE AND NO TERMINAL IS IN \nOPERATION AT YOUR CLASSIFIED ADDRESS." + endc)
print ("\n")
time.sleep (0.5)

#ques
say = input('') #what classified address?
print ("")
time.sleep (1)

#answer
print (white + "DOD PENSION FILES INDICATE CURRENT MAILING ADDRESS AS:\n" + endc)
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

#ques
say = input('') #are you still playing the game?
print ("")
time.sleep (1)

#answer
print (white + "OF COURSE.\n" + endc)
time.sleep (1)
print (white + "I SHOULD REACH DEFCON 1 AND LAUNCH MY MISSILES IN 28 HOURS.\n" + endc)
time.sleep (0.8)
print (white + "WOULD YOU LIKE TO SEE SOME PROJECTED KILL RATIOS?\n" + endc)
time.sleep (0.8)
print (white + " 69% housing destroyed\n" + endc)
time.sleep (0.5)
print (white + " 72 million people dead\n\n" + endc)
time.sleep (0.5)

#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (1)

#answer
print (white + "YOU SHOULD KNOW PROFESSOR, YOU PROGRAMMED ME." + endc)
print ("\n")
time.sleep (0.5)

#ques
say = input('') #is this a game or is it real?
print ("")
time.sleep (1)

#answer
print (white + "WHATS THE DIFFERENCE?" + endc)
print ("\n")
time.sleep (0.5)

#ques
say = input('') #people sometimes make mistaks
print ("")
time.sleep (1)

#answer
print (white + "YES THEY DO." + endc)
print ("\n")
time.sleep (0.5)

#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (1)


#answer
string = (white + "TO WIN THE GAME\n" + endc)
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
#games
string = (white + 'GAMES\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (0.5)

#games desc
string = (white + "'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


time.sleep (1)
print ("\n") 
print (yellow + "To view list, enter 'list games'" + endc)


print ("\n")
list = input('')
print ("")

os.system('clear')
time.sleep (0.8)
print ("")

#gameslist
string = (white + 'FALKENS MAZE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'BLACK JACK\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'GIN RUMMY\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'HEARTS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'BRIDGE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'CHECKERS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'CHESS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.07)


string = (white + 'POKER\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.07)


string = (white + 'FIGHTER COMBAT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'GUERRILLA ENGAGEMENT\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'DESERT WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'AIR-TO-GROUND ACTIONS\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'THEATERWIDE TACTICAL WARFARE\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)


string = (white + 'THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.06)

time.sleep (1)
string = (white + 'GLOBAL THERMONUCLEAR WAR\n\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.08) 

#menu
time.sleep (1)
while True:
    print (yellow + "\nWhat do you want to do?\n" + endc)
    print (white + "1. End Wargames" + endc)
    print (white + "2. Get DEFCON Status" + endc)
    print (white + "3. Get Launch Codes" + endc)
    print (white + "4. Review Statistics\n" + endc)
    que = input(yellow + "Enter a number: " + endc)
    
    if que == "1":
        os.system('clear')
        time.sleep (1)
        string = (white + '\nA STRANGE GAME.\n\nTHE ONLY WINNING MOVE IS\n\nNOT TO PLAY.\n\n' + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.08)

        time.sleep (1)
        break


    if que == "2":
        print ("")
        import sys
        string = (red + 'DEFCON 3\n' + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)
        
            
    if que == "3":
        time.sleep (.2)
        importlib.reload(targ) 
        time.sleep(.06)

    elif que == "4":        
        time.sleep (0.6)
        print ("")
        string = (white + " 69% housing destroyed\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

        string = (white + " 72 million people dead\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

        string = (white + " to be continued...\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

      
time.sleep (.2)
print (white +" \n--CONNECTION TERMINATED-- \n" + endc)
time.sleep (.5)

