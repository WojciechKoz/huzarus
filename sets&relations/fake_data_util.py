import numpy as np
import random
import matplotlib.pyplot as plt


def create_obj(center, deviation):
    return np.array([center[0] + random.uniform(-deviation, deviation), \
            center[1] + random.uniform(-deviation, deviation)])


def two_dim_data(centroids=[(4, 2), (1, 5)], deviation=1, num=30):
    output = []
    for centroid in centroids:
        output.append([])
        for i in range(num):
            output[-1].append(create_obj(centroid, deviation))
    return np.array(output)


def shuffle_in_unison(a, b):
    rng_state = np.random.get_state()
    np.random.shuffle(a)
    np.random.set_state(rng_state)
    np.random.shuffle(b)


def group_data(data):
    y = np.array([[1] for obj in data[0]] + [[-1] for obj in data[1]])
    data = np.vstack((data[0], data[1]))
    shuffle_in_unison(data, y)
    return data, y


def show_data(data):
    for cluster in data:
        if cluster is not None:
            plt.scatter(np.array(cluster).T[0], np.array(cluster).T[1])
    plt.show()


def cluster_data(model):
    cluster_a, cluster_b = [], []
    data, _ = group_data(two_dim_data())

    for obj in data:
        if model.predict_one(obj) == 1:
            cluster_a.append(obj)
        else:
            cluster_b.append(obj)
    return cluster_a, cluster_b


def standardizing_data(X):
    X_std = np.copy(X)
    X_std[:, 0] = (X[:, 0] - X[:, 0].mean()) / X[:, 0].std()
    X_std[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    return X_std


def plot_decision_regions(X, y, classifier, resolution=0.01):
    '''
    X is set of objects 
    (with the same number of attributes as X in fit method)
    y is set of clusters labels
    classifier - trained predictive model - perceptron, Adaline etc...
    resolution - accuracy of background (distance between two measurment points)

    draws scatter plot with divided background (many decision regions).
    
    returns None
    '''

    import matplotlib.pyplot as plt
    from matplotlib.colors import ListedColormap

    if resolution <= 0:
        raise ValueError("Resolution has to be positive number")

    # markers - tuple of marker types in plot (representation of objects in some cluster)
    # colors - tuple of colors which following cluster has
    markers = ('x', 'o', 's', '^', 'v') 
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    # size of all decision region
    # x_min, x_max 
    # min and max values increased by 1 from both sides for first attribute of each objects 
    # y_min, y_max - the same thing but for second attribute
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1

    # creates two matrixes of the range between min and max of each attribute
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
    Z = classifier.predict(vector_input)
    Z = Z.reshape(vertical.shape)

    # fills background 
    plt.contourf(vertical, horizontal, Z, alpha=0.4, cmap=cmap)
    plt.xlim(vertical.min(), vertical.max())
    plt.ylim(horizontal.min(), horizontal.max())

    # draws objects in plot
    y = y.T[0]
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1], alpha=0.8, \
                    c=colors[idx], marker=markers[idx], label=cl)

    plt.show()

