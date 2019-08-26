import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Wedge
from matplotlib.collections import PatchCollection
from converter import convert_sets_to_bool
from smart_split import smart_split
from _main_truth_tab import truth_table
from time import time


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


class DoubleAreaManager:
    def __init__(self, table, variables):
        self.table = table
        self.vars = variables

        self.in_circle_A = lambda x, y: (x+0.3)**2 + y**2 < 0.5**2 
        self.in_circle_B = lambda x, y: (x-0.3)**2 + y**2 < 0.5**2 

        self.in_A =  lambda x, y: self.in_circle_A(x, y) and not self.in_circle_B(x, y)
        self.in_B =  lambda x, y: self.in_circle_B(x, y) and not self.in_circle_A(x, y)
        self.in_AB = lambda x, y: self.in_circle_B(x, y) and self.in_circle_A(x, y)

        self.value_U = self.predict([(self.vars[0], False), (self.vars[1], False)])
        self.value_A = self.predict([(self.vars[0], True), (self.vars[1], False)])
        self.value_B = self.predict([(self.vars[0], False), (self.vars[1], True)])
        self.value_AB = self.predict([(self.vars[0], True), (self.vars[1], True)])


    def predict(self, args):
        filtered = self.table.copy()
        for arg in args:
            filtered = filtered[filtered[arg[0]] == arg[1]]
        return np.ravel(filtered.values)[-1]


    def color(self, vector):
        ''' A, B aren't a real name of sets in vienn diagram
            I'm using those names only to predict in which set representation 
            the following point is '''
        start = time()
        for point in vector:
            if self.in_A(*point):
                yield self.value_A
            elif self.in_B(*point):
                yield self.value_B
            elif self.in_AB(*point):
                yield self.value_AB
            else:
                yield self.value_U 
        print('time:', time() - start)


    @staticmethod
    def draw_circles(fig):
        circle_a = Wedge((-0.3, 0), 0.5, 0, 360, width=0.01,color='black', alpha=0.5)
        circle_b = Wedge((0.3, 0), 0.5, 0, 360, width=0.01, color='black', alpha=0.5)

        fig.add_artist(circle_a)
        fig.add_artist(circle_b)


    def write_sets_names(self):
        plt.text(-0.4, 0, self.vars[0], ha='center', va='center', fontsize=15)
        plt.text(0.4, 0, self.vars[1], ha='center', va='center', fontsize=15)
        plt.text(0, 0, self.vars[0]+self.vars[1], ha='center', va='center', fontsize=15)


class TripleAreaManager:
    def __init__(self, table, variables):
        self.table = table
        self.vars = variables

        self.in_circle_A = lambda x, y: (x+0.3)**2 + (y+0.15)**2 < 0.5**2 
        self.in_circle_B = lambda x, y: (x-0.3)**2 + (y+0.15)**2 < 0.5**2 
        self.in_circle_C = lambda x, y: (x)**2 + (y-0.35)**2 < 0.5**2 

        self.in_A =  lambda x, y: \
                self.in_circle_A(x, y) and not self.in_circle_B(x, y) and not self.in_circle_C(x, y)

        self.in_B =  lambda x, y: \
                self.in_circle_B(x, y) and not self.in_circle_A(x, y) and not self.in_circle_C(x, y)

        self.in_C =  lambda x, y: \
                self.in_circle_C(x, y) and not self.in_circle_A(x, y) and not self.in_circle_B(x, y)

        self.in_AB = lambda x, y: \
                self.in_circle_B(x, y) and self.in_circle_A(x, y) and not self.in_circle_C(x, y)

        self.in_AC = lambda x, y: \
                self.in_circle_A(x, y) and self.in_circle_C(x, y) and not self.in_circle_B(x, y)

        self.in_BC = lambda x, y: \
                self.in_circle_B(x, y) and self.in_circle_C(x, y) and not self.in_circle_A(x, y)

        self.in_ABC = lambda x, y: \
                self.in_circle_A(x, y) and self.in_circle_B(x, y) and self.in_circle_C(x, y)

        self.value_U = self.predict([(self.vars[0], False), (self.vars[1], False), (self.vars[2], False)])
        self.value_A = self.predict([(self.vars[0], True), (self.vars[1], False), (self.vars[2], False)])
        self.value_B = self.predict([(self.vars[0], False), (self.vars[1], True), (self.vars[2], False)])
        self.value_C = self.predict([(self.vars[0], False), (self.vars[1], False), (self.vars[2], True)])
        self.value_AB = self.predict([(self.vars[0], True), (self.vars[1], True), (self.vars[2], False)])
        self.value_AC = self.predict([(self.vars[0], True), (self.vars[1], False), (self.vars[2], True)])
        self.value_BC = self.predict([(self.vars[0], False), (self.vars[1], True), (self.vars[2], True)])
        self.value_ABC = self.predict([(self.vars[0], True), (self.vars[1], True), (self.vars[2], True)])


    def predict(self, args):
        filtered = self.table.copy()
        for arg in args:
            filtered = filtered[filtered[arg[0]] == arg[1]]
        return np.ravel(filtered.values)[-1]


    def color(self, vector):
        ''' A, B aren't a real name of sets in vienn diagram
            I'm using those names only to predict in which set representation 
            the following point is '''
        start = time()
        for point in vector:
            if self.in_A(*point):
                yield self.value_A
            elif self.in_B(*point):
                yield self.value_B
            elif self.in_C(*point):
                yield self.value_C
            elif self.in_AB(*point):
                yield self.value_AB
            elif self.in_AC(*point):
                yield self.value_AC
            elif self.in_BC(*point):
                yield self.value_BC
            elif self.in_ABC(*point):
                yield self.value_ABC
            else:
                yield self.value_U 
        print('time:', time() - start)


    @staticmethod
    def draw_circles(fig):
        circle_a = Wedge((-0.3, -0.15), 0.5, 0, 360, width=0.01,color='black', alpha=0.5)
        circle_b = Wedge((0.3, -0.15), 0.5, 0, 360, width=0.01, color='black', alpha=0.5)
        circle_c = Wedge((0, 0.35), 0.5, 0, 360, width=0.01, color='black', alpha=0.5)

        fig.add_artist(circle_a)
        fig.add_artist(circle_b)
        fig.add_artist(circle_c)


    def write_sets_names(self):
        plt.text(-0.5, -0.15, self.vars[0], ha='center', va='center', fontsize=15)
        plt.text(0.5, -0.15, self.vars[1], ha='center', va='center', fontsize=15)
        plt.text(0, 0.65, self.vars[2], ha='center', va='center', fontsize=15)

        plt.text(0, -0.3, self.vars[0]+self.vars[1], ha='center', va='center', fontsize=15)
        plt.text(-0.3, 0.15, self.vars[0]+self.vars[2], ha='center', va='center', fontsize=15)
        plt.text(0.3, 0.15, self.vars[1]+self.vars[2], ha='center', va='center', fontsize=15)

        plt.text(0, 0, self.vars[0]+self.vars[1]+self.vars[2], ha='center', va='center', fontsize=15)
