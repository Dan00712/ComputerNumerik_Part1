import numpy as np
from mpmath import mp

import matplotlib.pyplot as plt

DTYPE=np.float64
EPS = np.finfo(DTYPE).eps
mp.dps = 34 # approximate float128, which has a eps of ~1E-34

def root(p, q, dtype=DTYPE):
    p, q = dtype(p), dtype(q)
    D = p**2 - 4*q
    if D <= 0:
        return DTYPE('nan')
    return (-p + np.sqrt(D))/2

def stable_root(p, q):
    p, q = DTYPE(p), DTYPE(q)
    D = p**2 - 4*q
    if D <= 0:
        return DTYPE('nan')
    s = np.sign(p) if p != 0 else 1.0
    x1 = -(p + s*np.sqrt(D))/2  # stable version
                                # in this case s = +1
    x2 = q/x1                   # x2 is numerically unstable in unstable root
    return x2

def true_root(p, q):
    return root(p, q, dtype=mp.mpf)

P = np.logspace(-2, 16, 800)
q = 1.0
rel_err_u = []
rel_err_s = []

for p in P:
    x_t = mp.mpf(true_root(p, q))

    x_u = mp.mpf(root(p, q))
    err_u = abs((x_t - x_u)/x_t)
    rel_err_u.append(err_u)

    x_s = mp.mpf(stable_root(p, q))
    err_s = abs((x_t - x_s)/x_t)
    rel_err_s.append(err_s)

plt.figure(figsize=(10,6))
plt.loglog(P, rel_err_u, label="Instabil (float64)", lw=2)
plt.loglog(P, rel_err_s, label="Stabil (Vieta, float64)", lw=2)
plt.axhline(y=EPS, color='gray', linestyle='--', label="Maschinengenauigkeit (float64)")
plt.xlabel(r"$p$")
plt.ylabel("Relativer Fehler")
#plt.title("Numerische Stabilität: Instabile vs. stabile Berechnung der Nullstelle")
plt.legend()
plt.grid(True, which="both", ls=":")
plt.tight_layout()
plt.savefig('task3-istabil.pdf')
