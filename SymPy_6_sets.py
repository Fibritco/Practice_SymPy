"""
SETS
"""

from sympy import FiniteSet

print('Zadanie 1 _____________________')
a = FiniteSet(1, 2, 3)
b = FiniteSet(3, 4, 5)
print(a.union(b))           # wszystkie czści wspólne
print(a.intersect(b))       # tylko wspólny element

print('Zadanie 2 _____________________')
c = FiniteSet(1, 2, 3)
d = FiniteSet(3, 4, 5)
e = FiniteSet(3, 8, 5)
print(c.union(d).union(e))

print('Zadanie 3 _____________________')
x = a*b
print(x)      # iloczyn karteziański
for i in x:   # przejrzenie iloczynu karteziańskiego (zbiór wszystkich możliwych par)
    print(i)

print(len(x) == len(a) * len(b))

print('Zadanie 4 _____________________')
y = a**4      # jeżeli ** to wtedy 4 x iloczyn karteziański
print(y)      # iloczyn karteziański
for i in y:   # przejrzenie iloczynu karteziańskiego (zbiór wszystkich możliwych par)
    print(i)

print(len(x) == len(a) ** 4)
