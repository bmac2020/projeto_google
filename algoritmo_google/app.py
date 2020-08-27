#!/usr/bin/python3

from core import GeraGrafo, GeraMatriz, GeraGrafoAleatorio, GeraMatrizModificada, MatrizAuxiliar, Escalonamento, VetorX, Vetor_VLC, Constante, Solucao_Iterativa
from views import MostraVisualizacao, MostraMatriz, MostraMatrizModificada

def gera_matriz_inputada(arquivo):
    matriz_inputada = []
    try:
        arq = open(arquivo, "r") # Abre o arquivo.
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

def diferenca(Escalonamento, Iterativo):
    diferenca = []
    for k in range(len(Escalonamento)):
        diferenca.append(abs(Escalonamento[k]-Iterativo[k]))
    print("Diferença:", diferenca)

def funcao(matrizOriginal, matrizEsparsa, numero_nodes):
    M_M = GeraMatrizModificada(matrizOriginal, numero_nodes).cria_MM()
    # printa linha por linha com duas casas decimais
    # print("Matriz Modificada:\n")
    # MostraMatriz(M_M).mostraMatriz()

    # Constante C
    constante_c = Constante(M_M, numero_nodes).constante_C()
    # print("Esta é a constante C", constante_c)

    #### Matriz A
    Matriz_A_subtraida_identidade = MatrizAuxiliar(M_M, numero_nodes).cria_matrizaux()
    # printa linha por linha com duas casas decimais
    # print("Matriz Subtraída da Identidade:\n")
    # print(Matriz_A_subtraida_identidade)
    # MostraMatriz(Matriz_A_subtraida_identidade).mostraMatriz()

    ### Escalonando
    Matriz_Escalonada = Escalonamento(Matriz_A_subtraida_identidade, numero_nodes).escalona()
    # print("O valor de a",Escalonamento(n_nodes, Matriz_A_subtraida_identidade))
    # print("Matriz Escalonada:\n")
    # MostraMatriz(Matriz_Escalonada).mostraMatriz()

    ### Encontrando X
    Solucao_Escalonamento = VetorX(Matriz_Escalonada, numero_nodes).encontra_vetorx()
    print("\nVetor solução do modo escalonamento:", Solucao_Escalonamento)
    print("\nSoma solução escalonamento:", sum(Solucao_Escalonamento))


    # Vetores V L C
    V, L, C = Vetor_VLC(matrizEsparsa).vetor_VLC()

    # Solução Iterativa
    Solucao = Solucao_Iterativa(V, L, C, constante_c).solucao()
    print("\nvetor solução do modo iterativo", Solucao)
    print("\nSoma solução interativa: ", sum(Solucao))

    # Calcula a diferença dos dois métodos.
    diferenca(Solucao_Escalonamento, Solucao)

def main():
    print("-"*10)
    print("PageRank - Projeto Modelagem\n")
    print("Escolha uma opção:")
    print("[1] - Modelo cacique-tribo")
    print("[2] - Modelo grafo aleatório")
    print("[3] - Importar arquivo")
    print("[0] - Sair do programa")
    try:
        resposta = int(input("> "))
    except:
        print("Valor não númerico ou opção inválida.")
        exit()

    if resposta == 0:
        print("Saindo do programa...")
        exit()
    elif resposta == 1:
        print("\nModelo Cacique-Tribo")
        try:
            k = int(input("Digite o número de caciques: "))
        except:
            print("Valor não númerico ou opção inválida.")
            exit()
        # Gerando o grafo cacique.
        grafo = GeraGrafo(k)
        grafo.listaNodeCacique()
        grafo.criaGrafo()
        numero_nodes = grafo.n_nodes()
        arestas = grafo.arestas()
        # posicao = grafo.posicao()

        # Gerando a matriz com base no grafo.
        gera = GeraMatriz(grafo, numero_nodes, arestas)
        matriz = gera.geraMatriz()
        Matriz_Esparsa = []  # copiando matriz esparsa para fazer VLC
        Matriz_Esparsa = gera.geraMatriz()[:]

        funcao(matriz, Matriz_Esparsa, numero_nodes)
    elif resposta == 2:
        print("\nModelo Grafo Aleatório")
        try:
            k = int(input("Digite o número de nós: "))
        except:
            print("Valor não númerico ou opção inválida.")
            exit()
        # Gerando o grafo aleatório.
        # grafo2, n_nodes2, arestas2, posicao2 = Gera_Grafo_2(k)
        grafo2, n_nodes2, arestas2 = GeraGrafoAleatorio(k).gera_grafo()

        # Gerando a matriz com base no grafo.
        gera2 = GeraMatriz(grafo2, n_nodes2, arestas2)
        matriz2 = gera2.geraMatriz()
        matriz_esparsa2 = gera2.geraMatriz()[:]

        funcao(matriz2, matriz_esparsa2, n_nodes2)
    elif resposta == 3:
        print("\nImportação de Arquivo")
        try:
            nome_arq = input("Digite o nome do arquivo: ")
        except:
            print("\n")
            exit()

        # Gera a matriz inputada
        matriz = gera_matriz_inputada(nome_arq)

        # Se for retornado False, ficará em loop até encontrar o arquivo com nome correto.
        while matriz == False:
            print("Arquivo não encontrado.\n")
            nome_arq = input("Digite o nome do arquivo: ")
            matriz = gera_matriz_inputada(nome_arq)

        # Cria a matriz esparsa
        matriz_esparsa = matriz[:]
        numero_nodes = len(matriz[0]) # Número de nós (com base no número de colunas)

        funcao(matriz, matriz_esparsa, 8)
    print("-"*10)

if __name__ == "__main__":
    main()
