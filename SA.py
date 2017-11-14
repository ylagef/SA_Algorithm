import random

import matplotlib.pyplot as plt
import numpy as np


# f(x)=sin(0.15*x)+cos(x)
# 0 <= x <= 40

def f(x):
    return np.sin(0.15 * x) + np.cos(x)


def neighbor_acceptance(x_value):
    r_acceptance = random.random()  # Random value from 0 to 1
    r_neighborhood = random.uniform(-1, 1)  # Random value from -1 to 1
    neighbor_x = (x_value + ((40 - x_value) * neighborhood) * r_neighborhood)  # TODO MAL

    cost = f(neighbor_x) - f(x_value)

    if f(neighbor_x) > f(x_value):
        print("NEW BEST")
        return [1, neighbor_x]
    elif 1 / (1 + np.exp(cost / temp)) > r_acceptance:
        print("ACCEPTED")
        return [1, neighbor_x]
    else:
        print("AS WAS")
        return [0, x_value]


steps = dict()  # Movements to achieve optimization
x_value = 5  # Initial X value
neighborhood = 0.1
temp = 200

step_iteration = 0

for i in range(100):  # Iterations for optimization
    accept = neighbor_acceptance(x_value)[0]
    new_x = neighbor_acceptance(x_value)[1]

    if accept:
        x_value = new_x
        steps[step_iteration] = x_value
        step_iteration = step_iteration + 1

# Print f(x) and x with steps
t1 = np.arange(0.0, 40.0, 0.1)
for k, v in steps.items():
    plt.plot(t1, f(t1), 'b', steps[k], f(steps[k]), 'rx')
plt.show()
