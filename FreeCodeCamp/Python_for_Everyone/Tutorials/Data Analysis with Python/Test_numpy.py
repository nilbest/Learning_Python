import numpy as np

a = np.ones((5,5), dtype=int)
b = np.zeros((3,3), dtype=int)
b [1,1] = 9
a[1:-1,1:-1] = b

print(a)
print(b)

