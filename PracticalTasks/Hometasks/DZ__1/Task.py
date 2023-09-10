import math


class Task:
    ___argumentsQuantity = 7

    def ___GetArgument(self):
        return float(input())

    def ___Show(self, message):
        print(message)

    def ___Calculated(self, arguments): #
        return (arguments[0] * arguments[1] * arguments[2] * math.sqrt(arguments[3])) / (
                math.fabs(arguments[4]) * (arguments[5] ** arguments[6]))

    def Run(self):
        arguments = []

        self.___Show("Введите все аргументы в данную формулу!!!\n  (a * b * c * корень от d) / (модуль(e) * (f) степень"
                     "g))")

        for i in range(self.___argumentsQuantity):
            arguments.append(self.___GetArgument())

        result = self.___Calculated(arguments)

        self.___Show('result = {}'.format(result))
