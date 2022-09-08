n = int(input('Ввведите число'))
if (n % 5 == 0 and n % 10 == 0 )or (n % 15 == 0 and n % 30 != 0):
    print('Крастно' )
else:
    print('Некратно')
     