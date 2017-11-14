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

    # This is for fix the out-range while calculating neighbor X
    if x_value > 20:
        max_value = 40 - x_value
    else:
        max_value = x_value

    neighbor_x = x_value + (neighborhood * r_neighborhood)
    if neighbor_x < 0:
        neighbor_x = x_value + (neighborhood * abs(r_neighborhood))
    elif neighbor_x > 40:
        neighbor_x = x_value + (neighborhood * -abs(r_neighborhood))

    print("X=", x_value, "Nx=", neighbor_x)
    print("f(x)=", f(x_value), "f(Nx)=", f(neighbor_x))
    cost = abs(f(neighbor_x) - f(x_value))  # Absolute value
    print("Cost=", cost)
    print("-------------------------------------------")
    if f(neighbor_x) > f(x_value):
        # print("NEW BEST ", f(neighbor_x))
        return [1, neighbor_x]
    elif np.exp(-cost / temp) > r_acceptance:  # TODO ¿Es esta la función?
        # print("ACCEPTED", f(neighbor_x))
        return [1, neighbor_x]
    else:
        # print("AS WAS", f(x_value))
        return [0, x_value]


x_value = 5  # Initial X value
neighborhood = 1  # Alpha
temp = 100  # Start temperature
temp_variation = 0.95  # Beta

steps = dict()  # Movements to achieve optimization
temp_graph = []
step_iteration = 0

for i in range(1000):  # Iterations for optimization
    accept = neighbor_acceptance(x_value)[0]
    new_x = neighbor_acceptance(x_value)[1]

    if accept:
        x_value = new_x
        steps[step_iteration] = x_value
        step_iteration = step_iteration + 1
    temp = temp * temp_variation
    temp_graph.append(temp)

plt.figure(1)
# Print temp graph
plt.subplot(211)
plt.title("Temperature")
plt.ylabel("Temp (ºK)")
plt.xlabel("Iteration")
plt.plot(temp_graph, 'r', linewidth=0.5)
plt.grid(True)

# Print f(x) and x with steps
t1 = np.arange(0.0, 40.0, 0.1)
plt.subplot(212)
# plt.title("f(x)=sin(0.15*x)+cos(x)")
plt.ylabel("f(x)")
plt.xlabel("x")
for k, v in steps.items():
    plt.plot(t1, f(t1), 'b', v, f(v), 'rx', linewidth=0.5)
plt.grid(True)

plt.show()
