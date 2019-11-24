'''
Time: 11/11/2019 6:00 ETC+8
OS: Windows10 Enterprise 64 bit
NOTE: COPYRIGHT© BAO NING
Once you are reading or running the code you acknowledge that you admit the 'MIT license' used for this python script
For more info about the MIT license, visit www.github.com
Pay attention:
the layout of my game board is
    1   2   3   4   5   6   7
1
2
3
4
5
6
key: array[y][x]
'''
from preset import *
from printing import *
from dashboard import *
from judgement import *


def main():
    chess4board = [['-'] * 7 for i in range(0, 6)]
    index = 1
    txt_colour, txt_back = initialise()
    vali_arr = [0, 0, 0, 0, 0, 0, 0]
    while True:
        dash(txt_colour, txt_back, chess4board)
        if index == 1:
            x, y = user_and_input(chess4board, index, vali_arr)
            chess4board[6 - y][x] = '⚫'
            temp = 1
        elif index == 2:
            x, y = user_and_input(chess4board, index, vali_arr)
            chess4board[6 - y][x] = '🔷'
            index -= 2
            temp = 2
        index += 1
        judge = Judge(index, x, 6 - y, chess4board, temp)
        if judge.main_judge(x, 6 - y):
            break
    play_again()
    if platform_txt() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')
    main()


if __name__ == '__main__':
    main()
