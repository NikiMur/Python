import math

arr = [int(i) for i in input("Введите числа через пробел: ").split()]
new_arr = list()
j = -1

for i in range(math.ceil(len(arr) / 2)):
  new_arr.append(arr[i] * arr[j])
  j -= 1

print(new_arr)