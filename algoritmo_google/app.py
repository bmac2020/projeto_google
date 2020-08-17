#!/usr/bin/python3

from core import GeraGrafo, GeraMatriz
from views import MostraVisualizacao, MostraMatriz

def main():
    try:
        print("PageRank - Projeto Modelagem\n")
        k = int(input("Digite o número de caciques: "))
    except:
        print("Apenas valores inteiros.")
        exit()

    # Gerando o grafo.
    grafo = GeraGrafo(k)
    grafo.listaNodeCacique()
    grafo.criaGrafo()
    numero_nodes = grafo.n_nodes()
    arestas = grafo.arestas()
    posicao = grafo.posicao()

    # Exibindo o grafo em 3D.
    print("A visualização será exibida por 10 segundos.")
    mostra = MostraVisualizacao(vars(grafo)['grafo'], numero_nodes, posicao, arestas)
    mostra.gera3d()

    # Gerando a matriz com base no grafo.
    gera = GeraMatriz(grafo, numero_nodes, arestas)
    matriz = gera.geraMatriz()

    # Exibindo a matriz.
    MostraMatriz(matriz).mostraMatriz()

if __name__ == "__main__":
    main()
