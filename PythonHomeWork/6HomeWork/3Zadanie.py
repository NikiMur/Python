from math import pi


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]

def find_farthest_orbit(x):
    mult = list(pi * i[0] * i[1] for i in x if i[0] != i[1]) # списочное выражение
    for i in x:
        if i[0] * i[1] * pi == max(mult):
            return i

print(*find_farthest_orbit(orbits))