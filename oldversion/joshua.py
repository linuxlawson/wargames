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
string = (f"{white}\nSHALL WE PLAY A GAME?\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

input ("")

print (f"{white}\nFINE{endc}")
time.sleep (.2)
os.system('clear')


#pass
attempts=0
while attempts<3:
    password=input(f"{white}\nLOGON: {endc}")
    if password in ['Joshua', 'joshua']:
        #print (f"{white}\nACCESS GRANTED{endc}")
        break
    elif password == ('help'):
        print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
    else:
        print (f"{white}\nIDENTIFICATION NOT RECOGNIZED BY SYSTEM\n{endc}")


def is_glitch(): 
    time.sleep (.4)
    os.system('clear')
    print(f"{white}-------------------------{endc}")
    time.sleep (.3)
    os.system('clear')
    print(f"{white}\n-------------------------{endc}")
    time.sleep (.2)
    os.system('clear')
    print(f"{white}\n\n-------------------------{endc}")
    time.sleep (.1)
    os.system('clear')
    print(f"{white}-------------------------{endc}")
    time.sleep (.1)
    os.system('clear')
is_glitch()


#greet/conversation
def con_verse():
    time.sleep (.8)
string = (f"{white}\nGREETINGS PROFESSOR FALKEN.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #hello, joshua?
time.sleep (.5)

#wopr
string = (f"{white}\nYOU ARE A HARD MAN TO REACH. COULD NOT FIND \nYOU IN SEATTLE AND NO TERMINAL IS IN \nOPERATION AT YOUR CLASSIFIED ADDRESS.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what classified address?
time.sleep (.5)

#wopr
string = (f"{white}\nDOD PENSION FILES INDICATE \nCURRENT MAILING AS:\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (f"{white} Dr. Robert Hume (aka Stephen W. Falken)\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (f"{white} 5 Tall Cedar Road\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (f"{white} Goose Island, Oregon  97014\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #are you still playing the game?
time.sleep (.5)

#wopr
string = (f"{white}\nOF COURSE. I SHOULD REACH DEFCON 1 AND\nLAUNCH MY MISSLES IN 28 HOURS.\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (f"{white}WOULD YOU LIKE TO SEE SOME PROJECTED KILL RATIOS?\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

string = (f"{white} 69% housing destroyed\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)

string = (f"{white} 72  million people dead\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #what is the primary goal?
time.sleep (.5)

#wopr
string = (f"{white}\nYOU SHOULD KNOW PROFESSOR. YOU PROGRAMMED ME.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #is this a game or is it real?
time.sleep (.5)

#wopr
string = (f"{white}\nWHATS THE DIFFERENCE?\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #people sometimes make mistaks
time.sleep (.5)

#wopr
string = (f"{white}\nYES THEY DO.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what is the primary goal?
time.sleep (1)

#wopr
string = (f"{white}\nTO WIN THE GAME.\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
con_verse()


#games desc
def games_desc():
    os.system('clear')
    string = (f"{white}GAMES\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}'GAMES' REFERS TO MODELS, SIMULATIONS, AND GAMES\n WHICH HAVE TACTICAL, AND STRATEGIC APPLICATIONS.\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)


#menu item 7
def end_game():
    os.system('clear')
    time.sleep (1)
    string = (f"{white}\nA STRANGE GAME.\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.08)

    string = (f"{white}\nTHE ONLY WINNING MOVE IS\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.08)

    string = (f"{white}\nNOT TO PLAY.\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.08)

    time.sleep (.8)
    print (f"{white} \n--CONNECTION TERMINATED-- \n{endc}")
    time.sleep (0.5)


#menu item 6
def time_remain(timer):
    print (f"{white}\n ESTIMATED TIME REMAINING: \n{endc}")
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}'.format(secs)
        print (white + " 14 HRS  28 MIN ", timeformat, 'SEC', end='\r' + endc)
        time.sleep(1)
        timer -= 1


#menu item 5
def launch_code():
    string = (f"{white}\nCANNOT INITIATE LAUNCH CODE SEQUENCE.\nREASON: DEFCON 1 HAS NOT YET BEEN REACHED.\nWILL UPLOAD CODE WHEN END IS NEAR.\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)


#menu item 4
def game_list():
    os.system('clear')
    time.sleep (.2)
    string = (f"{white}\nFALKENS MAZE\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}BLACK JACK\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}GIN RUMMY\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}HEARTS\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}BRIDGE\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}CHECKERS\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}CHESS\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}POKER\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}FIGHTER COMBAT\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}GUERRILLA ENGAGEMENT\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}DESERT WARFARE\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}AIR-TO-GROUND ACTIONS\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}THEATERWIDE TACTICAL WARFARE\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white}THEATERWIDE BIOTOXIC AND CHEMICAL WARFARE\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    time.sleep (1)
    string = (f"{white}GLOBAL THERMONUCLEAR WAR\n\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.07) 


#menu item 3
def view_stats():
    time.sleep (0.6)
    print ("")
    string = (f"{white} PROJECTED KILL RATIOS:\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.05)

    string = (f"{white} UNITED STATES\n UNITS DESTROYED     MILITARY FORCES\n" 
                  "\n       68%           BOMBERS\n" 
                    "       54%           ICBM'S\n"
                    "       12%           ATTACK SUBS\n"
                    "       39%           TACTICAL ARICRAFT\n"
                    "       58%           GROUND FORCES\n\n\n")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)


    string = (f"{white} UNITED STATES\n UNITS DESTROYED     CIVILIAN ASSETS\n"
                  "\n       69%           HOUSING\n" 
                    "       22%           TRANSPORTATION\n"
                    "       70%           COMMUNICATIONS\n"
                    "       45%           FOOD STOCKPILES\n"
                    "       89%           HOSPITALS\n\n\n")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)


    string = (f"{white} UNITED STATES       HUMAN RESOURCES\n"
                  "\n 49 MILLION          NON-FATAL INJURED\n" 
                    " 72 MILLION          POPULATION DEATHS\n\n\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)
    

#menu item 2
def def_con():
    string = (f"{red}\nDEFCON 3\n{endc}")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.06)


#menu item 1
def proto_vision():
    os.system('clear')
    print (f"{white}\nSCANNING FOR CARRIER TONES IN SUNNYVALE, CA{endc}")
    time.sleep (.5)
    print (f"{white}SEARCHING FOR PROTOVISION\n{endc}")
    time.sleep (.5)
    print (f"{white}AREA\nCODE PRFX NUMBER")
    print ("")
    time.sleep (1)

    acode = ["(311)"]
    prefx = ["767"]
    for x in acode:
        for y in prefx:
            for z in range(9978, 9999): 
                print(x, y, z); sleep(1)

    print (f"{white}\nThis could take days, so..{endc}")
    time.sleep (.6)
    print (f"{white}\n-Disconnected-{endc}")
    time.sleep (1)


def enter_one():
    time.sleep (.8)
print (f"{yellow}\nTo continue, enter 'games'{endc}")

attempts=0
while attempts<3:
    uname = input("\n")
    if uname == 'games':
        games_desc()
        break
    else:
        print (f"{white}\n***Improper Request***{endc}")
enter_one()


def enter_two():
    time.sleep (.8)
print (f"{yellow}\nTo view list, enter 'list games'{endc}")

attempts=0
while attempts<3:
    uname = input("\n")
    if uname == 'list games':
        game_list()
        break
    else:
        print (f"{white}\n***Improper Request***{endc}")
enter_two()


#menu
def menu_code():
	print ("")
while True:
    print (f"{yellow}\nMenu Options\n{endc}")
    print (f"{white} 1. Find ProtoVision{endc}")
    print (f"{white} 2. DEFCON Status{endc}")
    print (f"{white} 3. View Statistics{endc}")
    print (f"{white} 4. List Games{endc}")
    print (f"{white} 5. Get Launch Code{endc}")
    print (f"{white} 6. Time Remaining{endc}")
    print (f"{white} 7. End Wargames\n{endc}")
    que = input(f"{yellow}Enter a number: {endc}")

    if que == "1":
        proto_vision() 

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


