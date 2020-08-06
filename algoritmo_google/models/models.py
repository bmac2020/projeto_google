#!/usr/bin/python3

import networkx as nx

class GeraGrafo:
    def __init__(self, k):
        self.caciques = []
        self.caciques2 = []
        self.tamanho = k

    def listaNodeCacique(self):
        cont = 0
        for j in range(1, int(self.tamanho)+1):
            self.caciques.append(j+cont)
            self.caciques2.append(j+cont)
            cont = cont + j

        print("O número dos nodes de cada cacique é", self.caciques)

    def criaGrafo(self):
        self.grafo = nx.DiGraph()
        self.grafo.add_nodes_from(self.caciques)

        count = 0
        for i in self.caciques:
            count = count + 1
            for p in self.caciques[count:]:
                self.grafo.add_edge(i, p)
                self.grafo.add_edge(p, i)

        cont = 1
        while len(self.caciques) != 0:
            for t in self.caciques:
                self.grafo.add_edge(t, t+cont)
                self.grafo.add_edge(t+cont, t)
            del self.caciques[0]
            cont = cont + 1

        nova_lista = []
        for i in self.grafo.edges():
            x = list(i)
            if (x[0] and x[1]) in self.caciques2:
                continue
            elif x[0] in self.caciques2 and x[1] not in nova_lista:
                nova_lista.append([x[1], x[0]])
            elif x[1] in self.caciques2 and x[0] not in nova_lista:
                nova_lista.append([x[1], x[0]])

        for i in self.caciques2:
            list2 = []
            for x in nova_lista:
                if x[1] == i:
                    list2.append(x[0])
            for x in range(len(list2)-1):
                for k in range(x, len(list2)):
                    if list2[x] != list2[k]:
                        self.grafo.add_edge(list2[x], list2[k])
                        self.grafo.add_edge(list2[k], list2[x])

        return self.grafo

    def edges(self):
        return self.grafo.number_of_edges()
