n = int(input("Введите колиичество чисел из ряда Негафибоначи: "))
def fibb(n):
    lst = []
    f1, f2 = 1, 1
    for i in range(abs(n)):
       lst.append(f1)
       f1, f2 = f2, f1 + f2
    return lst
def neg_fibb_2(n):
    lst = fibb(n)
    for i in range(len(lst)):
      if i %2 != 0:
        lst[i] = lst[i]*(-1)
    lst1 = lst[::-1]
    return lst1

print(neg_fibb_2(n) + [0] + fibb(n))