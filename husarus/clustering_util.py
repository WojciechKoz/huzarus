from math import sqrt
from obj_init import show_clusters
from random import sample 
import numpy as np


def minkowski_dist(obj1, obj2):
    assert len(obj1) == len(obj2)
    dim = len(obj1)
    return sum([(a-b)**dim for a, b in zip(obj1, obj2)])**(1/dim)


def make_cluster(med, univ):
    output = [[] for m in med]

    for obj in univ:
        dists = [minkowski_dist(obj, m) for m in med]
        output[dists.index(min(dists))].append(obj)

    return output


def find_medoid(cluster):
    dist_sum = [sum([minkowski_dist(obj, diff_obj) for diff_obj in cluster]) for obj in cluster]
    return cluster[dist_sum.index(min(dist_sum))]
        
    
def random_medoids(univ, num):
    return sample(list(univ), k=num) 


def array_in_list(myarr, list_arrays):
    return next((True for elem in list_arrays if np.array_equal(elem, myarr)), False)


def cluster_loop(univ, n_clus, n_iter):
    medoids = random_medoids(univ, n_clus)
    c_tuple = (0.1, 0.4, 0.3, 0.6, 0.9)
    colors = []

    for _ in range(n_iter):
        clusters = make_cluster(medoids, univ)
        medoids = [find_medoid(cluster) for cluster in clusters]

        colors.append([]) 
        for obj in univ:
            for index, cluster in enumerate(clusters):
                if array_in_list(obj, cluster): 
                    colors[-1].append(c_tuple[index])
                    break
    return clusters, colors
