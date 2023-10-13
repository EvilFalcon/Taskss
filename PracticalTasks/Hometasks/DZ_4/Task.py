def Main():
    userInput = int(input("Введите число: "))
    result = GetFibonacciNumbers(userInput)
    print(result)


def GetFibonacciNumbers(number):
    if number == 0 or number == 1:
        return number

    return GetFibonacciNumbers(number - 1) + GetFibonacciNumbers(number - 2)


if __name__ == '__main__':
    Main()
