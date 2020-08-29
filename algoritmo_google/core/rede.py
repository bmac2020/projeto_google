#!/usr/bin/python3

class Rede:
    """
    Essa classe gera uma rede, onde guardará os nós e as conexões.

    Parâmetros:
        - node : nó.
        - nodes : lista de nós.
        - conexao : uma conexão entre nós.
        - conexoes : lista de conexões.

    Funções:
        - adiciona_node() : adiciona um nó a lista de nós da rede.
        - adiciona_nodes() : adiciona os nós de uma lista a lista de nós da rede.
        - adiciona_conexao() : adiciona uma conexao a lista de conexões da rede.
        - adiciona_conexoes() : adiciona as conexões de uma lista a lista de conexões da rede.
        - numero_total_nodes() : retorna o número total de nós da rede.
        - conjunto_arestas() : retorna todas as conexões da rede.
    """

    def __init__(self):
        self.nodes = [] # Lista de nós
        self.conexao = [] # Lista de conexões

    def adiciona_node(self, node): # Adiciona o nó na lista de nós.
        self.nodes.append(node)

    def adiciona_nodes(self, nodes): # Adiciona uma lista de nós.
        for node in nodes:
            if node not in self.nodes:
                self.nodes.append(node)

    def adiciona_conexao(self, conexao): # Adiciona uma conexão.
        if conexao not in self.conexao:
            if conexao[0] not in self.nodes: # Verifica se os nós dessa conexão não está na lista de nós.
                self.nodes.append(conexao[0])
            if conexao[1] not in self.nodes: # Verifica se os nós dessa conexão não está na lista de nós.
                self.nodes.append(conexao[1])
            self.conexao.append(conexao)

    def adiciona_conexoes(self, conexoes): # Adiciona uma lista de conexões.
        for i in conexoes:
            self.adiciona_conexao(i)

    def numero_total_nodes(self): # Retorna o número de nós da rede.
        return len(self.nodes)

    def conjunto_arestas(self): # Retorna todas as conexões da rede.
        return self.conexao
