"""
SumPy  - formulas solvation 
"""


from sympy import symbols, solve, pprint, Symbol, plot

"""
x, a, t, c, y = symbols('x, a, t, c, y')
eq = a*t + (1/2)*a*t - c
t_eq = solve(eq, t, dict=True)
pprint(t_eq)
"""

print()
# _____________linear algebra_______________________________
print(' _____________linear algebra_______________________________')
x = Symbol('x')
y = Symbol('y')
eq_1 = 2*x + 2*y - 6  # equation 1
print(f'eq_1 = {eq_1}')
eq_2 = 3*x + y - 12   # equation 2
print(f'eq_2 = {eq_2}')
print()
eq_1_2 = solve((eq_1, eq_2), dict=True)  # solving eq1 vs eq2 - remember about brackets between eq_1 and eq_2 !!!!!!!!!!!!!!
print('eq_1 == eq_2 solution:')
pprint(eq_1_2)
print()

# checking correctness 
solv_1 = eq_1_2[0]

print('x =', solv_1[x])
print('y =', solv_1[y])
solv_ = eq_1.subs({x:solv_1[x], y:solv_1[y]})
print(f"Solution of the equation 0 = {eq_1} with x = {solv_1[x]} and y = {solv_1[y]} is equal :", solv_)
print()

print('x =', solv_1[x])
print('y =', solv_1[y])
solv__ = eq_2.subs({x:solv_1[x], y:solv_1[y]})
print(f"Solution of the equation 0 = {eq_2} with x = {solv_1[x]} and y = {solv_1[y]} is equal :", solv__)


# plotin eq_1 and eq_2
yy = solve(eq_1, y)
print(yy)
xx = solve(eq_2, y)
print(xx)
p = plot(xx[0], yy[0], (x, -2.4, 7), title='eq_1 and eq_2', xlabel= 'x', ylabel='y', legend=True)

# saving plot as a picture
p.save('eq_1 vs eq_2.png')
