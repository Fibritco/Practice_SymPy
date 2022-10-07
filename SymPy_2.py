"""
SymPy
"""


from sympy import sympify
from sympy.core.sympify import SympifyError
# Example 1 - sympify  (data from user)
print('Example 1')
ex = input('Podaj równanie:')
print(ex)
ex = sympify(ex)
print(ex)

# Example 2 - sympify  (data from user - Error in formula)
print('Example 2')
ex = input('Podaj równanie:')

try:
    ex = sympify(ex)  
except SympifyError:   # SympifyError
    print('Błąd w formule.')