import os


def Main():
    path = "Text/Result/"

    settings = SetFormatting()
    originalText = ReadLine()
    formattedText = FormatingText(originalText, settings[0], settings[1], settings[2])
    PrintTexts(originalText, formattedText)
    SaveResult(formattedText, path)


def SetFormatting():
    replaceable = int(input("Введите номер буквы (а) которая будет заменена: ")) - 1
    replace = int(input("Введите номер буквы (б) которая заменит букву (а)")) - 1
    changeRegister = int(input("Введите номер буквы (с) у которой будет изменён регистр")) - 1

    return [replaceable, replace, changeRegister]


def FormatingText(originalText, replaceable, replace, changeRegister):
    words = originalText.split(" ")
    text = ""
    for word in words:
        chars = list(word)
        countChar = len(chars) - 1

        if countChar >= replaceable and countChar >= replace:
            chars[replaceable] = chars[replace]

        if countChar >= changeRegister:

            if word[changeRegister].isupper():
                chars[changeRegister] = chars[changeRegister].lower()
            elif word[changeRegister].islower():
                chars[changeRegister] = chars[changeRegister].upper()

        text = F'{text} {"".join(chars)}'

    return text


def PrintTexts(originalText, formattedText):
    print("Оригинальный Текст {0} \n\nОтформатированный текст{1}".format(originalText, formattedText))


def SaveResult(result, path):
    fileName = "Result.txt"
    resultFile = open(path + fileName, "w")
    resultFile.write(result)
    resultFile.close()


def ReadLine():
    text_file = open("Text/Text.txt")
    text = text_file.read()
    text_file.close()

    return text


if __name__ == '__main__':
    Main()
