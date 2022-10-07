"""
SETS probability  - matplotlib_venn
"""

from sympy import FiniteSet
import matplotlib.pyplot as plt
from matplotlib_venn import venn2

def probability(s, e):
    return len(e) / len(s)

s = FiniteSet(*range(1, 100))
e = FiniteSet(2, 4, 6, 8, 50)
f = FiniteSet(3, 4, 6, 8, 5)

p1 = probability(s, e)
print(f'Probability to find numbers from {e} in {s} is =', round(p1, 3), '💫')

g = e.union(f)  # as a set it delete all repetition 

p2 = probability(s, g)
print(f'Probability to find numbers from {g} in {s} is =', round(p2, 3), '💫')

venn2(subsets=(g, s), set_labels=('G', 'S'))  # drawing two sets in one diagram (only two)
plt.show()
