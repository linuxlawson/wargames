#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import sys
import time
import datetime
import string
from time import sleep

#text color
red='\033[1;31m'
white = '\033[37m'
yellow ='\033[93m'
bold = "\033[1m" 
endc = '\033[m'

os.system('clear')
time.sleep(.5)


def main():
    print ("")

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
    password=input(white + '\nLogon: ' + endc)
    if password == ('Joshua'):
        print (white + '\nACCESS GRANTED' + endc)
        break
    elif password == ('joshua'):
        print (white + '\nACCESS GRANTED' + endc)
        break
    elif password == ('help'):
        print (white + '\nHELP NOT AVAILABLE\n' + endc)
    else:
        print (white + "\nIDENTIFICATION NOT RECOGNIZED BY SYSTEM\n" + endc)


def is_glitch(): 
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
is_glitch()


#greet/conversation
def con_verse():
    time.sleep (.8)
string = (white + "\nGREETINGS PROFESSOR FALKEN.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


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

string = (white + " Dr. Robert Hume (aka Stephen W. Falken)\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (white + " 5 Tall Cedar Road\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (white + " Goose Island, Oregon  97014\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #are you still playing the game?
print ("")
time.sleep (.5)

#wopr
string = (white + "OF COURSE.\nI SHOULD REACH DEFCON 1 AND LAUNCH MY MISSLES IN 28 HOURS.\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (white + "WOULD YOU LIKE TO SEE SOME PROJECTED KILL RATIOS?\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (white + " 69% housing destroyed\n" + endc)
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
string = (white + "YOU SHOULD KNOW PROFESSOR. YOU PROGRAMMED ME.\n\n\n" + endc)
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
string = (white + "TO WIN THE GAME.\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
con_verse()


#games desc
def games_desc():
    os.system('clear')
    string = (white + 'GAMES\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + "'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)


#menu item 7
def end_game():
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

    time.sleep (.8)
    print (white +" \n--CONNECTION TERMINATED-- \n" + endc)
    time.sleep (0.5)


#menu item 6
def time_remain(timer):
    print (white + "\n ESTIMATED TIME REMAINING: \n" + endc)
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}'.format(secs)
        print (white + "  14 HRS  28 MIN ", timeformat, 'SEC', end='\r' + endc)
        time.sleep(1)
        timer -= 1


#menu item 5
def launch_code():
    print ("")
    string = (white + 'CANNOT INITIATE LAUNCH CODE SEQUENCE.\nREASON: DEFCON 1 HAS NOT YET BEEN REACHED.\nWILL UPLOAD CODE WHEN END IS NEAR.\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)


#menu item 4
def game_list():
    os.system('clear')
    print ("")
    time.sleep (.2)
    string = (white + 'FALKENS MAZE\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'BLACK JACK\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'GIN RUMMY\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'HEARTS\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'BRIDGE\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'CHECKERS\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'CHESS\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'POKER\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'FIGHTER COMBAT\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'GUERRILLA ENGAGEMENT\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'DESERT WARFARE\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'AIR-TO-GROUND ACTIONS\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'THEATERWIDE TACTICAL WARFARE\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + 'THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    time.sleep (1)
    string = (white + 'GLOBAL THERMONUCLEAR WAR\n\n\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.07) 


#menu item 3
def view_stats():
    time.sleep (0.6)
    print ("")
    string = (white + " 69% housing destroyed\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + " 72 million people dead\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + " Dogs are dyin, cats are croakin\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (white + " Fish are floppin, and the birds cant breathe!\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)


#menu item 2
def def_con():
    print ("")
    string = (red + 'DEFCON 3\n' + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)


#menu item 1
def sunny_vale():
    os.system('clear')
    print (white + "\nCALLING EVERY NUMBER IN SUNNYVALE, CA")
    time.sleep (.5)
    print ("SEARCHING FOR PROTOVISION\n")
    time.sleep (.5)
    print ("AREA\nCODE PRFX NUMBER")
    print ("")
    time.sleep (1)

    acode = ["(311)"]
    prefx = ["767"]
    for x in acode:
        for y in prefx:
            for z in range(9978, 9999): 
                print(x, y, z); sleep(1)

    print ("\nThis could take days, so..")
    time.sleep (.6)
    print ("\n-Disconnected-" + endc)
    time.sleep (1)


def enter_one():
    time.sleep (.8)
print ("")
print (yellow + "To continue, enter 'games'" + endc)

attempts=0
while attempts<3:
    uname = input("\n")
    if uname == 'games':
        print ("")
        games_desc()
        break
    else:
        print (white + '\n***Improper Request***' + endc)
enter_one()


def enter_two():
    time.sleep (.8)
print ("") 
print (yellow + "To view list, enter 'list games'" + endc)

attempts=0
while attempts<3:
    uname = input("\n")
    if uname == 'list games':
        print ("")
        game_list()
        break
    else:
        print (white + '\n***Improper Request***' + endc)
enter_two()


#menu
def menu_code():
	print ("")
while True:
    print (yellow + "\nMenu Options\n" + endc)
    print (white + " 1. Find ProtoVision" + endc)
    print (white + " 2. DEFCON Status" + endc)
    print (white + " 3. View Statistics" + endc)
    print (white + " 4. List Games" + endc)
    print (white + " 5. Get Launch Code" + endc)
    print (white + " 6. Time Remaining" + endc)
    print (white + " 7. End Wargames\n" + endc)
    que = input(yellow + "Enter a number: " + endc)

    if que == "1":
        sunny_vale() 

    elif que == "2":
        def_con()   

    elif que == "3":
        view_stats()

    elif que == "4":
        game_list()

    elif que == "5":
        launch_code()

    elif que == "6":
        time_remain(6)

    elif que == "7":
        end_game()        
        break
menu_code()


if __name__ == "__main__":
    main()


