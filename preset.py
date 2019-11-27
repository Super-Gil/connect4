import os
import platform
import sys
import time


def platform_txt():
    return platform.system()


def detect():
    count = 2
    while count:
        try:
            import termcolor  # 引入需要的模块
            break

        except:
            print('termcolor MODULE is not ready, installing...')
            time.sleep(2)
            os.system('pip install termcolor')
            count -= 1
            continue


def encoding_detect():
    if sys.getdefaultencoding() == 'gbk':
        print('The script would not run correctly if you are using gbk encoding!')
        print('Please change your system default encoding to support "UTF-8"')


if __name__ == '__main__':
    print(platform.system())
    print(sys.getdefaultencoding())
    encoding_detect()
    detect()
