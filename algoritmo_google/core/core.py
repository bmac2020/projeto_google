#!/usr/bin/python3

from .rede import Rede
import random

class GeraGrafo:  # Grafo cacique
    """
    Essa classe gera o grafo da rede cacique-tribo.

    Parâmetros:
        - k : Número de caciques.

    Funções:
        - listaNodeCacique() : gera duas listas com todos os caciques.
        - criaGrafo() : gera o grafo da rede e faz as conexões entre caciques e entre caciques e seus respectivos índios.
        - n_nodes() : retorna o número de nós (leia-se índios).
        - arestas() : retorna todas as conexões do grafo/rede.
    """
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
    """
    Essa classe gera o grafo da rede aleatória.

    Parâmetros:
        - X : número de nós que a rede terá.

    Funções:
        - gera_grafo() : gera o grafo da rede, com as conexões entre os nós, respeitando algumas regras:
            -
            -
            - E por fim, retorna o grafo, os números de nós da rede e as arestas.
    """
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
    """
    Essa classe gera a matriz de um grafo/rede, com os respectivos pesos.

    Parâmetros:
        - grafo : grafo/rede que será usada para gerar a matriz.
        - n_nodes : número de nós da rede.
        - arestas : conexões da rede.

    Funções:
        - geraMatriz() : percorre as conexões e cria matriz inicial trocando as
            ligações por 1, logo depois cria uma matriz com os respectivos pesos.
    """
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

        for k in range(len(matriz)): # Percorre as colunas da matriz.
            cont = 0 # Guarda a soma das colunas.
            for j in range(len(matriz)): # Percorre as linhas da matriz.
                if matriz[j][k] == 1: # Se o elemento for 1, então há ligação, logo é incrementado a variável cont.
                    cont += 1
            for i in range(len(matriz)): # Percorre as linhas da matriz.
                if matriz[i][k] == 1: # Se o elemento for 1, então divide esse elemento pela soma dos valores da coluna (normalização).
                    matriz[i][k] = 1/cont

        return matriz

class GeraMatrizModificada:
    """
    Essa classe modifica a matriz que foi criada na classe acima.

    Parâmetros:
        - matriz : matriz da rede.
        - n_nodes : números de nós da rede.
        - alpha : alpha inputado pelo usuário/padrão.

    Funções:
        - cria_MM() : cria uma nova matriz modificando os seus valores com base no cálculo:
                            MM = (1 - alfa)M + alfa*Sn.
    """
    def __init__(self, matriz, n_nodes, alpha):
        self.matriz = matriz # Define a matriz no escopo classe.
        self.n_nodes = n_nodes # Define o número de nós no escopo da classe.
        self.alpha = alpha # Define o alpha no escopo da classe.

    def cria_MM(self):
        alfa = self.alpha
        alfa_Sn = alfa * 1 / self.n_nodes  # Elementos da Matriz Sn.
        MM = []  # Matriz Modificada.
        MM[:] = self.matriz[:] # Faz uma cópia da matriz.

        for k in range(self.n_nodes): # Percorre as linhas da matriz.
            for i in range(self.n_nodes): # Percorre as colunas da matriz.
                MM[k][i] = (1 - alfa) * MM[k][i] + alfa_Sn # MM = (1 - alfa)M + alfa*Sn.

        return MM

class GeraMatrizInputada:
    """
    Essa classe gera a matriz do grafo inputado por um arquivo.

    Parâmetros:
        - arquivo : nome do arquivo com o grafo.

    Funções:
        - gera_matriz_inputada() : percorre o arquivo, transformando as linhas
                do mesmo em linhas de uma matriz e por último retorna uma
                matriz com os respectivos pesos.

    """
    def __init__(self, arquivo):
        self.arquivo = arquivo # Define o arquivo inputado no escopo da classe

    def gera_matriz_inputada(self):
        matriz_inputada = []
        try:
            arq = open(self.arquivo, "r") # Abre o arquivo.
            lines = arq.readlines() # Retorna uma lista que contém cada linha do arquivo como um item da lista.
        except:
            return False

        for linha in lines:
            linhas_matriz_inputada = []
            lin = linha[:len(linha)-1] # Variável que recebe cada linha do arquivo de texto original como uma string.
            v = lin.split('\t') # Variável que recebe a linha acima e a transforma em uma lista com n elementos.

            for i in range (len(v)):
                linhas_matriz_inputada.append(int(v[i]))
            matriz_inputada.append(linhas_matriz_inputada)

        arq.close()

        # Conta a quantidade de ligações de cada página.
        for k in range(len(matriz_inputada)):
            cont = 0
            for j in range(len(matriz_inputada)):
                if matriz_inputada[j][k] == 1:
                    cont += 1
            # Cria a matriz com os pesos.
            for i in range(len(matriz_inputada)):
                if matriz_inputada[i][k] == 1:
                    matriz_inputada[i][k] = 1 / cont

        return matriz_inputada
