from menu import main_menu as mn
from log import read, app, imp, export



def prog():
    print("Вас приветствует программа 'Телефонный справочник'")
    while True:
        answer = mn()
        if answer == '1':
            read()

        elif answer == '2':
            app()

        elif answer == '3':
            imp()

        elif answer == '4':
            export()

        elif answer == '5':
            print("Программа завершена!")
            exit()

        else:
            print("Введите цифру от 1 до 5!")