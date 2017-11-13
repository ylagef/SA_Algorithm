import math
import matplotlib.pyplot as plt
import random
from matplotlib.mlab import frange


# f(x)=sin(0.15*x)+cos(x)
# 0 <= x <= 40

def f(x):
    return math.sin(0.15 * x) + math.cos(x)


values = dict()
for i in frange(0, 40, 0.001):
    values[i] = f(i)

# for k, v in values.items():
# plt.plot(k, v)
# plt.show()

initX = 5
neighborhood = 0.1
temp = 200


def neighborY(actualX):
    rAcceptance = random.random()
    rNeighborhood = random.uniform(-1, 1)

    neighborX = (actualX + ((40 - actualX) * neighborhood) * rNeighborhood)
    neighbor = f(neighborX)

    cost = neighbor - f(actualX)
    print("\nActualX=", actualX, "ActualY=", f(actualX), "NeighX=", neighborX, "NeighY=", neighbor)
    print("Cost=", cost, "Result=", 1 / (1 + math.exp(cost / temp)))
    if (neighbor > f(actualX)):
        print("NEW BEST")
        return [neighborX, neighbor]
    elif (1 / (1 + math.exp(cost / temp)) > rAcceptance):
        print("ACCEPTED")
        return [neighborX, neighbor]
    else:
        print("AS WAS")
        return [actualX, f(actualX)]


for i in range(1000):
    print(initX, f(initX))
    initX = neighborY(initX)[0]
    temp = temp * 0.9
