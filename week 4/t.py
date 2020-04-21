# import numpy as np
# import matplotlib.pyplot as plt

# xs = np.linspace(0, 2 * np.pi, 50)
# ys = np.sin(xs)

# mask = ys >= 0                        # condition for the blue crosses

# print(ys[mask])

# # rendering the blue plots only with filtered values
# plt.plot(xs[mask], ys[mask], 'bx')
# mask = (ys < 0)                       # condition for the green dots
# # condition applied to xs and ys data sets
# plt.plot(xs[mask]+1, ys[mask], 'go')
# plt.show()


# a = np.arange(0, 100, 10)
# c = a[a >= 50]
# print(a, type(a))
# print(c, type(c))

import keras
import tensorflow
import theano
import sklearn
import statsmodels
import pandas
import matplotlib
import numpy
import scipy
print('scipy: %s' % scipy.__version__)
# numpy
print('numpy: %s' % numpy.__version__)
# matplotlib
print('matplotlib: %s' % matplotlib.__version__)
# pandas
print('pandas: %s' % pandas.__version__)
# statsmodels
print('statsmodels: %s' % statsmodels.__version__)
# scikit-learn
print('sklearn: %s' % sklearn.__version__)


print("deep learning libraries installed:\n")
# theano
print('theano: %s' % theano.__version__)
# tensorflow
print('tensorflow: %s' % tensorflow.__version__)
# keras
print('keras: %s' % keras.__version__)
