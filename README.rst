Projeto Google
==============

O algoritmo de busca do Google e sua relação com a Álgebra Linear

Breve Resumo:
-------------

Este projeto tenta reconstruir o algoritmo de busca do Google por meio
de um processo de classificação de páginas, batizado pelos criadores do
Google de "PageRank".

O critério de classificação seria o grau de importância de cada página
em relação a uma possível busca de palavra-chave realizada em uma rede
fictícia.

Por exemplo: um site teria uma classificação maior quando muitos outros
hyperlinks vindos de outros sites apontasse para ele.

O projeto foi divido em duas etapas distintas (chamadas de Tarefa 1 e
Tarefa 2) utilizando dois métodos diferente para a resolução:

    - escalonamento de matriz utilizando eliminação Guassiana;
    - método iterativo de multiplicação de matriz por vetores, também conhecido como Power Method.

A Tarefa 1 consistia em classificar uma rede qualquer que é representado
por um grafo orientado, onde os vértices são páginas da internet e as
arestas são as ligações orientadas entre elas.

A Tarefa 2 consistia em classificar uma rede do tipo cacique-tribo, onde
os caciques representariam as páginas da internet que possuem um
subconjunto de páginas (índios) conectado a ela e também ligados entre
si, mas que não estão conectados a outros grupos de páginas de outros
caciques.

Modos de usar o programa:
-------------------------

1. Clone/baixe o repositório.
2. Verifique se o Python 3 está instalado em sua máquina.
3. Execute o programa com: ``python algoritmo_google/app.py``

Sobre a entrada de dados:
-------------------------

O programa disponibiliza duas formas de entrada de dados: 1. Gerar uma
rede cacique-tribo escolhendo um número N de caciques. 2. Ler um arquivo
de texto.

Caso opte pela segunda opção:

O arquivo de texto deve conter uma matriz quadrada com "zeros" e "uns",
onde os "zeros" representam ausência de conexão entre as páginas e os
"uns" representam existência de conexão, conforme arquivos de exemplos
incluidos no diretório ``algoritmo_google/tests``.

Esse arquivo que conterá a matriz deve ter os elementos separados por
EXATAMENTE UM "tab" e no final da ÚLTIMA LINHA deve conter EXATAMENTE UM
caractere de espaço.

Algumas outras regras para a construção desse arquivo:

    - AS DIAGONAIS DEVEM SER NULAS.
    - NÃO SE PODE TER UMA LINHA OU COLUNA ZERADAS.
