import os


class Task2:
    def __SetFormatting(self):
        replaceable = int(input("Введите номер буквы (а) которая будет заменена: ")) - 1
        replace = int(input("Введите номер буквы (б) которая заменит букву (а)")) - 1
        changeRegister = int(input("Введите номер буквы (с) у которой будет изменён регистр")) - 1

        return [replaceable, replace, changeRegister]

    def __FormatingText(self, originalText, replaceable, replace, changeRegister):
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

    def __PrintTexts(self, originalText, formattedText):
        print("Оригинальный Текст {0} \n\nОтформатированный текст{1}".format(originalText, formattedText))

    def __SaveResult(self, result, path):
        fileName = "Result.txt"
        resultFile = open(path + fileName, "w")
        resultFile.write(result)
        resultFile.close()

    def __ReadLine(self):
        text_file = open("Hometasks/DZ_2/Text/Text.txt")
        text = text_file.read()
        text_file.close()

        return text

    def Run(self):
        path = "Hometasks/DZ_2/Text/Result/"

        settings = self.__SetFormatting()
        originalText = self.__ReadLine()
        formattedText = self.__FormatingText(originalText, settings[0], settings[1], settings[2])
        self.__PrintTexts(originalText, formattedText)
        self.__SaveResult(formattedText, path)
