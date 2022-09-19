
num = int(input("¬ведите число, а € выведу его простые множители "))
i = 2
while i <= num: 
    if num % i == 0:
        print(i, end = " ")
        num //= i
        i = 1
    i += 1