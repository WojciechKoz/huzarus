import numpy as np
import matplotlib.pyplot as plt


class Double_classifier:
    ''' for vienn schema with only 2 sets, each set has to have at most 7 elements '''
    def __init__(self, set_A, set_B):
        self.A_slots  = np.array([[-0.25,0], [-0.225, 0.05], [-0.225, -0.05], \
                [-0.175, 0.1], [-0.175, -0.1], [-0.12, 0.125], [-0.12, -0.125]])

        self.B_slots  = np.array([[0.25,0], [0.225, 0.05], [0.225, -0.05], \
                [0.175, 0.1], [0.175, -0.1], [0.12, 0.125], [0.12, -0.125]])

        self.AB_slots = np.array([[0,0], [0, 0.08], [0, -0.08], \
                [-0.06, 0], [0.06, 0], [0, 0.04], [0, -0.04]])

        self.size = 240 # size of obj in plot 
        self.colors = ('#ff0000', '#0000ff', '#990099', 'lightgreen')

        self.A = set_A.difference(set_B)
        self.B = set_B.difference(set_A)
        self.AB = set_A.intersection(set_B)


    def draw_circles(self):
        plt.scatter([-0.1], [0], c='red', s=4*10**4, alpha=0.5)
        plt.scatter([0.1], [0], c='blue', s=4*10**4, alpha=0.5)
        plt.xlim(-0.4, 0.4)



    def slots(self):
        return self.A_slots[:len(self.A)], self.B_slots[:len(self.B)], self.AB_slots[:len(self.AB)]


    def subsets(self, idx):
        return list([self.A.difference(self.B), self.B.difference(self.A), \
                self.A.intersection(self.B)])[idx]


    def write_sets_names(self, names):
        plt.text(-0.175, 0, names[0], ha='center', va='center', fontsize=15)
        plt.text(0, 0.12, names[0]+names[1], ha='center', va='center', fontsize=15)
        plt.text(0.175, 0, names[1], ha='center', va='center', fontsize=15)


class Triple_classifier:
    ''' for vienn diagram with 3 sets, each set has to have at most 5 elements '''
    def __init__(self, set_A, set_B, set_C):
        self.A_slots  = np.array([[-0.14,-0.15], [-0.2, -0.1], [-0.24, -0.03], \
                [-0.26, 0.05], [-0.17, -0.03]])

        self.B_slots  = np.array([[0.14,-0.15], [0.2, -0.1], [0.24, -0.03], \
                [0.26, 0.05], [0.17, -0.03]])

        self.C_slots = np.array([[0,0.25], [-0.15, 0.27], [0.15, 0.27], \
                [-0.07, 0.31], [0.07, 0.31]])

        self.AB_slots = np.array([[0,-0.09], [-0.047, -0.13], [0.047, -0.13], \
                [-0.08, -0.08], [0.08, -0.08]])

        self.size = 240 # size of obj in plot 
        self.colors = ('#ff0000', '#0000ff', '#999900', '#990099', 'lightgreen')

        self.A = set_A.difference(set_B.union(set_C))
        self.B = set_B.difference(set_A.union(set_C))
        self.C = set_C.difference(set_A.union(set_B))
        self.AB = set_A.intersection(set_B).difference(set_C)
        self.AC = set_A.intersection(set_C).difference(set_B)
        self.BC = set_B.intersection(set_C).difference(set_A)
        self.ABC = set_B.intersection(set_C).intersection(set_A)


    def draw_circles(self):
        plt.scatter([-0.1], [0], c='red', s=4*10**4, alpha=0.5)
        plt.scatter([0.1], [0], c='blue', s=4*10**4, alpha=0.5)
        plt.scatter([0], [0.173], c='yellow', s=4*10**4, alpha=0.5)
        plt.xlim(-0.4, 0.4)
        plt.ylim(-0.3, 0.5)


    def slots(self):
        return self.A_slots[:len(self.A)], self.B_slots[:len(self.B)], self.C_slots[:len(self.C)], \
                self.AB_slots[:len(self.AB)]


    def subsets(self, idx):
        return list([self.A, self.B, self.C, self.AB])[idx]


    def write_sets_names(self, names):
        plt.text(-0.26, -0.09, names[0], ha='center', va='center', fontsize=15)
        plt.text(0, -0.175, names[0]+names[1], ha='center', va='center', fontsize=15)
        plt.text(0.26, -0.09, names[1], ha='center', va='center', fontsize=15)
