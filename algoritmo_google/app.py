#!/usr/bin/python3

from models import GeraGrafo

def main():
    k = input("Digite o k: ")
    grafo = GeraGrafo(k)
    grafo.listaNodeCacique()
    grafo.criaGrafo()
    print(grafo.edges())

if __name__ == "__main__":
    main()
