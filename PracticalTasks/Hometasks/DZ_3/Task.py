
def Main():
    number = GetNumber()
    result = ConversionNumber(number)

    print(result)

def GetNumber():
    return int(input("Введите число :"))

def ConversionNumber(number: int )-> str:
    roman_numerals = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }
    roman_numeral = ''
    for value, symbol in roman_numerals.items():
        while number >= value:
            roman_numeral += symbol
            number -= value
    return roman_numeral



if __name__ == '__main__':
    Main()