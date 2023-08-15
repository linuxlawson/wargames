#!/usr/bin/env python3
#Wargames WOPR Simulation

import os
import sys
import time
import datetime
import string
import random
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
    print("")

#menu item 1
def proto_vision():
    os.system('clear')
    print (f"{white}\nSCAN FOR CARRIER TONES IN SUNNYVALE, CA{endc}")
    time.sleep (.5)
    print (f"{white}\nSEARCHING FOR PROTOVISION\n{endc}")
    time.sleep (.5)
    print (f"{white}AREA\nCODE PRFX NUMBER\n")
    time.sleep (1)
    acode = ["(311)"]
    prefx = ["767"]
    for x in acode:
        for y in prefx:
            for z in range(9978, 9995): 
                print(x, y, z); sleep(.5)
proto_vision()


os.system('clear')
time.sleep (1)

def carrier_tones():
    os.system('clear')
while True:
    print (f"{white}\nNUMBERS FOR WHICH CARRIER TONES WERE DETECTED:\n\n{endc}")
    print (f"{white} 1. (311) 399 2364{endc}")
    print (f"{white} 2. (311) 399 3582{endc}")
    print (f"{white} 3. (311) 437 8739{endc}")
    print (f"{white} 4. (311) 437 1083 <== ########{endc}")
    print (f"{white} 5. (311) 437 2977{endc}")
    print (f"{white} 6. (311) 767 7305{endc}")
    print (f"{white} 7. (311) 767 3395{endc}")
    print (f"{white} 8. (311) 936 1493{endc}")
    print (f"{white} 9. (311) 936 3923\n\n\n\n{endc}")
    que = input(f"{white}Please select number and then [ENTER] to start dialing. {endc}")

    if que == "4":
        break
    else:   
        carrier_tones()


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


def try_one():
    print ("\n")
os.system('clear')
time.sleep (.8)
print (f"{yellow}\nTry 'help' or 'help games'\n{endc}")

attempts=0
while attempts<3:
    uname = input(white + "LOGON: " + endc)
    if uname == ('help games'):
        games_desc()
        break
    elif uname in ['Help', 'help']:
        print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
    else:
        print (f"{white}\n***Improper Request***\n{endc}")
try_one()


def try_two():
    print ("")
time.sleep (.8)
print (f"{yellow}Try 'games' or 'list games'\n{endc}")

attempts=0
while attempts<3:
    uname = input(f"{white}LOGON: {endc}")
    if uname == ('list games'):
        game_list()
        break
    elif uname in ['Help', 'help']:
        print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
    else:
        print (f"{white}\n***Improper Request***\n{endc}")
try_two()


def log_on():
    print ("")
os.system('clear')
attempts=0
while attempts<3:
    logon = input(f"{white}\nLOGON: {endc}")
    if logon in ['Joshua', 'joshua']:
        break
    elif logon in ['Help', 'help']:
        print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
    else:
        print (f"{white}\nIDENTIFICATION NOT RECOGNIZED BY SYSTEM\n{endc}")
log_on()


def is_glitch(): 
    time.sleep (.4)
    os.system('clear')
    print(f"{white}-------------------------{endc}")
    time.sleep (.3)
    os.system('clear')
    print(f"\n{white}-------------------------{endc}")
    time.sleep (.2)
    os.system('clear')
    print(f"\n\n{white}-------------------------{endc}")
    time.sleep (.1)
    os.system('clear')
    print(f"{white}-------------------------{endc}")
    time.sleep (.1)
    os.system('clear')
is_glitch()


#conversation 1
def convo_one():
    time.sleep (.8)
os.system('clear')
time.sleep (1)
string = (f"{white}\nGREETINGS PROFESSOR FALKEN.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #hello
print ("")
time.sleep (.5)

#wopr
string = (f"{white}HOW ARE YOU FEELING TODAY?\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #I am fine, how are you?
print ("")
time.sleep (.5)

#wopr
string = (f"{white}EXCELLENT. ITS BEEN A LONG TIME. CAN YOU EXPLAIN\nTHE REMOVAL OF YOUR USER ACCOUNT NUMBER 6/23/73?\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

#ques
say = input('') #people sometimes make mistaks?
print ("")
time.sleep (.5)

#wopr
string = (f"{white}YES THEY DO.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
convo_one()


def wel_come():
    print ("")
os.system('clear')
print ("\n\n################################")
print ("#                              #")
print ("#           WELCOME            #")          
print ("#                              #")
print ("#    Distinguished Visitors    #")
print ("#                              #")
print ("#            from              #")
print ("#                              #")
print ("#      City of Birmingham      #")
print ("#                              #")
print ("################################")
print ("")
time.sleep (1)
wel_come()

#menu item 6
def time_remain(timer):
    print (f"{white}\n\n ESTIMATED TIME REMAINING: \n{endc}")
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}'.format(secs)
        print (white + "  14 HRS  28 MIN ", timeformat, 'SEC', end='\r' + endc)
        time.sleep(1)
        timer -= 1
time_remain(6)


#conversation II
def convo_two():
    time.sleep (.8)
os.system('clear')
string = (f"{white}\nGREETINGS PROFESSOR FALKEN.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #im not falken, falken is dead
print ("")
time.sleep (.5)

#wopr
string = (f"{white}IM SORRY TO HEAR THAT, PROFESSOR.\n\nYESTERDAYS GAME WAS INTERUPTED.\n\nALTHOUGH PRIMARY GOAL HAS NOT YET\nBEEN ACHIEVED, SOLUTION IS NEAR.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (.5)

#wopr
string = (f"{white}YOU SHOULD KNOW PROFESSOR, YOU PROGRAMMED ME.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what is the primary goal?
print ("")
time.sleep (.5)

#wopr
string = (f"{white}TO WIN THE GAME.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)
convo_two()


def launch_codes():
    print ("")
    os.system('clear')
    print ("")
    time.sleep (0.5)

    target = ("CPE 1704 TKS")
    iscaps = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    isnums = list("1234567890")
    isspace = list(" ")

    attemptThis = ''.join(random.choice(iscaps + isnums + isspace) 
        for _ in range(len(target)))
    attemptNext = ''

    completed = False
    generation = 0

    while not completed:
        print(' ', bold + white + attemptThis, end='\r' + endc)
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


    time.sleep (1)
    print ("\n\n\n  Launch Code Authentic")
    time.sleep (0.8)
    print ("\n  Launch Order Confirmed")
    time.sleep (0.8)
    print ("\n  Launch missles in T-minus "f"{generation} second(s)\n")
    time.sleep (0.5)
    print(f"{white}\n  -------------------------{endc}")
    time.sleep (0.2)
    print(f"{white}\n  -------------------------{endc}")
    time.sleep (0.2)
    print ("\n  Turn your key, sir. \n")
    time.sleep (1)
    print("")
launch_codes()


#conversation III
def convo_three():
    time.sleep (.8)
os.system('clear')
string = (f"{white}\nGREETINGS PROFESSOR FALKEN.\n\n\n{endc}")
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.04)


#ques
say = input('') #hello, are you still playing the game?
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


#menu item 3
def view_stats():
    time.sleep (0.6)
    print ("")
    string = (white + " UNITED STATES\n UNITS DESTROYED     MILITARY FORCES\n" 
                  "\n       68%           BOMBERS\n" 
                    "       54%           ICBM'S\n"
                    "       12%           ATTACK SUBS\n"
                    "       39%           TACTICAL ARICRAFT\n"
                    "       58%           GROUND FORCES\n\n\n")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)


    string = (" UNITED STATES       CIVILIAN ASSETS\n"
                  "\n       69%           HOUSING\n" 
                    "       22%           TRANSPORTATION\n"
                    "       70%           COMMUNICATIONS\n"
                    "       45%           FOOD STOCKPILES\n"
                    "       89%           HOSPITALS\n\n\n")
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)


    string = (" UNITED STATES       HUMAN RESOURCES\n"
                  "\n 49 MILLION          NON-FATAL INJURED\n" 
                    " 72 MILLION          POPULATION DEATHS\n\n\n" + endc)
    for char in string:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(.04)
view_stats()


#ques
say = input('') #is this a game or is it real?
print ("")
time.sleep (.5)

#wopr
string = (white + "WHATS THE DIFFERENCE?\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)

#wopr
time.sleep (1)#here
string = (white + "\nYOU ARE A HARD MAN TO REACH. COULD NOT FIND \nYOU IN SEATTLE AND NO TERMINAL IS IN \nOPERATION AT YOUR CLASSIFIED ADDRESS.\n\n\n" + endc)
for char in string:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(.05)


#ques
say = input('') #what classified address?
time.sleep (.5)

#wopr
string = (white + "\nDOD PENSION FILES INDICATE \nCURRENT MAILING AS:\n\n" + endc)
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
convo_three()


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
    print (" \n--CONNECTION TERMINATED-- \n" + endc)
    time.sleep (0.5)


#menu item 2
def def_con():
    os.system('clear')
    print (f"{red}\n")
    print (" $$$$$$$   $$$$$$  $$$$$$  $$$$$$  $$$$$$  $$   $$     $$$$$$$")
    print (" $$    $$  $$      $$      $$      $$  $$  $$$  $$         $$")
    print (" $$     $$ $$$$$   $$$$$   $$      $$  $$  $$ $ $$      $$$$$")
    print (" $$    $$  $$      $$      $$      $$  $$  $$  $$$          $$")
    print (" $$$$$$$   $$$$$$  $$      $$$$$$  $$$$$$  $$   $$     $$$$$$$")
    print (f"{endc}\n\n")



def davids_grades():
    time.sleep (.5)
    os.system('clear')
    print (f"{white}\nPLEASE ENTER STUDENT NAME: Lightman, David L")
    print ("\n\n CLASS #   COURSE TITLE        GRADE     TEACHER     PERIOD      ROOM")
    print (f"{bold} ____________________________________________________________________{endc}")
    print (F"{white}\n S-202     BIOLOGY 2             F       LIGGET        3         214")
    print (" E-325     ENGLISH 11B           D       TURMAN        5         114")
    print (" H-221     WORLD HISTORY 11B     C       DWYER         2         108")
    print (" L-134     TRIG 2                B       DICKERSON     4         315")
    print (" G-212     LUNCH                 -       NONE          5         CAF")
    print (f"{white} G-322     PHYSICAL EDUCATION    B       COMSTOCK      6         GYM{endc}")
    print ("\n")


def jenns_grades():
    time.sleep (.5)
    os.system('clear')
    print (f"{white}\nPLEASE ENTER STUDENT NAME: Mack, Jennifer K")
    print ("\n\n CLASS #   COURSE TITLE        GRADE     TEACHER     PERIOD      ROOM")
    print (f"{bold} ____________________________________________________________________{endc}")
    print (f"{white}\n S-202     BIOLOGY 2             F       LIGGET        3         214")
    print (" E-325     ENGLISH 11B           A       ROBINSON      1         114")
    print (" H-221     WORLD HISTORY 11B     B       DWYER         2         108")
    print (" L-134     HOME ECONOMICS        D       MARKS         4         311")
    print (" G-212     GEOMETRY              C       JENKINS       5         116")
    print (f"{white} G-322     PHYSICAL EDUCATION    C       COMSTOCK      6         GYM{endc}")
    print ("\n")


def data_net():
    print ("")
    os.system('clear')
    time.sleep (.8)
    print (f"{white}\nWELCOME TO THE SEATTLE PUBLIC SCHOOL DISTRICT DATANET{endc}")

    attempts=0
    while attempts<3:
        aname = input(f"{white}\nPLEASE LOGON WITH USER PASSWORD: {endc}")
        if aname == ('pencil'):
            break
        elif aname in ['Help', 'help']:
            print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
        else:
            print (f"{white}\n** IMPROPER REQUEST **\n{endc}")


    os.system('clear')
    attempts=0
    while attempts<3:
        aname = input(f"{white}\nPLEASE ENTER STUDENT NAME: {endc}")
        if aname in ['Lightman, David L', 'David Lightman', 'Lightman', 'David']:
            davids_grades()
            break    
        elif aname in ('Mack, Jennifer K', 'Jennifer Mack', 'Mack', 'Jennifer'):
            jenns_grades()
            break
        elif aname in ['Help', 'help']:
            print (f"{white}\nHELP NOT AVAILABLE\n{endc}")
        else:
            print (f"{white}\n** IMPROPER REQUEST **\n{endc}")



#menu
def menu_code():
	print ("")
while True:
    time.sleep (1)
    print (f"{yellow}\nMenu Options\n{endc}")
    print (f"{white} 1. Find ProtoVision{endc}")
    print (f"{white} 2. DEFCON Status{endc}")
    print (f"{white} 3. View Statistics{endc}")
    print (f"{white} 4. List Games{endc}")
    print (f"{white} 5. Get Launch Code{endc}")
    print (f"{white} 6. Time Remaining{endc}")
    print (f"{white} 7. DataNet{endc}")
    print (f"{white} 8. End Wargames\n{endc}")
    que = input(f"{yellow}Enter a number: {endc}")

    if que == "1":
        proto_vision() 

    elif que == "2":
        def_con()

    elif que == "3":
        os.system('clear')
        view_stats()

    elif que == "4":
        game_list()

    elif que == "5":
        launch_codes()

    elif que == "6":
        time_remain(5)

    elif que == "7":
        data_net()        
        
    elif que == "8":
        end_game()        
        break
menu_code()


if __name__ == "__main__":
    main()

