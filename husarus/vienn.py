import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from vienn_managers import DoubleManager, TripleManager, DoubleAreaManager
from _main_truth_tab import truth_table
from smart_split import smart_split
from converter import convert_sets_to_bool


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
    manager.write_sets_names(names)  # prints name of each set
    plt.gca().set_aspect('equal', adjustable='box')  # keeps square shape of diagram
    # plt.axis('scaled')
    plt.show()


def plot_regions(manager, form, resolution=0.01):
    fig = plt.subplot()

    plt.xticks([]) # hides axis numbers
    plt.yticks([])

    x_min, x_max = -1.0, 1.0
    y_min, y_max = -1.0, 1.0
    cmap = ListedColormap(('red', 'green'))
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

    Z = np.array(list(manager.color(vector_input)))
    # print('Z:',Z)
    Z = Z.reshape(1, len(Z))
    Z = Z.reshape(vertical.shape)

    # fills background 
    fig.contourf(vertical, horizontal, Z, alpha=0.4, cmap=cmap)
    plt.xlim(vertical.min(), vertical.max())
    plt.ylim(horizontal.min(), horizontal.max())
    manager.draw_circles(fig) 
    manager.write_sets_names()
    fig.set_title(form)
    plt.show()



def vienn(*sets, names=None):
    """ runs plot_regions with some manager depends on sets amount """
    if len(sets) == 1 and type(sets[0]) is str:
        items = smart_split(sets[0])
        items = convert_sets_to_bool(items) 
        table, variables = truth_table(items)
        print(variables)
        if len(variables) == 2:
            plot_regions(DoubleAreaManager(table, variables), sets[0])
        elif len(variables) == 3:
            plot_regions(TripleAreaManager(table, variables), sets[0])
        else:
            raise ValueError('wrong amount of sets')
    if len(sets) == 2:
        names = ['A', 'B'] if not names else names
        plot_regions_with_elements(DoubleManager(*sets), sets, names)
    elif len(sets) == 3:
        names = ['A', 'B', 'C'] if not names else names
        plot_regions_with_elements(TripleManager(*sets), sets, names)
    else:
        raise ValueError('wrong number of sets')
