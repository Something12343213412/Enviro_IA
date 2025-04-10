import matplotlib.pyplot as plt
import numpy as np
import math
from Prey import Prey
from Plants import Plants
from Predator import Predator
import GlobalVariables
from Data_Management import save_entity, load_data

browse = Plants(10000, 1.1, 2*math.pow(10, 5), 700, 1, .7)
hare = Prey(100, 1.2, 1.8, .98, 2 * math.pow(10, 4))
predators = Predator(.1, 1.2, 600, 90, .9)

browse_array = []
hare_array = []
predator_array = []

# makes one specific text input into an array
def make_array(line: str):
    # makes into an array
    line = line.split(",")
    # remove first bracket
    line[0] = line[0].lstrip("[")
    # loop through each removing unnecessary space at beginning
    for d in range(0, len(line) - 1):
        line[d] = line[d].lstrip(" ")
    return line

def load_file():
    file = open("data.txt", "r")
    # puts the 3 lines as strings into an array ** could cause issues of array not being enough to hold all memory
    data = [file.readline(), file.readline(), file.readline()]
    return make_array(data[0]), make_array(data[1]), make_array(data[2])

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
    x = np.linspace(0, end_point, num)

    for b in x:
        update(end_point/num, b)

    #print(file.read())
    #file.write(f"{browse_array}\n{hare_array}\n{predator_array}")

    # loops through browse array saving each datapoint as a new line

    save_entity("data/browse_data", browse_array)
    save_entity("data/hare_data", hare_array)
    save_entity("data/predator_data", predator_array)

    print(load_data("data/browse_data"))
    print(len(load_data("data/browse_data")))

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

