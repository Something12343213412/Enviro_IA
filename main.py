import matplotlib.pyplot as plt
import numpy as np
import math
from Prey import Prey
from Plants import Plants
from Predator import Predator
import GlobalVariables
from Data_Management import save_entity, load_data
from graphing_misc import graph_data, graph_datasets

browse = Plants(10000, 1.1, 2*math.pow(10, 5), 700, 1, .7)
hare = Prey(100, 1.2, 1.8, .98, 2 * math.pow(10, 4))
predators = Predator(.1, 1.2, 600, 90, .9)

browse_array = []
hare_array = []
predator_array = []

# move into a misc func later
def empty_array():
    global browse_array, hare_array, predator_array
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
    num = 1200
    end_point = 60
    dt = end_point/num
    #x = np.linspace(0, end_point, num)
    #for b in x:
        #update(dt, b)
    # save seasonal data
    #save_entity("data/browse_seasonal", browse_array)
    #save_entity("data/hare_seasonal", hare_array)
    #save_entity("data/predator_seasonal", predator_array)

    #save_entity("data/browse_non_seasonal", browse_array)
    #save_entity("data/hare_non_seasonal", hare_array)
    #save_entity("data/predator_non_seasonal", predator_array)

    browse_data = [load_data("data/browse_seasonal"), load_data("data/browse_non_seasonal")]
    hare_data = [load_data("data/hare_seasonal"), load_data("data/hare_non_seasonal")]
    predator_data = [load_data("data/predator_seasonal"), load_data("data/predator_non_seasonal")]

    graph_datasets(browse_data, dt, "Browse wave + Browse vs Time", ["r", "b"], ["seasonal", "not seasonal"])
    graph_datasets(hare_data, dt, "Hare vs time", ["r", "b"], ["seasonal", "not seasonal"])
    graph_datasets(predator_data, dt, "Predator vs time", ["r", "b"], ["seasonal", "not seasonal"])


    """
    fig, axs = plt.subplots(1, 3)
    axs[0].set_title("Browse vs Time, years \n vs Hare vs Time")
    axs[0].plot(x, browse_array)

    axs[1].set_title("Hare vs Time, years")
    axs[1].plot(x, hare_array)

    axs[2].set_title("Predator vs Time, years")
    axs[2].plot(x, predator_array)
    """

    plt.legend()
    plt.show()

