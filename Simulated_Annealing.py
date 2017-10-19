import math
import matplotlib.pyplot as plt
from matplotlib.mlab import frange

# f(x)=sin(0.15*x)+cos(x)
# 0 <= x <= 40

f = []
x = []
for i in frange(0, 40, 0.0001):
    x.append(i)
    f.append(math.sin(0.15 * i) + math.cos(i))
plt.plot(x, f)
# plt.show()


