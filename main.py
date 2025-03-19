import matplotlib.pyplot as plt
import numpy as np
import math

def find_pos_lim(point, dx=math.pow(10, -4), func=lambda x: x*x):
    return func(point+dx)

def find_neg_lim(point, dx=math.pow(10, -4), func=lambda x: x*x):
    return func(point-dx)


def approximate_derivative(point, dx=math.pow(10, -4), accepted_range=.001, func=lambda x: x**2):
    lims = [find_pos_lim(point, dx, func), find_neg_lim(point, dx, func)]
    if not -accepted_range < lims[0]-lims[1] < accepted_range:
        print(f"lims not = at {point}")
        return -1
    else:
        derivative = (lims[0] - lims[1])/(2*dx)
        return derivative

def simulate_planet_1d(initial_pos: float, time_interval: (float, float) = (0, 5), c: float = 1, dt=.01):

    number_points = round((time_interval[1] - time_interval[0])/dt)
    time_positions = np.linspace(time_interval[0], time_interval[1], number_points)

    # collection of 3d points, first index is position 2nd is velocity, 3rd is accel
    positions = [initial_pos]
    velocities = [0]
    accelerations = [0]

    # declaring this for readability but also so we don't have forty billion .length calls
    last_index = [initial_pos, 0, 0]

    def find_accel_gravity():
        return c/math.pow(last_index[0], 2)

    # make more efficient, i never used so feels weird to define for loop like this
    for i in range(0, number_points-1):
        #print(-math.copysign(1, last_index[0]))
        last_index[2] = -math.copysign(1, last_index[0]) * find_accel_gravity()
        last_index[1] += last_index[2]*dt
        last_index[0] += last_index[1]*dt
        positions.append(last_index[0])
        velocities.append(last_index[1])
        accelerations.append(last_index[2])
        #print(last_index)

    return time_positions, positions, velocities, accelerations


if __name__ == '__main__':
    x = np.linspace(0, 10, 1000)

    def func(i):
        return math.sin(i**2)

    array_derivative = np.vectorize(lambda i: approximate_derivative(i, dx=.0000001, func=func))
    base_func = np.vectorize(func)

    y2 = array_derivative(x)
    y1 = base_func(x)

    #fig, _ = plt.subplots()
    _, ax2 = plt.subplots()
    #_, ax3 = plt.subplots()
    #_, ax4 = plt.subplots()

    x3, y3, y4, y5 = simulate_planet_1d(10, (0, 15), c=90, dt=.0000001)

    #ax.plot(x, y1)
    #ax.plot(x, y2)
    ax2.plot(x3, y3)
    #ax3.plot(x3, y4)
    #ax4.plot(x3, y5)

    plt.show()

