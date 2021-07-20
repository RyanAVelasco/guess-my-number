import random
import time
import colored
from colored import stylize

t_white = colored.fg('255')

## What this project does
print(stylize('Number Guessing', t_white), '\n')

print(stylize('\tThis is one of the simple python projects yet an exciting one. You can even call it a mini-game. Make a program in which the computer randomly chooses a number between 1 to 10, 1 to 100, or any range. Then give users a hint to guess the number. Every time the user guesses wrong, he gets another clue, and his score gets reduced. The clue can be multiples, divisible, greater or smaller, or a combination of all.', t_white), '\n')

print(stylize('\tYou will also need functions to compare the inputted number with the guessed number, to compute the difference between the two, and to check whether an actual number was inputted or not in this python project.', t_white), '\n')

## functions
def check(player, cpu):
    global freedom

    if int(player) == int(cpu) : print('You guess right!\n You:', player, '-', 'CPU:', cpu)
    elif int(player) < int(cpu):
        print('Too low')
        return
    else:
        print('Too high')
        return

    freedom = input('Play again? (Y/N)').lower().strip()
    if freedom == 'y' or freedom == 'yes' : freedom = True
    else : quit()

    

def range():
    global cpu_number
    
    while True:
        num_range = input('\nEnter your choice here: ').lower().strip()

        if num_range == '1' or num_range == 'ten' or num_range == '10':
            cpu_number = random.randint(1, 10)
            break
        elif num_range == '2' or num_range == 'hundred' or num_range == '100':
            cpu_number = random.randint(1, 100)
            break
        elif num_range == '3' or num_range == 'thousand' or num_range == '1000':
            cpu_number = random.randint(1, 100)
            break
        elif num_range == '4' or num_range == 'million' or num_range == '1000000':
            cpu_number = random.randint(1, 1000000)
            break
        elif num_range == '5' or num_range == 'infinity':
            cpu_number = random.randint(1, 1000000)
            break
        else:
            print('\n[ ERROR ] Sorry the only choices were: ten ( 10 ), hundred ( 100 ), thousand ( 1000 ) or million ( 1000000 )')
            print('\n[ ERROR ] Please try again.. noob')


## main code starts here
print('\nWelcome to Number Guessing!')
print('\nFirst things first, please choose a from the list of options below.')

# choose a range of numbers that the cpu will pick from
while True:
    freedom = False
    print('\n============================================================')
    print('\nHow high should the number the CPU reach?\n\n1.\tTen\n2.\tHundred\n3.\tThousand\n4.\tMillion\n5.\tInfinity')
    range()

    #Your turn to play
    print('\nIt\'s your turn to choose a number now')    
    while freedom == False:
        p_guess = input('\nChoose a number:', )
        check(p_guess, cpu_number)
        