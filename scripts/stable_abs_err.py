import numpy as np
import mpmath
import matplotlib.pyplot as plt

import const
from const import *

EPS = np.finfo(np.float64).eps

def x1_prim(p, q):
    D = p**2 - 4*q
    if D < 0:
        return None
    return -(p + np.sqrt(D)) / 2

def x1_stab(p, q):
    D = p**2 - 4*q
    if D < 0:
        return None
    return -(p + np.sqrt(D)) / 2

def x1_stab_mp(p, q):
    D = p**2 - 4*q
    if D < 0:
        return None
    return -(p + mpmath.sqrt(D)) / 2

q = 1.0

X1 = np.array([x1_prim(p, q) for p in P])
X1_st = np.array([x1_stab(p, q) for p in P])

X1_t = np.array([float(x1_stab_mp(mpmath.mpf(p), mpmath.mpf(q))) for p in P])

err_prim = np.abs(X1 - X1_t)
err_stab = np.abs(X1_st - X1_t)

plt.figure()
plt.xlabel("p")
plt.ylabel("Absoluter Fehler")

plt.loglog(P, err_prim, label="Instabil (float64)")
plt.loglog(P, err_stab, label="Stabil (Vieta, float64)", color="orange")
plt.loglog(P, P*EPS, label="Maschinengenauigkeit mal p", linestyle="--", color="gray")

plt.legend()
plt.tight_layout()
plt.savefig("tmp.2.pdf")

