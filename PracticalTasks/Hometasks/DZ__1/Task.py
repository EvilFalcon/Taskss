import math


class Task:
    __argumentsQuantity = 7

    def __UserInput(self):
        return float(input())

    def __Show(self, message):
        print(message)

    def __Calculated(self, arguments):
        return (arguments[0] * arguments[1] * arguments[2] * math.sqrt(arguments[3])) / (
                math.fabs(arguments[4]) * (arguments[5] ** arguments[6]))

    def ShowResults(self):
        arguments = []

        self.__Show("Введите все аргументы в данную формулу!!!\n  (a * b * c * корень от d) / (модуль(e) * (f) степень "
                    "g))")

        for i in range(self.__argumentsQuantity):
            arguments.append(self.__UserInput())

        result = self.__Calculated(arguments)

        self.__Show('result = {}'.format(result))
