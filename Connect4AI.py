# Want to play with AI
class Ai:
    def __init__(self, array, validation_array):
        self.array = array
        self.validation_array = validation_array

    def get_locations(self, *num):
        for i in range(7):
            num[i] = self.validation_array[i]
        for i in range(7):
            if 0 <= self.validation_array[i] + 1 < 7:
                num[i] += 1
            else:
                num[i] = -1
        return num

    def scoring(self):
        # Initialise variables
        temp_arr, individual_score, sub_arr = [0, 0, 0, 0, 0, 0, 0]
        temp_arr = self.get_locations(temp_arr)

        # Sub scoring
        for i in range(7):
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[6 - temp_arr[i]][i+1]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[6 - temp_arr[i]][i-1]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[7 - temp_arr[i]][i]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[5 - temp_arr[i]][i+1]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[5 - temp_arr[i]][i-1]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[7 - temp_arr[i]][i+1]:
                    individual_score += 100
            except IndexError:
                pass
            try:
                if self.array[6 - temp_arr[i]][i] == self.array[7 - temp_arr[i]][i-1]:
                    individual_score += 100
            except IndexError:
                pass
        for i in range(7):
            if temp_arr[i] == -1:
                individual_score[i] = -1000
            else:
                pass
            # TODO: OTHER SCORING METHODS SHOULD BE ADDED IN!
            return individual_score

    def final_decision_max(self):
        arr = self.scoring()
        maximum = 0
        for i in range(7):
            if maximum < arr[i]:
                maximum = arr[i]
        return maximum

