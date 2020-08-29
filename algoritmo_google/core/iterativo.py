#!/usr/bin/python3

class Constante:
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
            Z_k1 = [0 for i in range(max(self.L) + 1)] # Zera Z_k1 em todo loop.

            # Percorre os valores de Z_k1 de índice igual ao elemento de L[k] e faz determinado operação aritmética.
            for k in range(len(self.L)):
                Z_k1[self.L[k]] += self.V[k] * Y[self.C[k]]
            for i in range(len(Z_k1)): # Percorre todo Z_k1 executando operações aritméticas.
                Z_k1[i] = Z_k1[i]*constante_2
                Z_k1[i] = Z_k1[i] + (alpha*Sn)

            norma_1_diferenca = 0
            for i in range(len(Z_k1)): # Percorre Z_k1 e Y calculando a norma da soma (foi definida no pdf teórico).
                norma_1_diferenca += (abs(Z_k1[i] - Y[i]))
            Erro = (self.constante / (1 - self.constante)) * norma_1_diferenca # Calcula o Erro.

            Y = Z_k1[:] # Copia o Z_k1.
            iteracoes += 1

        soma_lista = sum(Z_k1)
        # Divide os pesos de cada elemento pela soma de todos os pesos.
        for k in range(len(Z_k1)):
            Z_k1[k] = Z_k1[k] / soma_lista
        return Z_k1, iteracoes
