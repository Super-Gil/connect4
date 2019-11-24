from judgement import *
from preset import *
from termcolor import *
import os
import random, time

def loop_colour_choice(choice, n):
    while choice == n:
        choice = input("Re-enter Please:")
    try:
        choice = int(choice)
    except ValueError:
        choice = ""
    return choice


def judge_user_input_on_choosing_colour(user_colour_choice):
    global run
    run = True
    while run:
        if user_colour_choice == 1:
            print('Choosing colour for you...')
            time.sleep(0.5)
            n = random.randint(1, 4)
            judge_user_input_on_choosing_colour(n)
        elif user_colour_choice == 2:
            print("The colour you have chosen is: ")
            text = 'Blue-Yellow'
            text_colour = 'blue'
            text_back = 'on_yellow'
            cprint(text, text_colour, text_back, attrs=['bold'])
            run = False
            return text_colour, text_back
            break
            # return text, text_colour, text_back
        elif user_colour_choice == 3:
            print("The colour you have chosen is: ")
            text = 'Yellow-Magenta'
            text_colour = 'yellow'
            text_back = 'on_magenta'
            cprint(text, text_colour, text_back, attrs=['bold'])
            run = False
            return text_colour, text_back
            break
            # return text, text_colour, text_back

        elif user_colour_choice == 4:
            print("The colour you have chosen is: ")
            text = 'Green-Blue'
            text_colour = 'green'
            text_back = 'on_blue'
            cprint(text, text_colour, text_back, attrs=['bold'])
            run = False
            return text_colour, text_back
            break
            # return text, text_colour, text_back
        else:
            user_colour_choice = random.randint(2, 4)
            judge_user_input_on_choosing_colour(user_colour_choice)
            return user_colour_choice, user_colour_choice


def initialise():
    global t1ext_buffer, t2ext_colour, t3ext_back, user_colour_choice
    t1ext_buffer = 'Blue-Yellow'
    t2ext_colour = 'blue'
    t3ext_back = 'on_yellow'

    if platform_txt() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    print('Which colour scheme would you like to use?')
    cprint('1. Random')
    cprint('2. Blue-Yellow', 'blue', 'on_yellow', attrs=['bold'])
    cprint('3. Yellow-Magenta', 'yellow', 'on_magenta', attrs=['bold'])
    cprint('4. Green-Blue', 'green', 'on_blue', attrs=['bold'])
    cprint('Enter your choice below:', 'red', attrs=['bold'])
    cprint('WARNING: Any INVALID inputs would be regarded choosing the option "random"!', 'red')
    try:
        user_colour_choice = int(input())
    except TypeError:
        user_colour_choice = 1
    if user_colour_choice < 1 or user_colour_choice > 4 or len(str(user_colour_choice)) > 1:
        user_colour_choice = 1
    t2ext_colour, t3ext_back = judge_user_input_on_choosing_colour(user_colour_choice)
    return t2ext_colour, t3ext_back
    # t1buffer, t2colour, t3back = judge_user_input_on_choosing_colour(user_colour_choice)
    # return t1buffer, t2colour, t3back


def play_again():
    try_again = input("Would you like to play again?(Y/n)")
    if try_again == 'Y' or try_again == 'y' or try_again == '':
        cprint('Reloading...Please wait for a sec', 'red', attrs=['bold'])
        time.sleep(2)
        reset(t1ext_buffer, t2ext_colour, t3ext_back)
    else:
        cprint('Thanks for playing, now quiting...', 'red', attrs=['bold'])
        quit()


if __name__ == '__main__':
    initialise()
    play_again()