#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class MostraVisualizacao:
    def __init__(self, G, n_nodes):
        self.grafo = G
        self.posicao = nx.spring_layout(self.grafo, dim=3)
        self.n_nodes = n_nodes

    def gera3d(self):
        maior_aresta = max([self.grafo.degree(i) for i in range(1, self.n_nodes+1)])
        cores_nos = [plt.cm.plasma(self.grafo.degree(i)/maior_aresta) for i in range(1, self.n_nodes+1)]

        def fecha_quadro():
            plt.close()

        with plt.style.context(('ggplot')):
            quadro = plt.figure()
            timeout = quadro.canvas.new_timer(interval=10000)
            timeout.add_callback(fecha_quadro)
            eixo3d = Axes3D(quadro)

            for chave, valor in self.posicao.items():
                xi = valor[0]
                yi = valor[1]
                zi = valor[2]

                eixo3d.scatter(xi, yi, zi, c=np.array(cores_nos[chave-1]).reshape(1,-1), s=10+10*self.grafo.degree(chave), edgecolors='k', alpha=0.7)

            for i,j in enumerate(self.grafo.edges()):
                x = np.array((self.posicao[j[0]][0], self.posicao[j[1]][0]))
                y = np.array((self.posicao[j[0]][1], self.posicao[j[1]][1]))
                z = np.array((self.posicao[j[0]][2], self.posicao[j[1]][2]))

                eixo3d.plot(x, y, z, c='black', alpha=0.5)

        eixo3d.set_axis_off()
        timeout.start()
        plt.show()
        return

class MostraMatriz:
    def __init__(self, matriz):
        self.matriz = matriz

    def mostraMatriz(self):
        print("\n")
        for i in range(len(self.matriz)):
            for k in range(len(self.matriz)):
                print("%4.2f" % self.matriz[i][k], " ", end ='')
            print("")
        return
