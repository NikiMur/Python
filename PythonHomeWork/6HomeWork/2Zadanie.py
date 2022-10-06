values = [i for i in input().split()]
transformation = lambda x: x    # lambda функция
transformation_values = list(map(transformation, values))
if values == transformation_values: print('ok')
else: print('fail')