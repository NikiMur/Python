#Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.Пример:
n = int(input('Введите число'))
if n == 6 or n == 7:
    print('Ура выходной')
elif 1 < n < 7:  
 print('рабочий день')
else:
 print('Такого дня недели нет')