"""
SETS exercise
"""
from sympy import FiniteSet, pi

def exercise(x, y):
    t = 2 * pi * (x/y)**0.5
    return t

x = FiniteSet(10, 18, 2, 220, 22.5, 25)
y = FiniteSet(10, 9.78, 9.83)

print('x * y = ', x * y, '________', 'len(x * y) = ', len(x * y))


id = 0  # ID numerator start value
print('_'*25 + '_'*38 + '_'*25 + '_'* 25)
print('{0:^25}{1:^38}{2:^25}{3:^25}'.format('Parametr A', 'Parametr B', 'Wynik:', 'ID'))
print('_'*25 + '_'*38 + '_'*25 + '_'* 25)

for i in x * y:  # all possibilities
    a = i[0]
    b = i[1]
    c = exercise(a/100, b)
    id += 1
    print('{0:^25}{1:^38}{2:^25.2f}{3:^25}'.format(float(a), float(b), float(c), id))

print('_'*25 + '_'*38 + '_'*25 + '_'* 25)

