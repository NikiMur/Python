import random

arr, new_arr = [random.randint(1,10) for i in range(10)], list()
print(arr)
for i in range(len(arr)):
    if arr.count(arr[i]) == 1: new_arr.append(arr[i])
print(new_arr)