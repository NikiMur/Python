from ui import hello_user
from random import  randint
def search():
    while True:
        hello_user()
        n = int(input())
        if n ==1:
            with open('d:\Coding\Python\PythonHomeWork\8HomeWork\students.csv', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')

        elif n == 2:
            with open('d:\Coding\Python\PythonHomeWork\8HomeWork\class.csv', 'r', encoding = 'utf_8') as f:
                    for line in f.readlines():
                        print(line)
            input('\nНажмите enter')

        elif n == 3:
            answer = input('Введите фамилию ученика: ').title()
            with open('d:\Coding\Python\PythonHomeWork\8HomeWork\students.csv', 'r', encoding='utf_8') as f:
                for line in f.readlines():
                    if answer in line:
                        a = line.split()
                        print(a[3])

        elif n == 4:
            f = open('d:\Coding\Python\PythonHomeWork\8HomeWork\students.csv','a+', encoding = 'utf_8')
            new_contact = input('Введите данные(ФИ, год рождения, успеваемость, ID) ').split(' ')
            f.write('\n'+'\t'.join(new_contact))
            f.close()
            input('\nНажмите enter')

        elif n == 5:
            answer = input("Введите Фамилию: ")
            with open('d:\Coding\Python\PythonHomeWork\8HomeWork\class.csv', 'r', encoding='utf_8') as f:
                a = len(f.readlines())

            f = open('d:\Coding\Python\PythonHomeWork\8HomeWork\students.csv', 'r', encoding='utf_8')
            for line in f.readlines():
                if answer in line:
                    with open('d:\Coding\Python\PythonHomeWork\8HomeWork\class.csv', 'r', encoding='utf_8') as f:
                        print(f.readlines()[randint(1,a-1)])

        elif n == 6:
            print('До встречи')
            exit()