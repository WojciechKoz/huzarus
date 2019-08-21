import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.collections import PatchCollection


class DoubleManager:
    """ for vienn schema with only 2 sets, each set has to have at most 7 elements """

    def __init__(self, set_a, set_b):
        self.A_slots = np.array([[-0.25, 0], [-0.225, 0.05], [-0.225, -0.05],
                                 [-0.175, 0.1], [-0.175, -0.1], [-0.12, 0.125], [-0.12, -0.125]])

        self.B_slots = np.array([[0.25, 0], [0.225, 0.05], [0.225, -0.05],
                                 [0.175, 0.1], [0.175, -0.1], [0.12, 0.125], [0.12, -0.125]])

        self.AB_slots = np.array([[0, 0], [0, 0.08], [0, -0.08],
                                  [-0.06, 0], [0.06, 0], [0, 0.04], [0, -0.04]])

        self.size = 240  # size of obj in plot
        self.colors = ('#ff0000', '#0000ff', '#990099')

        self.A = set_a.difference(set_b)
        self.B = set_b.difference(set_a)
        self.AB = set_a.intersection(set_b)

    @staticmethod
    def draw_circles():
        circle_a = Circle((-0.1, 0), 0.23, color='red', alpha=0.5)
        circle_b = Circle((0.1, 0), 0.23, color='blue', alpha=0.5)

        fig, ax = plt.subplots()
        ax.add_artist(circle_a)
        ax.add_artist(circle_b)

        plt.xlim(-0.4, 0.4)
        plt.ylim(-0.4, 0.4)

    def slots(self):
        return self.A_slots[:len(self.A)], self.B_slots[:len(self.B)], self.AB_slots[:len(self.AB)]

    def subsets(self, idx):
        return list([self.A, self.B, self.AB])[idx]

    @staticmethod
    def write_sets_names(names):
        plt.text(-0.175, 0, names[0], ha='center', va='center', fontsize=15)
        plt.text(0, 0.12, names[0] + names[1], ha='center', va='center', fontsize=15)
        plt.text(0.175, 0, names[1], ha='center', va='center', fontsize=15)


class TripleManager:
    """ for vienn diagram with 3 sets, each set has to have at most 5 elements """

    def __init__(self, set_a, set_b, set_c):
        self.A_slots = np.array([[-0.14, -0.15], [-0.2, -0.1], [-0.24, -0.03],
                                 [-0.26, 0.05], [-0.17, -0.03]])

        self.B_slots = np.array([[0.14, -0.15], [0.2, -0.1], [0.24, -0.03],
                                 [0.26, 0.05], [0.17, -0.03]])

        self.C_slots = np.array([[0, 0.25], [-0.15, 0.27], [0.15, 0.27],
                                 [-0.07, 0.31], [0.07, 0.31]])

        self.AB_slots = np.array([[0, -0.09], [-0.047, -0.13], [0.047, -0.13],
                                  [-0.08, -0.08], [0.08, -0.08]])

        self.AC_slots = np.array([[-0.13, 0.12], [-0.19, 0.12], [-0.16, 0.17],
                                  [-0.15, 0.06], [-0.09, 0.18]])

        self.BC_slots = np.array([[0.13, 0.12], [0.19, 0.12], [0.16, 0.17],
                                  [0.15, 0.06], [0.09, 0.18]])

        self.ABC_slots = np.array([[0, 0.03], [-0.05, 0], [0.05, 0],
                                   [-0.06, 0.09], [0.06, 0.09]])

        self.size = 240  # size of obj in plot
        self.colors = ('#ff0000', '#0000ff', '#bbbb00', '#990099', '#555500', '#00ff00', '#777777')

        self.A = set_a.difference(set_b.union(set_c))
        self.B = set_b.difference(set_a.union(set_c))
        self.C = set_c.difference(set_a.union(set_b))
        self.AB = set_a.intersection(set_b).difference(set_c)
        self.AC = set_a.intersection(set_c).difference(set_b)
        self.BC = set_b.intersection(set_c).difference(set_a)
        self.ABC = set_b.intersection(set_c).intersection(set_a)

    @staticmethod
    def draw_circles():
        circle_a = Circle((-0.1, 0), 0.23, color='red', alpha=0.5)
        circle_b = Circle((0.1, 0), 0.23, color='blue', alpha=0.5)
        circle_c = Circle((0, 0.173), 0.23, color='yellow', alpha=0.5)

        fig, ax = plt.subplots()
        ax.add_artist(circle_a)
        ax.add_artist(circle_b)
        ax.add_artist(circle_c)

        plt.xlim(-0.4, 0.4)
        plt.ylim(-0.3, 0.5)

    def slots(self):
        return self.A_slots[:len(self.A)], self.B_slots[:len(self.B)], self.C_slots[:len(self.C)], \
               self.AB_slots[:len(self.AB)], self.AC_slots[:len(self.AC)], self.BC_slots[:len(self.BC)], \
               self.ABC_slots[:len(self.ABC)]

    def subsets(self, idx):
        return list([self.A, self.B, self.C, self.AB, self.AC, self.BC, self.ABC])[idx]

    @staticmethod
    def write_sets_names(names):
        plt.text(-0.26, -0.09, names[0], ha='center', va='center', fontsize=15)
        plt.text(0.26, -0.09, names[1], ha='center', va='center', fontsize=15)
        plt.text(0, 0.38, names[2], ha='center', va='center', fontsize=15)

        plt.text(0, -0.175, names[0] + names[1], ha='center', va='center', fontsize=15)
        plt.text(-0.2, 0.17, names[0] + names[2], ha='center', va='center', fontsize=15)
        plt.text(0.2, 0.17, names[1] + names[2], ha='center', va='center', fontsize=15)

        plt.text(0, 0.08, names[0] + names[1] + names[2], ha='center', va='center', fontsize=15)