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
                for i in self.grafo.edges(): # Faz a conexão entre os índios.
                    if i[0] == t and i[1] != t+cont and i[1] not in self.caciques2:
                        self.grafo.add_edge(i[1], t+cont)
                        self.grafo.add_edge(t+cont, i[1])
                    elif i[1] == t and i[0] != t+cont and i[0] not in self.caciques2:
                        self.grafo.add_edge(i[0], t+cont)
                        self.grafo.add_edge(t+cont, i[0])
            del self.caciques[0]
            cont = cont + 1

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


class GeraMatrizModificada:
    def __init__(self, matriz, n_nodes):
        self.matriz = matriz
        self.n_nodes = n_nodes

    def cria_MM(self):
        alfa = 0.15
        alfa_Sn = alfa * 1 / self.n_nodes  # Elementos da Matriz Sn.
        MM = []  # Matriz Modificada.
        MM[:] = self.matriz[:]

        for k in range(self.n_nodes):
            for i in range(self.n_nodes):  # MM = (1 - alfa)M + alfa*Sn.
                MM[k][i] = (1 - alfa) * MM[k][i] + alfa_Sn

        return MM

class MatrizAuxiliar:
    def __init__(self, matriz_modificada, n_nodes):
        self.matriz = matriz_modificada
        self.n_nodes = n_nodes

    def cria_matrizaux(self):
        matriz_aux = []
        matriz_aux[:] = self.matriz[:]

        for k in range(self.n_nodes):
            matriz_aux[k][k] = matriz_aux[k][k] - 1 # Subtrai 1 da diagonal principal.

        return matriz_aux

class Escalonamento:
    def __init__(self, matriz_aux, n_nodes):
        self.matriz = matriz_aux
        self.n_nodes = n_nodes

    def escalona(self):
        # Realiza o pivotamento.
        for k in range(self.n_nodes): # Varre as colunas.
            # Define variável que recebe o elemento de maior valor absoluto da coluna. Começa com o 1º.
            maximo_absoluto = abs(self.matriz[0][k])
            # Define variável que recebe o indice do maior valor absoluto da coluna. Começa com o 1º.
            indice_absoluto = 0

            for l in range (1, self.n_nodes): # Varre as linhas.
                # Verifica se o valor do elemento da linha l, coluna k é maior que o maximo absoluto.
                # Melhorar essa linha de codigo. talvez não precise da primeira parte do != l.
                if indice_absoluto != l and abs(self.matriz[l][k]) >= maximo_absoluto:
                    # Troca o maximo e o indice se for verdade.
                    maximo_absoluto = abs(self.matriz[l][k])
                    indice_absoluto = l
            # Troca as linhas para levar o maior elemento de valor absoluto ao pivô.
            if abs(self.matriz[indice_absoluto][k]) >= abs(self.matriz[k][k]):
                self.matriz[indice_absoluto], self.matriz[k] = self.matriz[k], self.matriz[indice_absoluto]

        # Realiza o escalonamento.
        for k in range (self.n_nodes): # Varre as colunas.
            for i in range(k + 1, self.n_nodes): # Varre as linhas.
                alpha_i = self.matriz[i][k] / self.matriz[k][k] # Divide o elemento da linha i pelo pivô.
                for j in range(k, self.n_nodes): # Varre as colunas.
                    # Altera os elementos das linhas à direita da coluna que está sendo zerada.
                    self.matriz[i][j] = self.matriz[i][j] - (alpha_i * self.matriz[k][j])

        return self.matriz

class VetorX:
    def __init__(self, matriz_escalonada, n_nodes):
        self.matriz = matriz_escalonada
        self.n_nodes = n_nodes

    def encontra_vetorx(self):
        x_n = 1 # Define o vetor da linha de zeros como 1.
        lista_x_k = [x_n] # Cria lista que receberá o peso das páginas (x_k).
        for k in range (self.n_nodes-2,-1,-1): # Inicia na penúltima coluna e vai até a primeira.
            x_k = 0 # Inicia a soma do x_k, que é o vetor em questão que está sendo calculado.
            p = -1
            for i in range (k+1,self.n_nodes): # Varre as colunas da linha que está sendo calculada.
                # Multiplica os elementos à direita do pivô pelo x_n correspondente e soma em x_k.
                x_k += self.matriz[k][i] * lista_x_k[p]
                p -= 1
            # Divide a soma total do x_k pelo elemento pivô.
            # Equivalente a: 5x - 2 = 0 => 5x = 2 => x = 2/5
            x_k = (-x_k)/self.matriz[k][k]
            # Adiciona o valor do peso de x_k à lista de pesos.
            lista_x_k.append(x_k)

        # NORMALIZAÇÃO
        soma_lista = sum(lista_x_k)

        # Divide os pesos de cada elemento pela soma de todos os pesos.
        for k in range (len(lista_x_k)):
            lista_x_k[k] = lista_x_k[k]/soma_lista

        # Inverte a ordem da lista para ter o x_1 como primeiro elemento indo até o x_n.
        lista_x_k.reverse()

        # print("\n",lista_x_k)
        print("\nSoma: ",sum(lista_x_k))

        return lista_x_k

class Constante:
    def __init__(self, matriz_modificada, n_nodes):
        self.matriz = matriz_modificada
        self.n_nodes = n_nodes

    def constante_C(self):
        lista_max = []
        min_coluna = self.matriz[0][0]

        for j in range(self.n_nodes):
            for i in range(self.n_nodes):
                if self.matriz[i][j] < min_coluna:
                    min_coluna = self.matriz[i][j]
            lista_max.append(abs(1 - (2 * min_coluna)))
        return max(lista_max)

class Vetor_VLC:
    def __init__(self, matriz_esparsa):
        self.matriz = matriz_esparsa

    def vetor_VLC(self):
        V = [] # Elemento.
        L = [] # Linha do elemento.
        C = [] # Coluna do elemento.

        for k in range(len(self.matriz)):
            for j in range(len(self.matriz)):
                if self.matriz[k][j] != 0:
                    V.append(self.matriz[k][j]) # Adiciona elemento em V.
                    L.append(k) # Salva a linha.
                    C.append(j) # Salva a coluna.

        return V, L, C

class Solucao_Iterativa:
    def __init__(self, V, L, C, constante):
        self.V = V
        self.L = L
        self.C = C
        self.constante = constante

    def solucao(self):
        Z_k1 = [0 for i in range(max(self.L) + 1)] # Inicia nulo com tamanho n da matriz nxn.
        Y = [1/len(Z_k1) for i in range(len(Z_k1))]

        Erro = 1 # Definido assim para entrar no while.

        Z_k = [1/len(Z_k1) for i in range(len(Z_k1))]

        cont = 0
        while abs(Erro) >= 1e-5:
            cont += 1
            if cont > 10000:
                break

            Z_k1 = [0 for i in range(max(self.L) + 1)]

            for k in range(len(self.L)):
                Z_k1[self.L[k]] = Z_k1[self.L[k]] + self.V[k] * Y[self.C[k]]
            Y = Z_k1[:]

            norma_1_diferenca = 0
            for i in range(len(Z_k1)):
                norma_1_diferenca += (Z_k1[i] - Z_k[i])
            Erro = (self.constante / (1 - self.constante)) * norma_1_diferenca

            print("\nErro:", Erro)
            Z_k[:] = Z_k1[:]

        return Z_k1
