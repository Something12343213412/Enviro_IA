import matplotlib.pyplot as plt
import numpy as np
from data.non_disruption.Data_Management import save_entity, load_data
from graphing_misc import graph_data, graph_datasets
from Point_Calculations import update, get_pred, get_hare, get_browse, cause_disruption_hare, empty_array

def calculate_difference(arr1, arr2):
    diff = []
    for c in range(0, len(arr1)-1):
        diff.append(arr1[c]/arr2[c])
        if (diff[c] < .95 or diff[c] > 1.05) and c*dt > .65:
            print(f"% is {diff[c]} at {c*dt - .65}")

    return diff


if __name__ == '__main__':
    num = 1200
    end_point = 10
    dt = end_point/num
    x = np.linspace(0, end_point, num)

    cause_disruption_hare(0.4, .05, 0, .1, 5, .12, dt, num)
    #for b in x:
        #update(dt)

    save_entity("data/disruption/browse_s", get_browse())
    save_entity("data/disruption/hare_s", get_hare())
    save_entity("data/disruption/pred_s", get_pred())

    #empty_array()
    #for b in x:
        #update(dt)

    #save_entity("data/non_disruption/browse_s", get_browse())
    #save_entity("data/non_disruption/hare_s", get_hare())
    #save_entity("data/non_disruption/pred_s", get_pred())

    browse_data = [load_data("data/disruption/browse_s"), load_data(
        "data/non_disruption/browse_s")]
    hare_data = [load_data("data/disruption/hare_s"), load_data("data/non_disruption/hare_s")]
    predator_data = [load_data("data/disruption/pred_s"), load_data(
        "data/non_disruption/pred_s")]

    #graph_data(load_data("data/disruption/browse_s"), dt, "browse vs time")
    #graph_data(load_data("data/disruption/hare_s"), dt, "hare vs time")
    #graph_data(load_data("data/disruption/pred_s"), dt, "predator vs time")

    graph_datasets(browse_data, dt, "Browse d + Browse non d vs Time", ["r", "b"], ["d", "non_d"])
    graph_datasets(hare_data, dt, "Hare vs time", ["r", "b"], ["d", "non_d"])
    graph_datasets(predator_data, dt, "Predator vs time", ["r", "b"], ["d", "non_d"])

    graph_data(calculate_difference(predator_data[0], predator_data[1]), dt, "% diff pred")
    graph_data(calculate_difference(hare_data[0], hare_data[1]), dt, "% diff hare")
    graph_data(calculate_difference(browse_data[0], browse_data[1]), dt, "% diff browse baseline")

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

