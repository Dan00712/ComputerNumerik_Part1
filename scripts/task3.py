from decimal import Decimal, getcontext

import numpy as np
import matplotlib.pyplot as plt

import progressbar

N=2000

getcontext().prec = 20
def quadratic_1(p,q):
    D = p**2 - 4*q
    if D <= 0:
        return np.nan
    return -(p + np.sqrt(D))/2


def quadratic_1_dec(p,q):
    D = p**2 - 4*q
    if D <= 0:
        return Decimal('nan')
    return -(p + D.sqrt())/2

# TODO: what values to use in ranges?
P = np.linspace(0, 1, N)
Q = np.linspace(-1, 0, N)

delta = []
for q in progressbar.progressbar(Q):
    sub_delta = []
    for p in P:
        s1 = quadratic_1(p, q)
        s2 = quadratic_1_dec(
                Decimal(p),
                Decimal(q))
        sub_delta.append(Decimal(str(s1)) - s2)
    delta.append(sub_delta)
delta = np.array(delta)
delta = np.array(list(map(np.float64, 
    delta /Decimal(np.finfo(np.float64).eps)
    ))
)

print(f'mean:{np.nanmean(delta)}\nmax:{np.nanmax(delta)}')

delta_ = np.ma.masked_invalid(delta)
# TODO: make plots prettier (change color scheme, add proper axes,...)
plt.imshow(delta_)
plt.savefig('tmp.svg')
