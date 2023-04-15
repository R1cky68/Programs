import time
import random
from sys import exit

print('Hahaha! You will never defeat my Charizard with your Lucario! Do your worst!')

Chealth = 140
Phealth = 100

def AS():
    global Chealth
    Chealth = Chealth - 50

def ES():
    global Chealth
    Chealth = Chealth - 40

def DP():
    global Chealth
    Chealth = Chealth - 35

def MM():
    global Chealth
    Chealth = Chealth - 45

Cmoves = [1, 2, 3]
def Cmove():
    global Phealth
    random.choice(Cmoves)
    if (random.choice(Cmoves) == 1):
        print('Charizard use air slash!')
        Phealth = Phealth - 35

    elif (random.choice(Cmoves) == 2):
        print('Charizard use dragon claw!')
        Phealth = Phealth - 30

    else:
        print('Charizard use flamethrower!')
        Phealth = Phealth - 50

b = True
t1 = time.time()
M1=input('I have the first move. Should I use aura sphere, extremespeed, dragon pulse or meteor mash? ')
t2 = time.time()
t = round(t2 - t1)
print('You took', t, 'seconds!')

if (t > 5):
    print('Too late! Lucario could not move!')
    b = False

elif (b == True):
    if (M1 == 'aura sphere'):
            AS() 

    elif (M1 == 'extremespeed'):
            ES()

    elif (M1 == 'dragon pulse'):
            DP()

    elif (M1 == 'meteor mash'):
            MM()
                
    else:
        print('Select a valid move!')

print('Charizard has', Chealth, 'health remaining! \nOkay my turn now!')

Cmove()
print('Lucario has', Phealth, 'health remaining!')

if (Phealth == 0):
    print('Lucario is out of health! Lucario fainted! Game over!')
    exit(0)

M2 = input('That hurt. Now should I use aura sphere, extremespeed, dragon pulse or meteor mash? ')
t = round(t2 - t1)
print('You took', t, 'seconds!')

if (t > 5):
    print('Too late! Lucario could not move!')
    b = False

elif (b == True):
    if (M2 == 'aura sphere'):
        AS()

    elif (M2 == 'extremespeed'):
        ES()

    elif (M2 == 'dragon pulse'):
        DP()

    elif (M2 == 'meteor mash'):
        MM()
        
    else:
        print('Select a valid move!')

print('Charizard has', Chealth, 'health remaining!')

Cmove()
print('Lucario has', Phealth, 'health remaining!')

M3 = input('Last move now! Make it count! Aura sphere, extremespeed, dragon pulse or meteor mash? ')
t = round(t2 - t1)
print('You took', t, 'seconds!')

if (t > 5):
    print('Too late! Lucario could not move!')
    b = False

elif (b == True):
    if (M3 == 'aura sphere'):
        AS()

    elif (M3 == 'extremespeed'):
        ES()

    elif (M3 == 'dragon pulse'):
        DP()

    elif (M3 == 'meteor mash'):
        MM()
        
    else:
        print('Select a valid move!')

print('Charizard has', Chealth, 'health remaining!')

if (Chealth <= 0):
    print('Charizard has', Chealth, 'health! Charizard has fainted! You win!')

else:
    print('This ends here!')
    Cmove()

    if (Phealth <= 0):
        print('Lucario has' , Phealth , 'health! Lucario is out of health! Game over!')

    elif(Phealth > 0):
        if (Chealth > Phealth):
            print('I have more health, but we will see next time')
            
        else:
            print('You have more health, good job')

    else:
        print('Damn a tie! Not bad', Phealth, Chealth)
