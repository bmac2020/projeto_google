#!/usr/bin/python3

from models import GeraGrafo
from core import GeraMatriz
from views import MostraMatriz

def main():
    k = input("Digite o k: ")
    grafo = GeraGrafo(k)
    grafo.listaNodeCacique()
    grafo.criaGrafo()
    n_nodes = grafo.n_nodes()
    arestas = grafo.arestas()

    gera = GeraMatriz(grafo, n_nodes, arestas)
    matriz = gera.geraMatriz()

    print(MostraMatriz(matriz).mostraMatriz())

if __name__ == "__main__":
    main()
