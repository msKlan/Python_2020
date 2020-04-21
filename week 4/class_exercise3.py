import numpy as np
a = np.arange(1, 101).reshape(10, 10)

even = a[a % 2 == 0]
ends6 = a[np.where(a % 10 == 6)]
div3orstart8 = a[np.where((a % 3 == 0) | (a == 8) | ((a >= 80) & (a <= 89)))]


print('even:\n', even, '\nends6:\n', ends6, '\ndiv3orstart8:\n', div3orstart8)
