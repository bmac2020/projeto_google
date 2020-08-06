#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


class GeraVisualizacao:
    def __init__(self, G):
        self.grafo = G
        self.posicao = nx.spring_layout(self.grafo, dim=3)
        self.n_nodes = self.grafo.number_of_nodes()

    def gera3d(self)
        maior_aresta = max([self.grafo.degree(i) for i in range(1, self.n_nodes+1)])
        cores_nos = [plt.cm.plasma(self.grafo.degree(i)/maior_aresta) for i in range(1, self.n_nodes+1)]

        with plt.style.context(('ggplot')):
            quadro = plt.figure()
            eixo3d = Axes3D(quadro)

            for chave, valor in pos.items():
                xi = value[0]
                yi = value[1]
                zi = value[2]

                eixo3d(xi, yi, zi, c=np.array(cores_nos[key-1]).reshape(1,-1), s=10+10*self.grafo.degree(key), edgecolors='k', alpha=0.7)

            for i,j in enumerate(self.grafo.edges()):
                x = np.array((self.posicao[j[0]][0], self.posicao[j[1]][0]))
                y = np.array((self.posicao[j[0]][1], self.posicao[j[1]][1]))
                z = np.array((self.posicao[j[0]][2], self.posicao[j[1]][2]))

                eixo3d.plot(x, y, z, c='black', alpha=0.5)

        eixo3d.set_axis_off()
        plt.show()
        return
