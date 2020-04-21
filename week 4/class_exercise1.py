import numpy as np

a = np.arange(10, 30).reshape(4, 5)

yellow = a[0, 0]
red = a[0, 1:4]
cyan = a[:, (1, 3)]
blue = a[(0, 2), -1]
green = a[0:3, 2]
print("yellow\n", yellow)
print("red\n", red)
print("cyan\n", cyan)
print("blue\n", blue)
print("green\n", green)
