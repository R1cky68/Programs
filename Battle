from sys import exit

name = input('Whats your name? ')
print('Let us battle', name + '! \n' 'I choose a grass type! ')

points = 0

T1 = input('Should I pick grass, fire, or water? ')
if (T1 == 'fire'):
    print('Ah! That was good', name + '!')
    points += 1

else: 
    print('Wrong choice', name + '!')

print('Okay! Now I will choose a fire type! What will you pick this time?')
    
T2 = input('Bit different now. Should I choose grass, fire or water? ')
if (T2 == 'water'): 
    print('Nice! That was the correct answer', name + '!')
    points += 1

else:
    print('Sorry ', name + '! That was wrong!')

print('Last one! This time it is a water type!')

T3 = input('Grass, fire or water now? ')

if (T3 == 'grass'):
    print('Damn! You got me', name + '! Congrats!')
    points += 1

else:
    print('So close! But you lose now', name + '!')

print('You won' , points, 'out of 3 battles')

if (points < 3):
    print('Game over' , name + '!')
    exit(0)

