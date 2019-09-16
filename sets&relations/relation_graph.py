from relations import Relation
import networkx as nx
from matplotlib import pyplot as plt


def render_relation(relation):
    """ renders relation as graph """
    if type(relation) is Relation:
        G = nx.Graph()
        G = nx.to_directed(G)
        G.add_edges_from(list(relation.relation))
        nx.draw_networkx(G, with_labels=True, node_color='skyblue', node_size=1500, edge_cmap=plt.cm.Blues)
        plt.title("R=" + str(relation.relation))
        plt.show()

    else:
        raise TypeError("argument type must be 'Relation'")
