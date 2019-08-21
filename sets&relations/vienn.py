import numpy as np
import matplotlib.pyplot as plt
from vienn_managers import Double_manager, Triple_manager


def plot_regions_with_elements(manager, sets, names):
    ''' draws vienn diagram using matplotlib library and given manager '''

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
    manager.write_sets_names(names) # prints name of each set
    plt.gca().set_aspect('equal', adjustable='box') # keeps square shape of diagram
    # plt.axis('scaled')
    plt.show()


def plot_decision_regions(manager, resolution=0.01):
    if resolution <= 0:
        raise ValueError("Resolution has to be positive number")

    colors = ('grey', 'blue', 'yellow')

    x_min, x_max = -0.5, 0.5
    y_min, y_max = -0.5, 0.5

    # creates two matrixes of the range between min and max on each axis
    # vertical = [[min, min+resolution, min+2*resolution ...],
    #             [min, min+resolution, min+2*resolution ...], ...]
    # horizontal = [[min, min, min, ...],
    #               [min+resolution, min+resolution, ...]...]
    # then flattens it by ravel function and makes new array from them
    # that array is cartesian product of x and y axis with given resolution
    vertical, horizontal = np.meshgrid(np.arange(x_min, x_max, resolution), 
                                       np.arange(y_min, y_max, resolution))
    vector_input = np.array([vertical.ravel(), horizontal.ravel()]).T

    # predicts every pair from xy plane and reshapes it to original shape
    Z = manager.color(vector_input)
    Z = Z.reshape(vertical.shape)

    # fills background 
    plt.contourf(vertical, horizontal, Z, alpha=0.4, cmap=cmap)
    plt.xlim(vertical.min(), vertical.max())
    plt.ylim(horizontal.min(), horizontal.max())

    plt.show()



def vienn(*sets, names=None):
    ''' runs plot_regions with some manager depends on sets amount ''' 
    if len(sets) == 2:
        names = ['A', 'B'] if not names else names
        plot_regions_with_elements(Double_manager(*sets), sets, names)
    elif len(sets) == 3:
        names = ['A', 'B', 'C'] if not names else names
        plot_regions_with_elements(Triple_manager(*sets), sets, names)
    else:
        raise ValueError('wrong number of sets')
