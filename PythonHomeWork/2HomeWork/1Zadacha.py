import random

print()
vibor = int(input("введите 1 если хотите рандомное число монеток или 2 если хотите указать их число "))
if vibor == 1:
    num = random.randint(1,10)
    print(f"монеток {num} выпало  ")
elif vibor == 2:
    num = int(input("Введите число монеток: "))    
else: 
    print(f"ах так тогда получай столько монет сколько ввел {vibor}  ")
    num = vibor
   

count = 0
print()

for i in range(num):
    x = random.randint(0, 2)
    if x == 0: count += 1

if count < num / 2: print(f"Необходимо перевернуть {count} монеток с гербом")
elif count == num / 2: print(f"Необходимо перевернуть {count} монеток либо с гербом, либо с решкой")
else: print(f"Необходимо перевернуть {num - count} монеток с решкой")
