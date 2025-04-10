import matplotlib.pyplot as plt
import numpy as np

# takes data, the time interval, and title of the graph and then creates a graph
def graph_data(data, dt, title):
    endpoint = dt * len(data)
    x = np.linspace(0, endpoint, len(data))

    fig, axs = plt.subplots(1, 1)
    axs.set_title(title)
    axs.plot(x, data)

# graphs multiple different graphs on same plot
def graph_datasets(data, dt, title, colors=None, labels=None):
    if labels is None:
        labels = ["1", "2"]
    if colors is None:
        colors = ["red", "blue"]
    endpoint = dt * len(data)
    x = np.linspace(0, endpoint, len(data[0]))

    fig, axs = plt.subplots(1, 1)
    axs.set_title(title)

    for b in range(0, len(data)):
        axs.plot(x, data[b], color=colors[b], label=labels[b])
    plt.legend()
