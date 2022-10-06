def same_by(operation, object):
    counter = 0
    for i in object:
        if operation(i) == True:
            counter += 1
    if counter == len(object): return True
    else: return False

values = [int(i) for i in input().split()]
if same_by(lambda x: x % 2 == 0, values): print('same')
else: print('different')
