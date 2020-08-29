#!/usr/bin/python3

from core.core import GeraGrafo, GeraMatriz, GeraGrafoAleatorio, GeraMatrizModificada, GeraMatrizInputada
from core.escalonamento import MatrizAuxiliar, Escalonamento, VetorX
from core.iterativo import Vetor_VLC, Constante, Solucao_Iterativa
from core.rede import Rede
import time, string, decimal

def Ranking(X): # Recebe vetor solução.
    X_ordenado = X[:] # Copia o vetor solução.
    X_ordenado.sort() # Ordena em ordem crescente o vetor solução.
    X_ordenado.reverse() # Inverte o vetor solução, ordenando de forma decrescente.

    lista_aux = []
    numeros = []
    ordenado = []

    for k in range(len(X)): # Percorre os elementos do vetor solução
        ind = int(X.index(X_ordenado[k])) # Guarda o índice do elemento X_ordenado[k].
        while ind in lista_aux: # Se o índice já estiver na lista, então procurasse a partir dele+1.
            ind = int(X.index(X_ordenado[k], ind+1))
        numero_pagina = X.index(X_ordenado[k], ind) # Encontra o índice da primeira ocorrência do valor.
        lista_aux.append(ind)
        numeros.append(numero_pagina+1) # Appenda os números da páginas, exemplo: página 0 será exibida como página 1 e assim por diante.
        ordenado.append(X_ordenado[k]) # Guarda o valor do elemento.

    return numeros, ordenado

def tabela(numeros1, ordenado1, numeros2, ordenado2, tempo, tempo1, iteracoes):
    print("-----------")
    print("Deseja visualizar quantas páginas?")
    print("[1] - Escolher um determinado número de páginas.")
    print("[2] - Todas as páginas.")
    print("[3] - Gerar um arquivo com todas as páginas.")

    resp = None
    while resp == None:
        try:
            resp = int(input("> "))
            if resp < 1 or resp > 3:
                resp = None
                print("O digitado deve corresponder a uma das opções acima.")
                continue
        except:
            resp = None
            print("O digitado deve corresponder a uma das opções acima.")
            continue

    if resp == 1:
        resp = None
        while resp == None:
            try:
                resp = int(input("Digite o número de páginas (no máximo %i): " % (len(numeros1))))
                if resp < 1 or resp > len(numeros1):
                    resp = None
                    print("O número de páginas deve ser um inteiro e estar entre 1 e %i" % (len(numeros1)))
                    continue
            except:
                resp = None
                print("O número de páginas deve ser um inteiro e estar entre 1 e %i" % (len(numeros1)))
                continue

        print("\nMétodo Escalonamento\t\t| Método Iterativo")
        print("Pos. \t| Pág. \t| Score \t| Pos. \t| Pág. \t| Score \t| Diferença")
        cont = 1
        for i in range(resp):
            print("%.2iº \t| %.2i \t| %.5f \t| %.2iº \t| %.2i \t| %.5f \t| %.3e" % (cont, numeros1[i], ordenado1[i], cont, numeros2[i], ordenado2[i], decimal.Decimal(abs(ordenado2[i]-ordenado1[i]))) )
            cont += 1
        print("Número de iterações do Método Iterativo:", str(iteracoes))
        print("Tempo de execução do Método de Escalonamento (em segundos):", str(tempo))
        print("Tempo de execução do Método Iterativo (em segundos):", str(tempo1))
    elif resp == 2:
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

    # Começa medir o tempo para o método de escalonamento.
    tempo_inicio = time.time()
    M_M = GeraMatrizModificada(matrizOriginal, numero_nodes, alpha).cria_MM()

    #### Matriz A
    Matriz_A_subtraida_identidade = MatrizAuxiliar(M_M, numero_nodes).cria_matrizaux()

    ### Escalonando
    Matriz_Escalonada = Escalonamento(Matriz_A_subtraida_identidade, numero_nodes).escalona()

    ### Encontrando X
    Solucao_Escalonamento = VetorX(Matriz_Escalonada, numero_nodes).encontra_vetorx()
    tempo_fim = time.time() # Para de contar o tempo do escalonamento.
    tempo = (tempo_fim - tempo_inicio) # Tempo passado.
    numeros1, ordenado1 = Ranking(Solucao_Escalonamento)

    # Começa contar tempo para o método iterativo.
    tempo_inicio1 = time.time()
    # Vetores V L C
    V, L, C = Vetor_VLC(matrizEsparsa).vetor_VLC()

    # Constante C
    constante_c = Constante(M_M, numero_nodes).constante_C()

    # Solução Iterativa
    Solucao, iteracoes = Solucao_Iterativa(V, L, C, constante_c, alpha).solucao()
    tempo_fim1 = time.time() # Para de contar o tempo para o iterativo.
    numeros2, ordenado2 = Ranking(Solucao)
    tempo1 = (tempo_fim1 - tempo_inicio1)

    tabela(numeros1, ordenado1, numeros2, ordenado2, tempo, tempo1, iteracoes)

def main():
    print("\t" + "-"*30)
    print("\tProjeto PageRank\n")
    print("\tEscolha uma opção:")
    print("\t[1] - Rede cacique-tribo")
    print("\t[2] - Importar arquivo")
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
                # Alpha que será passado como parametro para as funções.
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
        arestas = grafo.arestas()

        # Gerando a matriz com base no grafo.
        gera = GeraMatriz(grafo, numero_nodes, arestas)
        matriz = gera.geraMatriz()
        Matriz_Esparsa = [] # Copiando matriz esparsa para fazer VLC.
        Matriz_Esparsa = gera.geraMatriz()[:]

        procedimentos(matriz, Matriz_Esparsa, numero_nodes, float(alpha))

    elif resposta == 2:
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
    print("-"*10 + "\n")

if __name__ == "__main__":
    while True:
        main()
        try:
            resp = input("Deseja executar novamente? [S/N] ")
            if resp.lower() == "s":
                continue
            else:
                break
        except:
            print("Saindo do programa...")
            exit()
