#!/usr/bin/python3

from core import GeraGrafo, GeraMatriz, GeraMatrizModificada, MatrizAuxiliar, Escalonamento, VetorX, Vetor_VLC
from views import MostraVisualizacao, MostraMatriz, MostraMatrizModificada

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
    mostra = MostraVisualizacao(vars(grafo)['grafo'], numero_nodes, posicao, arestas)
    mostra.gera3d()

    # Gerando a matriz com base no grafo.
    gera = GeraMatriz(grafo, numero_nodes, arestas)
    matriz = gera.geraMatriz()
    matriz_esparsa = []
    matriz_esparsa = matriz[:]

    # Exibindo a matriz.
    MostraMatriz(matriz).mostraMatriz()

    # Gerando a Matriz Modificada.
    matriz_modificada = GeraMatrizModificada(matriz, numero_nodes)
    matriz_modificada.cria_MM()

    # Mostra a Matriz Modificada.
    mostraModificada = MostraMatrizModificada(vars(matriz_modificada)['matriz'])
    mostraModificada.mostraModificada()

    # Gera a Matriz Auxiliar, que é a matriz subtraida pela Matriz Identidade.
    matriz_auxiliar = MatrizAuxiliar(vars(matriz_modificada)['matriz'], numero_nodes)
    matriz_auxiliar.cria_matrizaux()

    # Mostra a Matriz Auxiliar.
    MostraMatriz(vars(matriz_auxiliar)['matriz']).mostraMatriz()

    # Escalonamento.
    matriz_escalonada = Escalonamento(vars(matriz_auxiliar)['matriz'], numero_nodes)
    matriz_escalonada.escalona()

    # Mostra a matriz escalonada.
    MostraMatriz(vars(matriz_escalonada)['matriz']).mostraMatriz()

    # Encontrando o Vetor X.
    vetor_X = VetorX(vars(matriz_escalonada)['matriz'], numero_nodes)
    vetor_X.encontra_vetorx()

    # Vetores V, L, C.
    vetores = Vetor_VLC(matriz_esparsa)
    V, L, C = vetores.vetor_VLC()
    print("\nV:",V)
    print("\nL:", L)
    print("\nC:", C)

if __name__ == "__main__":
    main()
