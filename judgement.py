from termcolor import cprint


class Judge:
    lFlag = False

    def __init__(self, user, x_loc, y_loc, array, counter):
        self.user = user
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.array = array
        self.counter = counter

    def simplify(self, a, b, c, d):
        try:
            if self.array[a][b] == self.array[c][d]:
                if self.counter == 3:
                    cprint('User ' + str(self.user) + ' Wins', 'red', attrs=['bold'])
                    self.lFlag = True
                    return True
                return True
            else:
                return False
        except IndexError:
            return False

    # lFlag means local global flag!
    def main_judge(self, x_loc, y_loc):
        # Horizontal ->
        if self.user == 1:
            self.user = 2
        else:
            self.user = 1
        lFlag = False
        for i in range(1, 4):
            self.counter = i
            if self.simplify(y_loc, x_loc, y_loc, x_loc + i):
                pass
            else:
                i -= 1
                for j in range(1, 4 - i):
                    self.counter = i+j
                    if self.simplify(y_loc, x_loc, y_loc, x_loc - j):
                        pass
                    else:
                        break
                break
        if self.lFlag:
            return True

        # Vertical direction(Downwards)
        for i in range(1, 4):
            self.counter = i
            if self.simplify(y_loc, x_loc, y_loc + i, x_loc):
                pass
            else:
                break
        if self.lFlag:
            return True

        # y = x direction +tan-1(1)
        for i in range(1, 4):
            self.counter = i
            if self.simplify(y_loc, x_loc, y_loc - i, x_loc + i):
                pass
            else:
                self.counter -= 1
                for j in range(1, 4 - i):
                    if self.simplify(y_loc, x_loc, y_loc + i, x_loc - i):
                        pass
                    else:
                        break
                break
        if self.lFlag:
            return True

        # y = -x direction -tan-1(1)
        for i in range(1, 4):
            self.counter = i
            if self.simplify(y_loc, x_loc, y_loc + i, x_loc + i):
                pass
            else:
                self.counter -= 1
                for j in range(1, 4 - i):
                    self.counter = i+j
                    if self.simplify(y_loc, x_loc, y_loc - i, x_loc - i):
                        pass
                    else:
                        break
                break
        if self.lFlag:
            return True
