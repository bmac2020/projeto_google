#!/usr/bin/python3

import networkx as nx
import random

class Rede:
    def __init__(self):
        self.nodes = []
        self.conexao = []

    def adiciona_node(self, node):
        self.nodes.append(node)

    def adiciona_nodes(self, nodes):
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)

    def adiciona_conexao(self, conexao):
        if conexao not in self.conexao:
            if conexao[0] not in self.nodes:
                self.nodes.append(conexao[0])
            if conexao[1] not in self.nodes:
                self.nodes.append(conexao[1])
            self.conexao.append(conexao)

    def adiciona_conexoes(self, conexoes):
        for i in conexoes:
            self.adiciona_conexao(i)

    def numero_total_nodes(self):
        return len(self.nodes)

    def conjunto_arestas(self):
        return self.conexao

class GeraGrafo:  # grafo cacique
    def __init__(self, k):
        self.caciques = []  # Cria uma lista para armazenar os caciques.
        self.caciques2 = []  # Cria outra lista para armazenar os caciques.
        self.numero_caciques = k  # Número de caciques.

    def listaNodeCacique(self):
        cont = 0
        # Percorre de 1 até o número de caciques.
        for j in range(1, int(self.numero_caciques) + 1):
            self.caciques.append(j + cont)  # Adiciona os caciques a lista.
            self.caciques2.append(j + cont)  # Adiciona os caciques a lista.
            cont = cont + j

        print("O número dos nodes de cada cacique é", self.caciques)

    def criaGrafo(self):
        # self.grafo = nx.DiGraph()  # Inicia o grafo.
        self.grafo = Rede()
        # self.grafo.add_nodes_from(self.caciques)  # Adiciona os nós dos caciques.
        # print(self.caciques)
        self.grafo.adiciona_nodes(self.caciques)

        count = 0
        for i in self.caciques:  # Percorre a lista dos caciques para fazer a conexão entre os mesmos.
            count = count + 1
            for p in self.caciques[count:]:  # Percorre de count pra frente.
                # self.grafo.add_edge(i, p)  # Cria uma conexão (aresta) entre i e p.
                self.grafo.adiciona_conexao((i, p))
                # self.grafo.add_edge(p, i)  # Cria uma conexão (aresta) entre p e i.
                self.grafo.adiciona_conexao((p, i))
                # Aqui é importante fazer duas conexões, pois as conexões no grafo
                # cacique-tribo são dadas por conexões mútuas.

        cont = 1
        while len(self.caciques) != 0:
            for t in self.caciques:  # Faz a conexão entre os caciques e os respectivos índios.
                # self.grafo.add_edge(t, t + cont)
                self.grafo.adiciona_conexao((t, t+cont))
                # self.grafo.add_edge(t + cont, t)
                self.grafo.adiciona_conexao((t+cont, t))
            del self.caciques[0]
            cont = cont + 1

        nova_lista = []  # Cria uma nova lista que guardará os índios.
        # for i in self.grafo.edges():  # Percorre todas as conexões.
        for i in self.grafo.conjunto_arestas():
            x = list(i)  # É preciso converter para lista, pois as conexões são tuplas.
            if (x[0] and x[1]) in self.caciques2:  # Se os dois valores forem caciques, então o loop é reiniciado.
                continue
            # Verifica se o x[0] é cacique e se x[1] não já foi adicionado a nova_lista
            elif x[0] in self.caciques2 and x[1] not in nova_lista:
                nova_lista.append([x[1], x[0]])  # Coloca o cacique como segundo elemento.
            # Verifica se o x[1] é cacique e se x[0] não já foi adicionado a nova_lista
            elif x[1] in self.caciques2 and x[0] not in nova_lista:
                nova_lista.append([x[0], x[1]])  # Coloca o cacique como segundo elemento.

        for i in self.caciques2:  # Percorre a segunda lista de caciques.
            list2 = []  # Cria outra nova lista para guardar só os índios.
            for x in nova_lista:  # Percorre a nova_lista procurando o cacique igual a i.
                if x[1] == i:
                    list2.append(x[0])  # Appenda a list2 com o índio desse cacique i.
            for z in range(len(list2) - 1):  # Percorre a list2 até o penúltimo valor.
                for k in range(z, len(list2)):  # Percorre list2 de z até o último valor.
                    if list2[z] != list2[k]:  # Para que não seja feita conexões de um índio consigo mesmo.
                        # self.grafo.add_edge(list2[z], list2[k])  # Liga um índio ao outro.
                        self.grafo.adiciona_conexao((list2[z], list2[k]))
                        # self.grafo.add_edge(list2[k], list2[z])  # Liga um índio ao outro.
                        self.grafo.adiciona_conexao((list2[k], list2[z]))

        return self.grafo  # Retorna o grafo.

    def n_nodes(self):  # Gera o número de nodes (nós) existentes no grafo.
        # return self.grafo.number_of_nodes()
        return self.grafo.numero_total_nodes()

    def arestas(self):  # Gera as arestas (conexões) existentes no grafo.
        # return self.grafo.edges()
        return self.grafo.conjunto_arestas()

    # def posicao(self):  # Gera a posição do grafo.
        # self.posicao = nx.spring_layout(self.grafo, dim=3)
        # return self.posicao

class GeraGrafoAleatorio:
    def __init__(self, X):
        self.X = X

    def gera_grafo(self):  # Grafo aleatório
        # G = nx.DiGraph()
        G = Rede()

        for i in range(1, self.X + 1):  # Cria x bolinhas, do 1 até o X.
            # G.add_node(i)
            G.adiciona_node(i)

        for k in range(1, self.X + 1):  # Varre os nodes para fazer as ligações.
            lista_numero_ligacoes = random.sample(range(1, self.X + 1), random.randrange(1, self.X - 1))
            for j in lista_numero_ligacoes:  # Determina com quem o node será ligado.
                if k == j:  # Se a ligação for com ele mesmo, passa.
                    pass
                else:
                    # G.add_edge(k, j)
                    G.adiciona_conexao((k,j))

        for k in range (1,self.X+1):
            ligacao_obrigatoria = random.choice([i for i in range (1,self.X+1) if i not in [k]])
            # G.add_edge(ligacao_obrigatoria, k)
            G.adiciona_conexao((ligacao_obrigatoria, k))

        Grafo2 = []
        # for k in G.edges():
        for k in G.conjunto_arestas():
            Grafo2.append(list(k))

        # n_nodes2 = nx.Graph.number_of_nodes(G)
        n_nodes2 = G.numero_total_nodes()
        # arestas2 = G.edges()
        arestas2 = G.conjunto_arestas()
        # posicao2 = nx.spring_layout(G, dim=3)

        return Grafo2, n_nodes2, arestas2 #, posicao2

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
        Sn = 1/(max(self.L)+1)
        alpha = 0.15
        constante_2 = 1 - alpha
        Y = [1/(max(self.L)+1) for i in range(max(self.L)+1)]
        Erro = 1 # Definido assim para entrar no while.

        while abs(Erro) >= 1e-5:
            Z_k1 = [0 for i in range(max(self.L) + 1)]

            for k in range(len(self.L)):
                Z_k1[self.L[k]] += self.V[k] * Y[self.C[k]]
            for i in range(len(Z_k1)):
                Z_k1[i] = Z_k1[i]*constante_2
                Z_k1[i] = Z_k1[i] + (alpha*Sn)
            # Z_k1 == x^(k+1)
            # Y[i] == x^k

            norma_1_diferenca = 0
            for i in range(len(Z_k1)):
                norma_1_diferenca += (abs(Z_k1[i] - Y[i]))
            Erro = (self.constante / (1 - self.constante)) * norma_1_diferenca
            # print("\nErro =", Erro)

            Y = Z_k1[:]
        return Z_k1
