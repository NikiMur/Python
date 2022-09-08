import random

n = 5

lst = [random.randint(0, 1) for i in range(n)]
print(lst)

if lst.count(1) > lst.count(0):
    print(f"Минимальное число решек: {lst.count(0)}") 
else:
    print(f"Минимальное число гербов {lst.count(1)}")


print((f"Минимальное число решек: {lst.count(0)}", 
f"Минимальное число гербов {lst.count(1)}")[lst.count(1) < lst.count(0)])     
