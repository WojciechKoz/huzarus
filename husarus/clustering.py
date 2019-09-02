from obj_init import create_universe, show_universe, show_clusters
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from clustering_util import cluster_loop


def anim_plot(univ, colors, fig, time_text):
    numframes = colors.shape[0]

    x, y = univ.T[0], univ.T[1]

    pts = np.array([x, y]).T

    scat = plt.scatter(x, y, c=colors[0], s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=range(numframes),
                                  fargs=(colors, scat, time_text), interval=750)
    plt.show()


def update_plot(i, data, scat, time_text):
    scat.set_array(data[i])
    time_text.set_text('step no. ' + str(i+1))
    return scat,

def k_means():
    K = create_universe(cluster_size=80)
    cluster, colors = cluster_loop(K, 3, 5)


    fig = plt.figure()
    time_text = fig.text(0.05, 0.95, 'clustering sample', horizontalalignment='left', \
            verticalalignment='top')

    anim_plot(K, np.array(colors), fig, time_text)

k_means()
