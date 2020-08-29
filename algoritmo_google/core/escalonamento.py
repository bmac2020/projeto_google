#!/usr/bin/python3

class MatrizAuxiliar:
    """
    Essa classe gera a matriz subtraída pela matriz Identidade.

    Parâmetros:
        - matriz_modificada : matriz original/esparsa que sofreu modificações.
        - n_nodes : número de nós.

    Funções:
        - cria_matrizaux() : retorna a matriz auxiliar após a diagonal da
                matriz modificada ser subtraída pela matriz Identidade.

    """

    def __init__(self, matriz_modificada, n_nodes):
        self.matriz = matriz_modificada # Define a matriz modificada no escopo da classe.
        self.n_nodes = n_nodes # Define o número de nós no escopo da classe.

    def cria_matrizaux(self):
        matriz_aux = []
        matriz_aux = self.matriz[:] # Copia a matriz.

        for k in range(self.n_nodes): # Percorre as diagonais.
            matriz_aux[k][k] = matriz_aux[k][k] - 1 # Subtrai 1 da diagonal principal.

        return matriz_aux

class Escalonamento:
    """
    Essa classe realiza o processo de escalonamento usando o método de Gauss.

    Parâmetros:
        - matriz_aux : matriz auxiliar que será escalonada.
        - n_nodes :  número de nós.

    Funções:
        - escalona() : realiza o escalonamento da matriz auxiliar pelo método
                de Gauss e, por fim, retorna a matriz escalonada.
    """
    def __init__(self, matriz_aux, n_nodes):
        self.matriz = matriz_aux # Define a matriz auxiliar no escopo da classe.
        self.n_nodes = n_nodes # Define o número de nós no escopo da classe.

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
    """
    Essa classe encontra o vetor X, que é os valores das incógnitas.

    Parâmetros:
        - matriz_escalonada : matriz que sofreu o processo de escalonamento.
        - n_nodes : número de nós.

    Funções:
        - encontra_vetorx() : encontra os valores das incógnitas do vetor X
                e normaliza os mesmos.
    """
    def __init__(self, matriz_escalonada, n_nodes):
        self.matriz = matriz_escalonada # Define a matriz escalonada no escopo da classe.
        self.n_nodes = n_nodes # Define o número de nós no escopo da classe.

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

        return lista_x_k
