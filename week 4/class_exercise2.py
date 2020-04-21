import numpy as np
a = np.arange(0, 27).reshape((3, 3, 3))

slice1 = a[1, 1, :]
slice2 = a[:, 1, 0]
slice3 = a[0, :, 2]
print(a)
print(slice1)
print(slice2)
print(slice3)
