#!/usr/bin/python3

class Constante:
    """
    Essa classe cria a constante que será usada para encontrar o erro da solução iterativa.

    Parâmetros:
        - matriz_modificada : será usada para obter os valores pra gerar a constante.
        - n_nodes : número de nós.

    Funções:
        - constante_C() : depois de percorrer a matriz modificada e fazer
                processos aritméticos, é retornado a constante C.
    """

    def __init__(self, matriz_modificada, n_nodes):
        self.matriz = matriz_modificada # Define a matriz modificada no escopo da classe.
        self.n_nodes = n_nodes # Define o número de nós no escopo da classe.

    def constante_C(self):
        lista_max = []
        min_coluna = self.matriz[0][0]

        for j in range(self.n_nodes): # Percorre as colunas da matriz.
            for i in range(self.n_nodes): # Percorre as linhas da matriz.
                if self.matriz[i][j] < min_coluna: # Verifica qual é o menor elemento da coluna.
                    min_coluna = self.matriz[i][j]
            lista_max.append(abs(1 - (2 * min_coluna))) # Adiciona na lista.
        return max(lista_max) # Retorna o máximo valor da lista.

class Vetor_VLC:
    """
    Essa classe gera os vetores V, L, C.

    Parâmetros:
        - matriz_esparsa : a matriz esparsa é usada para criação dos três vetores.

    Funções:
        - vetor_VLC() : retorna os vetores V, L, C, que são, respectivamente,
                elemento não nulo da matriz esparsa, índice da linha desse
                elemento e índice da coluna desse elemento.
    """
    def __init__(self, matriz_esparsa):
        self.matriz = matriz_esparsa # Define a matriz esparsa no escopo da classe.

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
    """
    Essa classe executa o método Iterativo.

    Parâmetros:
        - V : vetor que contém os elementos não nulos da matriz esparsa.
        - L : vetor que contém os índices da linha dos elementos não nulos.
        - C : vetor que contém os índices da coluna dos elementos não nulos.

    Funções:
        - solucao() : executa o processo Iterativo, normaliza o vetor solução
                e retorna esse vetor e no número de iterações.
    """

    def __init__(self, V, L, C, constante, alpha):
        self.V = V # Define o vetor V dentro do escopo da classe.
        self.L = L # Define o vetor L dentro do escopo da classe.
        self.C = C # Define o vetor C dentro do escopo da classe.
        self.constante = constante # Define a constante dentro do escopo da classe.
        self.alpha = alpha # Define o alpha dentro do escopo da classe.

    def solucao(self):
        Sn = 1/(max(self.L)+1) # Define o Sn como 1/N.
        alpha = self.alpha
        constante_2 = 1 - alpha
        Y = [1/(max(self.L)+1) for i in range(max(self.L)+1)] # Y é uma lista com vários "Sn"s.
        Erro = 1 # Definido assim para entrar no while.
        iteracoes = 0 # Números de iterações.

        while abs(Erro) >= 1e-5: # Enquanto o Erro é maior/igual que 1e-5, o loop é executado.
            Z_k = [0 for i in range(max(self.L) + 1)] # Zera Z_k em todo loop.

            # Percorre os valores de Z_k de índice igual ao elemento de L[k] e faz determinado operação aritmética.
            for k in range(len(self.L)):
                Z_k[self.L[k]] += self.V[k] * Y[self.C[k]]
            for i in range(len(Z_k)): # Percorre todo Z_k executando operações aritméticas.
                Z_k[i] = Z_k[i]*constante_2
                Z_k[i] = Z_k[i] + (alpha*Sn)

            norma_1_diferenca = 0
            for i in range(len(Z_k)): # Percorre Z_k e Y calculando a norma da soma (foi definida no pdf teórico).
                norma_1_diferenca += (abs(Z_k[i] - Y[i]))
            Erro = (self.constante / (1 - self.constante)) * norma_1_diferenca # Calcula o Erro.

            Y = Z_k[:] # Copia o Z_k.
            iteracoes += 1

        soma_lista = sum(Z_k)
        # Divide os pesos de cada elemento pela soma de todos os pesos.
        for k in range(len(Z_k)):
            Z_k[k] = Z_k[k] / soma_lista
        return Z_k, iteracoes
