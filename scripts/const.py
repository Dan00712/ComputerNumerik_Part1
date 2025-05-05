import numpy as np
from mpmath import mp

DTYPE=np.float64
EPS = np.finfo(DTYPE).eps

START=1
STOP=7.9
N = 500
P = np.logspace(START, STOP, N)

mp.dps = 34 # approximate float128, which has a eps of ~1E-34

