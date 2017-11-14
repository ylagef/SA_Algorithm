import matplotlib.pyplot as plt
import numpy as np


# f(x)=sin(0.15*x)+cos(x)
# 0 <= x <= 40

def f(x):
    return np.sin(0.15 * x) + np.cos(x)


t1 = np.arange(0.0, 40.0, 0.1)
plt.plot(t1, f(t1))
plt.show()
