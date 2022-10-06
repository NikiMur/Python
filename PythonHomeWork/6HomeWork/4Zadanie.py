vowel = 'аеёиоуэюя'
words = input().split()
res = list()

for i in words:
    res.append([j for j in i if j in vowel])    # Списочное выражение

res = (list(map(lambda x: len(x), res)))        # lambda выражение и функция высшего порядка
flag = True
for i in range(1, len(res) - 1):
    if res[0] != res[i]: flag = False

if flag == True: print('Парам пам-пам')
else: print('Пам парам')