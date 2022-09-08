# 2. Напишите программу, которая на вход принимает 5 чисел
#     и находит максимальное из них.
    
#    Примеры:
    
#    - 1, 4, 8, 7, 5 -> 8
#    - 78, 55, 36, 90, 2 -> 90
max = -1
for i in range(5):
    n= int(input())
    if max < n :
        max = n
print(max)

# flag = True
#i = 0
#while flag:
#    i += 1
#    if i == 11:
#        flag = False
#print(i)
