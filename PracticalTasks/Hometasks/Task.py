import math


class Task:

    def Calculated(self):
        return (3 * 5 * 10 * math.sqrt(49)) / (math.fabs(-10) * (0.01 ** (1 / 3)))

    def Get_Solution(self):
        result = self.Calculated()
        print(format(result))
