import matplotlib.pyplot as plt
import numpy as np
import math
from Prey import Prey
from Plants import Plants
from Predator import Predator
import GlobalVariables

browse = Plants(10000, 1.1, 2*math.pow(10, 5), 700, 1, .7)
hare = Prey(100, 1.2, 1.8, .98, 2 * math.pow(10, 4))
predators = Predator(.1, 1.2, 600, 90, .9)

browse_array = []
hare_array = []
predator_array = []

def update(time_interval, b):
    b = round(b/time_interval)

    GlobalVariables.time += time_interval
    plant_der = browse.plant_derivative(hare) * time_interval
    hare_der = hare.prey_derivative(browse, predators) * time_interval
    pred_der = predators.find_predator_derivative(hare) * time_interval
    browse.density += plant_der
    hare.density += hare_der
    predators.density += pred_der

    print(f" {hare_der} at {GlobalVariables.time}")

    try:

        browse_array.append(browse.density)
        hare_array.append(hare.density)
        predator_array.append(predators.density)

        #browse_array.append(plant_der)
        #hare_array.append(hare_der)
        #predator_array.append(pred_der)
        #hare_array[b] = hare.prey_derivative(browse, predators)
        #predator_array[b] = predators.find_predator_derivative(hare)

    except:
        pass

if __name__ == '__main__':
    # 10000 is arbitary start value

    #x = np.linspace(0, 10, 1000)

    num = 4000
    end_point = 120
    x = np.linspace(0, end_point, num)

    for b in x:
        update(end_point/num, b)


    fig, axs = plt.subplots(1, 1)
    axs.set_title("Browse vs Time, years")
    axs.plot(x, browse_array)
    _, ax = plt.subplots(1, 1)
    ax.set_title("Hare vs Time, years")
    ax.plot(x, hare_array)
    _, ax2 = plt.subplots(1, 1)
    ax2.set_title("Predator vs Time, years")
    ax2.plot(x, predator_array)
    """
    fig, axs = plt.subplots(1, 3)
    axs[0].set_title("Browse vs Time, years \n vs Hare vs Time")
    axs[0].plot(x, browse_array)

    axs[1].set_title("Hare vs Time, years")
    axs[1].plot(x, hare_array)

    axs[2].set_title("Predator vs Time, years")
    axs[2].plot(x, predator_array)
    """

    plt.show()

