import math


class Task1:
    __argumentsQuantity = 7

    def ___GetArgument(self):
        input_number = 0
        try:
            input_number = int(input())
        except ValueError:
            print("неверный ввод")
            input_number = self.___GetArgument()

        return input_number

    def ___Show(self, message):
        print(message)

    def ___Calculated(self, arguments):
        return (arguments[0] * arguments[1] * arguments[2] * math.sqrt(arguments[3])) / (
                math.fabs(arguments[4]) * (arguments[5] ** arguments[6]))

    def Run(self):
        arguments = []

        self.___Show("Введите все аргументы в данную формулу!!!\n  (a * b * c * корень от d) / (модуль(e) * (f) степень"
                     "g))")

        for i in range(self.__argumentsQuantity):
            arguments.append(self.___GetArgument())

        result = self.___Calculated(arguments)

        self.___Show('result = {}'.format(result))
