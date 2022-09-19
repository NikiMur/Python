import random

k = 3
poly_length = random.randint(1,3)
sign = ['+', '-']
if poly_length == 1:
    print(f"{random.randint(1,100)}*x**{k} = 0")
elif poly_length == 2:
    print(f"{random.randint(1,100)} {random.choice(sign)} x**{k} = 0")
else:
    print(f"{random.randint(1,100)} {random.choice(sign)} {random.randint(1,100)}*x**{k} {random.choice(sign)} {random.randint(1,100)}*x = 0")

