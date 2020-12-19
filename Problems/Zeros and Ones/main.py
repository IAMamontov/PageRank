import numpy as np
n = int(input())
d = int(input())
if d == 1:
    a = np.ones((n, n))
elif d == 0:
    a = np.zeros((n, n))
print(a)
