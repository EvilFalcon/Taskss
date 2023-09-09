import math


class Task:

    def Calculated(self):
        return (3 * 5 * 10 * math.sqrt(49)) / (math.fabs(-10) * (0.01 ** (1 / 3)))

    def Show_Solution(self):
        result = self.Calculated()
        print('result = {}'.format(result))
