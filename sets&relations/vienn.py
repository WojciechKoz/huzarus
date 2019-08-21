import numpy as np
import matplotlib.pyplot as plt
from vienn_managers import DoubleManager, TripleManager


def plot_regions(manager, sets, names):
    """ draws vienn diagram using matplotlib library and given manager """

    manager.draw_circles() # draws representations of sets (big circles)

    plt.xticks([]) # hides axis numbers
    plt.yticks([])

    points = manager.slots() # split sets e.g. (A, B) -> (A-B, AB, B-A)

    for idx, cluster in enumerate(points):
        # draws elements in diagram
        plt.scatter(cluster[:, 0], cluster[:, 1], s=manager.size, c=manager.colors[idx], marker='s')
        # prints name of each element
        for (x, y), value in zip(cluster, manager.subsets(idx)):
            plt.annotate(value, (x, y), ha='center', va='center', c='white')

    plt.title('Vienn diagram')
    manager.write_sets_names(names)  # prints name of each set
    plt.gca().set_aspect('equal', adjustable='box')  # keeps square shape of diagram
    # plt.axis('scaled')
    plt.show()


def vienn(*sets, names=None):
    """ runs plot_regions with some manager depends on sets amount """
    if len(sets) == 2:
        names = ['A', 'B'] if not names else names
        plot_regions(DoubleManager(*sets), sets, names)
    elif len(sets) == 3:
        names = ['A', 'B', 'C'] if not names else names
        plot_regions(TripleManager(*sets), sets, names)
    else:
        raise ValueError('wrong number of sets')
