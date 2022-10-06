"""
micro program with SymPy - data from user
"""

from sympy import expand, sympify
from sympy.core.sympify import SympifyError
import time

def formula_1(x, y):
    res = expand(x * y)
    print(res)


if __name__ == '__main__':
    x = input('Please give first formula:')
    y = input('Please give second formula:')
    try:
        x = sympify(x)
        y = sympify(y)
    except SympifyError:
        print('Incorrect input data')
    else:
        formula_1(x, y)

    time.sleep(3)


