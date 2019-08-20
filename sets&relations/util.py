import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from classifiers import Double_classifier, Triple_classifier


def plot_regions(classifier, sets, names):
    ''' draws vienn diagram using matplotlib libarary and given classifier '''

    classifier.draw_circles() # draws representations of sets (big circles)

    # plt.xticks([]) # hides axis numbers
    # plt.yticks([])

    points = classifier.slots() # split sets e.g. (A, B) -> (A-B, AB, B-A)

    for idx, cluster in enumerate(points):
        # draws elements in diagram
        plt.scatter(cluster[:, 0], cluster[:, 1], s=classifier.size, c=classifier.colors[idx], marker='s')
        # prints name of each element
        for (x, y), value in zip(cluster, classifier.subsets(idx)):
            plt.annotate(value, (x, y), ha='center', va='center', c='white')

    plt.title('Vienn diagram')
    classifier.write_sets_names(names) # prints name of each set
    plt.gca().set_aspect('equal', adjustable='box') # keeps square shape of diagram
    # plt.axis('scaled')
    plt.show()


def vienn(*sets, names=['A', 'B']):
    ''' runs plot_regions with some classifier depends on sets amount ''' 
    if len(sets) == 2:
        plot_regions(Double_classifier(*sets), sets, names)
    elif len(sets) == 3:
        plot_regions(Triple_classifier(*sets), sets, names)
    else:
        raise ValueError('wrong number of sets')
