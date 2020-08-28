#!/usr/bin/python3

from core.core import GeraGrafo, GeraMatriz, GeraGrafoAleatorio, GeraMatrizModificada, GeraMatrizInputada
from core.escalonamento import MatrizAuxiliar, Escalonamento, VetorX
from core.iterativo import Vetor_VLC, Constante, Solucao_Iterativa
from core.rede import Rede
from views import MostraVisualizacao, MostraMatriz, MostraMatrizModificada
import time, string, decimal

def Ranking(X):#recebe vetor solução
    X_ordenado = X[:]
    X_ordenado.sort()
    X_ordenado.reverse()

    lista_aux = []
    numeros = []
    ordenado = []

    for k in range(len(X)):
        ind = int(X.index(X_ordenado[k]))
        while ind in lista_aux:
            ind = int(X.index(X_ordenado[k], ind+1))
        numero_pagina = X.index(X_ordenado[k], ind) #encontra o indice da primeira ocorrência do valor
        lista_aux.append(ind)
        numeros.append(numero_pagina)
        ordenado.append(X_ordenado[k])

    return numeros, ordenado

def tabela(numeros1, ordenado1, numeros2, ordenado2, tempo, tempo1, iteracoes):
    print("-----------")
    print("Deseja visualizar quantas páginas?")
    print("[1] - Escolher um determinado número de páginas.")
    print("[2] - Todas as páginas.")
    print("[3] - Gerar um arquivo com todas as páginas.")
    resp = input("> ")

    if resp == "1":
        resp = input("Digite o número de páginas (no máximo %i): " % (len(numeros1)))

        print("\nMétodo Escalonamento\t\t| Método Iterativo")
        print("Pos. \t| Pág. \t| Score \t| Pos. \t| Pág. \t| Score \t| Diferença")
        cont = 1
        for i in range(int(resp)):
            print("%.2iº \t| %.2i \t| %.5f \t| %.2iº \t| %.2i \t| %.5f \t| %.3e" % (cont, numeros1[i], ordenado1[i], cont, numeros2[i], ordenado2[i], decimal.Decimal(abs(ordenado2[i]-ordenado1[i]))) )
            cont += 1
        print("Número de iterações do Método Iterativo:", str(iteracoes))
        print("Tempo de execução do Método de Escalonamento (em segundos):", str(tempo))
        print("Tempo de execução do Método Iterativo (em segundos):", str(tempo1))
    elif resp == "2":
        print("\nMétodo Escalonamento\t\t| Método Iterativo")
        print("Pos. \t| Pág. \t| Score \t| Pos. \t| Pág. \t| Score \t| Diferença")
        cont = 1
        for i in range(len(numeros1)):
            print("%.2iº \t| %.2i \t| %.5f \t| %.2iº \t| %.2i \t| %.5f \t| %.3e" % (cont, numeros1[i], ordenado1[i], cont, numeros2[i], ordenado2[i], decimal.Decimal(abs(ordenado2[i]-ordenado1[i]))) )
            cont += 1
        print("Número de iterações do Método Iterativo:", str(iteracoes))
        print("Tempo de execução do Método de Escalonamento (em segundos):", str(tempo))
        print("Tempo de execução do Método Iterativo (em segundos):", str(tempo1))
    else:
        with open("ranking.txt", "w", encoding="utf-8") as file:
            file.write("Método Escalonamento\t\t| Método Iterativo")
            file.write("\nPos. \t| Pág. \t| Score \t| Pos. \t| Pág. \t| Score \t| Diferença")
            cont = 1
            for i in range(len(numeros1)):
                file.write("\n%.2iº \t| %.2i \t| %.5f \t| %.2iº \t| %.2i \t| %.5f \t| %.3e" % (cont, numeros1[i], ordenado1[i], cont, numeros2[i], ordenado2[i], decimal.Decimal(abs(ordenado2[i]-ordenado1[i]))))
                cont += 1
            file.write("\nNúmero de iterações do Método Iterativo: %s" % (str(iteracoes)))
            file.write("\nTempo de execução do Método de Escalonamento (em segundos): %s" % str(tempo))
            file.write("\nTempo de execução do Método Iterativo (em segundos): %s" % (str(tempo1) + "\n"))
        print("O arquivo com o ranking foi criado com o nome: ranking.txt")

def procedimentos(matrizOriginal, matrizEsparsa, numero_nodes, alpha):
    M_M = GeraMatrizModificada(matrizOriginal, numero_nodes, alpha).cria_MM()
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
    tempo_inicio = time.time_ns()
    Solucao_Escalonamento = VetorX(Matriz_Escalonada, numero_nodes).encontra_vetorx()
    tempo_fim = time.time_ns()
    numeros1, ordenado1 = Ranking(Solucao_Escalonamento)
    tempo = (tempo_fim - tempo_inicio)/10e9
    # print("Tempo de execução do Método de Escalonamento (em segundos):", )

    # Vetores V L C
    V, L, C = Vetor_VLC(matrizEsparsa).vetor_VLC()

    # Solução Iterativa
    tempo_inicio1 = time.time_ns()
    Solucao, iteracoes = Solucao_Iterativa(V, L, C, constante_c, alpha).solucao()
    tempo_fim1 = time.time_ns()
    numeros2, ordenado2 = Ranking(Solucao)
    tempo1 = (tempo_fim1 - tempo_inicio1)/10e9
    # print("Tempo de execução do Método Iterativo (em segundos):", )

    tabela(numeros1, ordenado1, numeros2, ordenado2, tempo, tempo1, iteracoes)

def main():
    print("\t" + "-"*30)
    print("\tProjeto PageRank\n")
    print("\tEscolha uma opção:")
    print("\t[1] - Rede cacique-tribo")
    print("\t[2] - Rede aleatória")
    print("\t[3] - Importar arquivo")
    print("\t[0] - Sair do programa")

    resposta = ""
    while resposta == "":
        try:
            resposta = int(input("> "))
        except:
            print("Valor não númerico ou opção inválida.")
            continue

    if resposta == 0:
        print("Saindo do programa...")
        exit()
    elif resposta == 1:
        print("\nModelo Cacique-Tribo")
        k = ""
        while k == "":
            try:
                #alfa q será passado como parametro para as funções
                alpha = input("\nInsira o valor de alpha (aperte enter para alpha padrão 0.15): ")
                for letra in alpha.lower():
                    if letra in string.ascii_lowercase:
                        assert()

                if alpha == "":
                    alpha = 0.15
                if float(alpha) < 0 or float(alpha) > 1:
                    print("Valor não númerico ou negativo.")
                    print("Valor do alpha precisa estar entre 0 e 1.")
                    continue
                k = input("Digite o número de caciques: ")
                if int(k) < 1:
                    k = ""
                    print("Valor não númerico ou negativo.")
                    continue
            except:
                k = ""
                print("Valor não númerico ou negativo.")
                continue

        # Gerando o grafo cacique.
        grafo = GeraGrafo(k)
        grafo.listaNodeCacique()
        grafo.criaGrafo()
        numero_nodes = grafo.n_nodes()
        # posicao = grafo.posicao()
        arestas = grafo.arestas()

        # Gerando a matriz com base no grafo.
        gera = GeraMatriz(grafo, numero_nodes, arestas)
        matriz = gera.geraMatriz()
        Matriz_Esparsa = []  # copiando matriz esparsa para fazer VLC
        Matriz_Esparsa = gera.geraMatriz()[:]

        procedimentos(matriz, Matriz_Esparsa, numero_nodes, float(alpha))


    elif resposta == 2:
        print("\nModelo Grafo Aleatório")
        k = ""
        while k == "":
            try:
                alpha = input("\nInsira o valor de alpha (aperte enter para alpha padrão 0.15): ")
                for letra in alpha.lower():
                    if letra in string.ascii_lowercase:
                        assert()

                if alpha == "":
                    alpha = 0.15
                if float(alpha) <= 0 or float(alpha) > 1:
                    print("Valor não númerico, negativo ou opção inválida.")
                    print("Valor do alpha precisa estar entre 0 e 1.")
                    continue

                k = input("Digite o número de nós: ")
                if int(k) < 1:
                    k = ""
                    print("Valor não númerico ou negativo.")
                    continue
            except:
                k = ""
                print("Valor não númerico ou negativo.")
                continue

        # Gerando o grafo aleatório.
        # grafo2, n_nodes2, arestas2, posicao2 = Gera_Grafo_2(int(k))
        grafo2, n_nodes2, arestas2 = GeraGrafoAleatorio(int(k)).gera_grafo()

        # Gerando a matriz com base no grafo.
        gera2 = GeraMatriz(grafo2, n_nodes2, arestas2)
        matriz2 = gera2.geraMatriz()
        matriz_esparsa2 = gera2.geraMatriz()[:]

        procedimentos(matriz2, matriz_esparsa2, n_nodes2, float(alpha))

    elif resposta == 3:
        print("\nImportação de Arquivo")
        nome_arq = ""
        while nome_arq == "":
            try:
                alpha = input("\nInsira o valor de alpha (aperte enter para alpha padrão 0.15): ")
                for letra in alpha.lower():
                    if letra in string.ascii_lowercase:
                        assert()
                if alpha == "":
                    alpha = 0.15
                if float(alpha) <= 0 or float(alpha) > 1:
                    print("Valor não númerico, negativo ou opção inválida.")
                    print("Valor do alpha precisa estar entre 0 e 1.")
                    continue

                nome_arq = input("Digite o nome do arquivo: ")
            except:
                print("Valor não númerico ou negativo.")
                continue

        # Gera a matriz inputada
        matriz = GeraMatrizInputada(nome_arq).gera_matriz_inputada()

        # Se for retornado False, ficará em loop até encontrar o arquivo com nome correto.
        while matriz == False:
            print("Arquivo não encontrado.\n")
            nome_arq = input("Digite o nome do arquivo: ")
            matriz = GeraMatrizInputada(nome_arq).gera_matriz_inputada()

        # Cria a matriz esparsa
        matriz_esparsa = matriz[:]
        numero_nodes = len(matriz[0]) # Número de nós (com base no número de colunas)

        procedimentos(matriz, matriz_esparsa, numero_nodes, float(alpha))
    print("-"*10)

if __name__ == "__main__":
    while True:
        main()
        resp = input("Deseja executar novamente? [S/N] ")
        if resp.lower() == "s":
            continue
        else:
            break
