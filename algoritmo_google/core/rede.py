#!/usr/bin/python3

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
