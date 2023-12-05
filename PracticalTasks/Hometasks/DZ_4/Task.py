class Task4:

    def Run(self):
        user_input = float(input("Введите число: "))
        result = self.__GetFibonacciNumbers(user_input)
        print(result)

    def __GetFibonacciNumbers(self, number):
        if number == 0 or number == 1:
            return number

        return self.__GetFibonacciNumbers(number - 1) + self.__GetFibonacciNumbers(number - 2)
