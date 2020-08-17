#!/usr/bin/python3

import networkx as nx

class GeraGrafo:
    def __init__(self, k):
        self.caciques = [] # Cria uma lista para armazenar os caciques.
        self.caciques2 = [] # Cria outra lista para armazenar os caciques.
        self.numero_caciques = k # Número de caciques.

    def listaNodeCacique(self):
        cont = 0
        # Percorre de 1 até o número de caciques.
        for j in range(1, int(self.numero_caciques)+1):
            self.caciques.append(j+cont) # Adiciona os caciques a lista.
            self.caciques2.append(j+cont) # Adiciona os caciques a lista.
            cont = cont + j

        print("O número dos nodes de cada cacique é", self.caciques)

    def criaGrafo(self):
        self.grafo = nx.DiGraph() # Inicia o grafo.
        self.grafo.add_nodes_from(self.caciques) # Adiciona os nós dos caciques.

        count = 0
        for i in self.caciques: # Percorre a lista dos caciques para fazer a conexão entre os mesmos.
            count = count + 1
            for p in self.caciques[count:]: # Percorre de count pra frente.
                self.grafo.add_edge(i, p) # Cria uma conexão (aresta) entre i e p.
                self.grafo.add_edge(p, i) # Cria uma conexão (aresta) entre p e i.
                # Aqui é importante fazer duas conexões, pois as conexões no grafo
                # cacique-tribo são dadas por conexões mútuas.

        cont = 1
        while len(self.caciques) != 0:
            for t in self.caciques: # Faz a conexão entre os caciques e os respectivos índios.
                self.grafo.add_edge(t, t+cont)
                self.grafo.add_edge(t+cont, t)
            del self.caciques[0]
            cont = cont + 1

        nova_lista = [] # Cria uma nova lista que guardará os índios.
        for i in self.grafo.edges(): # Percorre todas as conexões.
            x = list(i) # É preciso converter para lista, pois as conexões são tuplas.
            if (x[0] and x[1]) in self.caciques2: # Se os dois valores forem caciques, então o loop é reiniciado.
                continue
            # Verifica se o x[0] é cacique e se x[1] não já foi adicionado a nova_lista
            elif x[0] in self.caciques2 and x[1] not in nova_lista:
                nova_lista.append([x[1], x[0]]) # Coloca o cacique como segundo elemento.
            # Verifica se o x[1] é cacique e se x[0] não já foi adicionado a nova_lista
            elif x[1] in self.caciques2 and x[0] not in nova_lista:
                nova_lista.append([x[0], x[1]]) # Coloca o cacique como segundo elemento.

        for i in self.caciques2: # Percorre a segunda lista de caciques.
            list2 = [] # Cria outra nova lista para guardar só os índios.
            for x in nova_lista: # Percorre a nova_lista procurando o cacique igual a i.
                if x[1] == i:
                    list2.append(x[0]) # Appenda a list2 com o índio desse cacique i.
            for z in range(len(list2)-1): # Percorre a list2 até o penúltimo valor.
                for k in range(z, len(list2)): # Percorre list2 de z até o último valor.
                    if list2[z] != list2[k]: # Para que não seja feita conexões de um índio consigo mesmo.
                        self.grafo.add_edge(list2[z], list2[k]) # Liga um índio ao outro.
                        self.grafo.add_edge(list2[k], list2[z]) # Liga um índio ao outro.

        return self.grafo # Retorna o grafo.

    def n_nodes(self): # Gera o número de nodes (nós) existentes no grafo.
        return self.grafo.number_of_nodes()

    def arestas(self): # Gera as arestas (conexões) existentes no grafo.
        return self.grafo.edges()

    def posicao(self): # Gera a posição do grafo.
        self.posicao = nx.spring_layout(self.grafo, dim=3)
        return self.posicao

class GeraMatriz:
    def __init__(self, grafo, n_nodes, arestas):
        self.n_nodes = n_nodes # Define o número de nós dentro do escopo da classe.
        self.grafo = grafo # Define o grafo dentro do escopo da classe.
        self.arestas = arestas # Define as arestas dentro do escopo da classe.

    def geraMatriz(self):
        grafo_lista = [] # Essa lista guardará a arestas em forma de list e não de tupla.
        for k in self.arestas:
            grafo_lista.append(list(k))

        # Cria a matriz com zeros, do tamanho do grafo.
        matriz = [[0 for k in range(self.n_nodes)] for i in range(self.n_nodes)]

        for i in range(1, self.n_nodes+1):
            for k in range(len(grafo_lista)):
                if grafo_lista[k][0] == i:
                    matriz[grafo_lista[k][1]-1][i-1] = 1

        for k in range(len(matriz)):
            cont = 0
            for j in range(len(matriz)):
                if matriz[j][k] == 1:
                    cont += 1
            for i in range(len(matriz)):
                if matriz[i][k] == 1:
                    matriz[i][k] = 1/cont

        return matriz
