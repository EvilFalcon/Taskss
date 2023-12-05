import os
from PracticalTasks.Hometasks.DZ_1.Task import Task1
from PracticalTasks.Hometasks.DZ_2.Task import Task2
from PracticalTasks.Hometasks.DZ_3.Task import Task3
from PracticalTasks.Hometasks.DZ_4.Task import Task4

class Menu:
    def __init__(self, items):
        self.items = items
        self.programWork = True
        self.task1Command = 1
        self.task2Command = 2
        self.task3Command = 3
        self.task4Command = 4
        self.exitCommand = 0

    def Run(self):
        while self.programWork:
            os.system('cls || clear')
            print(f"Лабораторная №1 - клавиша {self.task1Command}")
            print(f"Лабораторная №2 - клавиша {self.task2Command}")
            print(f"Лабораторная №3 - клавиша {self.task3Command}")
            print(f"Лабораторная №4 - клавиша {self.task4Command}")
            print(f"для выхода нажмите {self.exitCommand} ")
            match self.UserInput():
                case self.task1Command:
                    self.GetTask(self.task1Command)()
                case self.task2Command:
                    self.GetTask(self.task2Command)()
                case self.task3Command:
                    self.GetTask(self.task3Command)()
                case self.task4Command:
                    self.GetTask(self.task4Command)()
                case self.exitCommand:
                    self.programWork = False

            os.system('cls || clear')

    def GetTask(self, index: int):
        return self.items[index - 1]

    def UserInput(self):
        input_number = 0
        try:
            input_number = int(input())
        except ValueError:
            print("неверный ввод")
            self.UserInput()

        return input_number


if __name__ == '__main__':
    task1 = Task1()
    task2 = Task2()
    task3 = Task3()
    task4 = Task4()
    core = Menu([task1.Run, task2.Run, task3.Run, task4.Run])
    core.Run()
