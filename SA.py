import random

import matplotlib.pyplot as plt
import numpy as np


def simulated_annealing(init_x, neighborhood, init_temp, temp_variation, iterations, graphs):
    def f(x):
        # f(x)=sin(0.15*x)+cos(x)
        # 0 <= x <= 40
        return np.sin(0.15 * x) + np.cos(x)

    def neighbor_acceptance(x):  # Calculates the neighbor value and decide if accept it or not
        r_acceptance = random.random()  # Random value behind 0 and 1 for acceptance

        left = x - (x * neighborhood)  # Alpha percent of left
        right = x + ((40 - x) * neighborhood)  # Alpha percent of right

        neighbor_x = random.uniform(left, right)  # Random value behind neighborhood range

        cost = abs(f(neighbor_x) - f(x))  # Cost. Abs of difference between energies

        if f(neighbor_x) > f(x):  # Accept new value (it's better)
            return [1, neighbor_x]
        elif np.exp(-cost / temp) > r_acceptance:  # Random accepting worst new value
            return [1, neighbor_x]
        else:
            return [0, x]  # Not accepted new value

    def print_graphs():
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
        plt.title("f(x)=sin(0.15*x)+cos(x)")
        plt.ylabel("f(x)")
        plt.xlabel("x")
        for l, m in steps.items():
            plt.plot(t1, f(t1), 'b', m, f(m), 'rx', linewidth=0.5)
        plt.grid(True)

        plt.show()

    steps = dict()  # Movements to achieve optimization
    step_iteration = 0
    temp_graph = []

    # Initialize values and do iterations
    x_value = init_x
    temp = init_temp
    for i in range(iterations):  # Iterations for optimization

        n_acceptance = neighbor_acceptance(x_value)
        accepted = n_acceptance[0]
        new_x = n_acceptance[1]

        if accepted:
            x_value = new_x
            steps[step_iteration] = x_value
            step_iteration = step_iteration + 1
        temp = temp * temp_variation
        temp_graph.append(temp)

    # Calculates final max and its iteration
    maximum = 0
    for k, v in steps.items():
        if f(v) > f(maximum):
            maximum = v

    if graphs:
        print_graphs()

    absolute = 0
    if f(maximum) > 1.81:
        absolute = 1

    return absolute


def print_results():
    print("\n--------------- ITERATIONS =", test_iterations, "------------------------------------------------\n")

    max = 0
    plt.figure(1)
    for k, v in initial_temperature_p.items():
        if v > max:
            max = v
            key = k
    print("initial_temperature =", key, "num of absolute maximums =", max)
    print("\t", max / test_iterations * 100, "%")

    max = 0
    for k, v in initial_x_p.items():
        if v > max:
            max = v
            key = k
    print("initial_x =", key, "num of absolute maximums =", max)
    print("\t", max / test_iterations * 100, "%")

    max = 0
    for k, v in neigh_p.items():
        if v > max:
            max = v
            key = k
    print("neigh =", key, "num of absolute maximums =", max)
    print("\t", max / test_iterations * 100, "%")

    max = 0
    for k, v in var_p.items():
        if v > max:
            max = v
            key = k
    print("var =", key, "num of absolute maximums =", max)
    print("\t", max / test_iterations * 100, "%")


# init_x - Initial X value
# neighborhood - Alpha
# init_temp - Start temperature
# temp_variation - Beta
# iterations - Number of iterations
# graphs - Display graph or not 1,0
initial_temperature_p = dict()
var_p = dict()
neigh_p = dict()
initial_x_p = dict()

for times in [1, 2, 3]:
    test_iterations = 0
    for initial_temperature in range(100, 1000, 100):
        if not initial_temperature_p.get(initial_temperature):
            initial_temperature_p[initial_temperature] = 0
        for var in np.arange(0.9, 1.0, 0.01):
            if not var_p.get(var):
                var_p[var] = 0
            for neigh in np.arange(0.0, 1.0, 0.1):
                if not neigh_p.get(neigh):
                    neigh_p[neigh] = 0.0
                for initial_x in np.arange(0, 40, 1):
                    if not initial_x_p.get(initial_x):
                        initial_x_p[initial_x] = 0
                    it = simulated_annealing(init_x=initial_x, neighborhood=neigh, init_temp=initial_temperature,
                                             temp_variation=var,
                                             iterations=1000,
                                             graphs=0)
                    if it:
                        initial_temperature_p[initial_temperature] += 1
                        var_p[var] += 1
                        neigh_p[neigh] += 1
                        initial_x_p[initial_x] += 1
                    test_iterations += 1
    print_results()
