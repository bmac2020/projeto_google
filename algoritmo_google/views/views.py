#!/usr/bin/python3

import networkx as nx
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

class MostraVisualizacao:
    def __init__(self, G, n_nodes, posicao, arestas):
        self.grafo = G # Define o grafo dentro do escopo da classe.
        self.n_nodes = n_nodes # Define o número de nós dentro do escopo da classe.
        self.posicao = posicao # Define a posição do grafo dentro do escopo da classe.
        self.arestas = arestas # Define as arestas dentro do escopo da classe.

    def gera3d(self):
        # Define a maior aresta, a que tem mais conexões.
        maior_aresta = max([self.grafo.degree(i) for i in range(1, self.n_nodes+1)])
        # Define cores diferentes para os nós (nem sempre isso acontece).
        cores_nos = [plt.cm.plasma(self.grafo.degree(i)/maior_aresta) for i in range(1, self.n_nodes+1)]

        # Define o estilo do quadro 3D. Esse é um estilo temporário, não é global.
        with plt.style.context(('ggplot')):
            quadro = plt.figure() # Cria a figura para o quadro.
            # Define o intervalo de 10 segundos para a exibição do quadro.
            timeout = quadro.canvas.new_timer(interval=10000)
            # Decorridos os 10 segundos, a função (anônima) lambda será chamada e fechará o quadro.
            timeout.add_callback(lambda: plt.close())
            # Cria os eixos 3D no quadro.
            eixo3d = Axes3D(quadro)

            # Percorre as posições do grafo.
            for chave, valor in self.posicao.items():
                xi = valor[0] # A posição x de um determinado nó
                yi = valor[1] # A posição y de um determinado nó
                zi = valor[2] # A posição z de um determinado nó

                # Plota cada nó no quadro 3D.
                eixo3d.scatter(xi, yi, zi, c=np.array(cores_nos[chave-1]).reshape(1,-1), s=10+10*self.grafo.degree(chave), edgecolors='k', alpha=0.7)

            # Percorre as conexões e liga as mesmas.
            for j in self.arestas:
                x = np.array((self.posicao[j[0]][0], self.posicao[j[1]][0]))
                y = np.array((self.posicao[j[0]][1], self.posicao[j[1]][1]))
                z = np.array((self.posicao[j[0]][2], self.posicao[j[1]][2]))

                # Plota a ligação x, y, z.
                eixo3d.plot(x, y, z, c='black', alpha=0.5)

        eixo3d.set_axis_off() # Desabilita os eixos.
        timeout.start() # Começa o contagem de tempo (10 segundos).
        plt.show() # Exibe o quadro.
        return # Retorna/sai da função.

class MostraMatriz:
    def __init__(self, matriz):
        self.matriz = matriz # Recebe a matriz e a define dentro do escopo da classe.

    def mostraMatriz(self): # Exibe a matriz nxn.
        print("\n")
        for i in range(len(self.matriz)):
            for k in range(len(self.matriz)):
                print("%4.2f" % self.matriz[i][k], " ", end ='')
            print("")
        return
