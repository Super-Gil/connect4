'''
Time: 11/11/2019 6:00 ETC+8
MIT License

Copyright (c) [2019] [Bao Ning]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

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
    encoding_detect()
    main()
