import numpy as np
a1 = int(input())
a2 = int(input())
a3 = int(input())
a4 = int(input())
a5 = int(input())
a6 = int(input())
arr1 = np.array([[a1, a2], [a3, a4]])
arr2 = np.array([a5, a6])
print(arr1 @ arr2)