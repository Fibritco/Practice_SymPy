"""
SymPy
"""
from sympy import Symbol, expand, symbols, factor, pprint, init_printing

# Exaple 1 - Symbol
print('Example 1')
z = Symbol('z') 
print(z + z + 1)

# Example 2 - checking symbol
print('Example 2')
print(z.name)

# Example 3 - symbols
print('Example 3')
x, y, z, u = symbols('x, y, z, u')
print(4 * x + x + x / y + y - u * 10)

# Example 4 - factor
print('Example 4')
expr = x**3 - y**4 - round(5/89, 2)
factors = factor(expr)
print(factors)
gg = expand(factors)
print(gg)

# Example 5 - pprint
print('Example 5')
pprint(expr)


# Example 6 - init_printing handsome formula printing 
print('Example 6')

def print_in_series(n):
    init_printing(order='rev-lex')
    x = Symbol('x')
    ser = x
    for i in range(2, n + 1):
        ser += (x**i)/i

    pprint(ser)

inpu = input('Podaj liczbę elementów szeregu:')
gh = print_in_series(int(inpu))

# Example 7 - Value substitution 
print('Example 7')
xxx = x*x + 2*y + 20
res = xxx.subs({x:2, y:6})  # subs()
print(res)










