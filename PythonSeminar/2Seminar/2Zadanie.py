#n = int(input('Ввведите первое число'))
#step = 4
#for i in range(n):
#    print(f'{i+1}:{step}  ')
#    step = step + 3

n = int(input())
d = {}
for i in range(1, n+1):
    d[i] = 3 * i + 1
print(d)


