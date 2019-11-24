from termcolor import *
import time


# print(dashboard)

def reverse_array(array):
    global temp_arr
    temp_arr = []
    for i in range(0, 3):
        temp_arr = array[i]
        array[i] = array[5-i]
        array[5-i] = temp_arr


def dash(text_color, background_color, array):
    for i in range(1, 8):
        cprint('\t' + str(i), text_color, background_color, attrs=['bold'], end='')
    cprint('\t', text_color, background_color, attrs=['bold'], end='')
    print('')
    for i in range(0, 6):
        cprint('\t', text_color, background_color, attrs=['bold'], end='')
        for j in range(7):
            cprint(array[i][j] + '\t', text_color, background_color, attrs=['bold'], end='')
        print('')


def plain_print(arr):
    for i in range(5, -1, -1):
        for j in range(7):
            print('\t', arr[i][j], '\t', end='')
        print()


def user_and_input(array, user, valid_arr):
    cprint('user ' + str(user) + ' Which roll do you want to go?:', 'red', attrs=['bold'])
    # input validation
    user_roll = input()
    try:
        while int(user_roll) > 7 or int(user_roll) <= 0 or valid_arr[int(user_roll)-1]>=6:
            cprint('Invalid input! Please enter again:', 'red', attrs=['bold'])
            user_roll = input()
    except ValueError:
        cprint('WARNING:: If your input is invalid again, the program would EXIT', 'red', attrs=['bold'])
        try:
            user_roll = input()
            if int(user_roll) > 7 or int(user_roll) <= 0:
                while 0 < int(user_roll) < 7:
                    cprint('Invalid input! Please enter again:', 'red', attrs=['bold'])
                    user_roll = input()
        except ValueError:
            cprint('Now quiting...', 'red', attrs=['bold'])
            time.sleep(1)
            quit()
    except IndexError:
        cprint('WARNING:: If your input is invalid again, the program would EXIT', 'red', attrs=['bold'])
        try:
            user_roll = input()
            if int(user_roll) > 7 or int(user_roll) <= 0:
                while 0 < int(user_roll) < 7:
                    cprint('Invalid input! Please enter again:', 'red', attrs=['bold'])
                    user_roll = input()
        except ValueError:
            cprint('Now quiting...', 'red', attrs=['bold'])
            time.sleep(1)
            quit()
    valid_arr[int(user_roll) - 1] += 1
    # print(valid_arr)
    x_loc = int(user_roll) - 1
    y_loc = valid_arr[x_loc]
    return x_loc, y_loc

# 🔷⚫▰
if __name__ == '__main__':
    # validation_array = [0, 0, 0, 0, 0, 0, 0]
    # dash('blue', 'on_green')
    # user_and_input( 'User1', validation_array, '▰')
    # dash('blue', 'on_green')
    dashboard = [['-' for i in range(0, 7)] for j in range(0, 6)]
    dashboard[0][1] = 'x'
    reverse_array(dashboard)
    dash('blue', 'on_green', dashboard)