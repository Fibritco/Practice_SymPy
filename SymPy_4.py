"""
SymPy practice - solve()
"""

from sympy import Symbol, solve, pprint

x = Symbol('x')
ex1 = x - 10 - 120  # 0 = x - 10 - 120
s1 = solve(ex1)
print(s1)   # x = 130
print()

ex2 = x**3 + 4*x + 4
s2 = solve(ex2, dict=True) # 
print(s2) 
print(len(s2)) # numbers of formulas 
pprint(s2)  # print as a mathematical formula