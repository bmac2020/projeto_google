#!/usr/bin/python3

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
    def __init__(self, V, L, C, constante, alpha):
        self.V = V
        self.L = L
        self.C = C
        self.constante = constante
        self.alpha = alpha

    def solucao(self):
        Sn = 1/(max(self.L)+1)
        alpha = self.alpha
        constante_2 = 1 - alpha
        Y = [1/(max(self.L)+1) for i in range(max(self.L)+1)]
        Erro = 1 # Definido assim para entrar no while.
        iteracoes = 0 #numeros iterações

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

            Y = Z_k1[:]
            iteracoes += 1

        soma_lista = sum(Z_k1)
        # divide os pesos de cada elemento pela soma de todos os pesos
        for k in range(len(Z_k1)):
            Z_k1[k] = Z_k1[k] / soma_lista
        return Z_k1, iteracoes
