#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import sys
import time
import string
import random
import importlib

try:
    import target as targ
except ImportError:
    print("Cannot import target module. Failure to launch.")


#text color
red='\033[1;31m'
white = '\033[37m'
yellow ='\033[93m' 
endc = '\033[m'

os.system('clear')
time.sleep(.5)

string = (white + "\nSHALL WE PLAY A GAME?\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

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
string = (white + "\nGREETINGS PROFESSOR FALKEN.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #hello, joshua?
print ("")
time.sleep (.5)

#wopr
string = (white + "YOU ARE A HARD MAN TO REACH. COULD NOT FIND \nYOU IN SEATTLE AND NO TERMINAL IS IN \nOPERATION AT YOUR CLASSIFIED ADDRESS.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what classified address?
print ("")
time.sleep (.5)

#wopr
string = (white + "DOD PENSION FILES INDICATE \nCURRENT MAILING AS:\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (white + " DR. ROBERT HUME (A.K.A. STEPHEN W. FALKEN)\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)
    
string = (white + " 5 TALL CEDAR ROAD\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (white + " GOOSE ISLAND, OREGON  97014\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)
    

#ques
say = input('') #are you still playing the game?
print ("")
time.sleep (.5)

#wopr
string = (white + "OF COURSE. I SHOULD REACH DEFCON 1 AND LAUNCH MY MISSLES IN 28 HOURS.\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (white + "WOULD YOU LIKE TO SEE SOME PROJECTED KILL RATIOS?\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (white + " 69% housing destroyed\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)
    
string = (white + " 72 million people dead\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (.5)

#wopr
string = (white + "YOU SHOULD KNOW PROFESSOR, YOU PROGRAMMED ME.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #is this a game or is it real?
print ("")
time.sleep (.5)

#wopr
string = (white + "WHATS THE DIFFERENCE?\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #people sometimes make mistaks
print ("")
time.sleep (.5)

#wopr
string = (white + "YES THEY DO.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (1)

#wopr
string = (white + "TO WIN THE GAME\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


time.sleep (1)
print ("\n")
print (yellow + "To continue, enter 'games'" + endc)

print ("\n")
attempts=0
while attempts<3:
    word=input('')
    if word=='games':
        print ("")
        break
    else:
        print (white + "\n***Improper Request***\n" + endc)

os.system('clear')
time.sleep (.5)

#games
string = (white + 'GAMES\n' + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

#time.sleep (0.5)

#games desc
string = (white + "'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


time.sleep (1)
print ("\n") 
print (yellow + "To view list, enter 'list games'" + endc)

print ("\n")
attempts=0
while attempts<3:
    word=input('')
    if word=='list games':
        print ("")
        break
    else:
        print (white + "\n***Improper Request***\n" + endc)


os.system('clear')
time.sleep (0.8)
print ("")


#gameslist
def game_list():  
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
    string = (white + 'GLOBAL THERMONUCLEAR WAR\n\n\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.08) 
game_list()

#menu
time.sleep (1)
while True:
    print (yellow + "\nWhat do you want to do?\n" + endc)
    print (white + " 1. End Wargames" + endc)
    print (white + " 2. Get DEFCON Status" + endc)
    print (white + " 3. Get Launch Codes" + endc)
    print (white + " 4. Review Statistics" + endc)
    print (white + " 5. List Games\n" + endc)
    que = input(yellow + "Enter a number: " + endc)
    

    if que == "1":
        os.system('clear')
        time.sleep (1)
        string = (white + '\nA STRANGE GAME.\n' + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.08)

        string = (white + '\nTHE ONLY WINNING MOVE IS\n' + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.08)

        string = (white + '\nNOT TO PLAY.\n\n' + endc)
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

    if que == "4":        
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

        string = (white + " dogs are dyin, cats are croakin\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

        string = (white + " fish are floppin, and the birds cant breathe!\n" + endc)
        for char in string:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(.06)

    elif que == "5":
        os.system('clear')
        print ("")
        time.sleep (.2)
        game_list()
        time.sleep(.06)
      
time.sleep (.5)
print (white +" \n--CONNECTION TERMINATED-- \n\n" + endc)
time.sleep (.5)

