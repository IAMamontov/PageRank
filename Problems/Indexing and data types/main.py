import numpy as np

array = np.array([[0, 2, 1998],
                  [12, 0, 1212],
                  [21, 0, 0],
                  [7, 0, 2019]])

x = int(input())
print(array[x].astype(np.bool))