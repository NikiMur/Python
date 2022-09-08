#Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.



X = input()
Y = input()
Z = input()
left = not(X or Y or Z)  
right = (not X) and  (not Y) and (not Z)
print(left == right)
