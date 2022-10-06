def print_operation_table(operation, num_rows = 9, num_colums = 9):
    for i in range(1, num_rows + 1):
        for j in range(1, num_colums + 1):
            print(operation(i, j), "\t", end = '')
        print()

num1, num2 = (int(input("Введите числа ")) for i in range(2))
print('________________________')
print_operation_table(lambda x, y: x+y, num1)
print('________________________')
print_operation_table(lambda x, y: x*y, num1, num2)
print('________________________')
print_operation_table(lambda x, y: x**y, num2)
