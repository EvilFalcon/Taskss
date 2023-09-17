
def Main():
    number = GetNumber()
    result = ConversionNumber(number)

    print(result)

def GetNumber():
    return int(input("Введите число :"))

def ConversionNumber(number):
    ones = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    tens = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    hunds = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    thous = ["", "M", "MM", "MMM", "MMMM"]

    t = thous[number // 1000]
    h = hunds[number // 100 % 10]
    te = tens[number // 10 % 10]
    o = ones[number % 10]

    return t + h + te + o



if __name__ == '__main__':
    Main()