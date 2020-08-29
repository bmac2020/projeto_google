# Projeto Google
O algoritmo de busca do Google e sua relação com a Álgebra Linear

## Checklist

- [x] Obtenção da matriz M
  - [x] Entrada de dados
  - [x] Gerar uma matriz aleatória
  - [x] Solicitar input do usuário para o tamanho da matriz
  - [x] Gerar uma matriz aleatória com base no input do usuário
  - [x] Gerar um grafo orientado aleatório
  - [x] Imprimir graficamente a composição do grafo
  - [x] Gerar a matriz de entrada utilizando a equação de importância das páginas:

      <img align="center" src="https://i.upmath.me/svg/x_k%20%3D%20%5Csum_%7Bj%20%5Cin%20L_k%7D%20%7Bx_j%20%5Cover%20n_j%7D" alt="x_k = \sum_{j \in L_k} {x_j \over n_j}" />

- [x] Modificação da matriz
  - [x] Criar uma matriz S cujo tamanho é nxn e cujas as entradas são todas iguais a 1/n
  - [x] Definir a componente <img align="center" src="https://i.upmath.me/svg/%5Calpha" alt="\alpha" /> (alpha) como 0.15
  - [x] Resolver a equação:

      <img align="center" src="https://i.upmath.me/svg/MM%20%3D%20(1%20-%20%5Calpha)M%20%2B%20%5Calpha%20S" alt="MM = (1 - \alpha)M + \alpha S" />, onde MM é a matriz modificada (ou que está sendo modificada)

- [x] Encontrando o vetor x
  - [x] Vamos construir uma matriz auxiliar A que satisfaça a equação:

      <img align="center" src="https://i.upmath.me/svg/A%20%3D%20MM%20-%20I" alt="A = MM - I" />

  - [x] Escalonar usando o algoritmo descrito pelo professor:

      <img src="https://i.imgur.com/H2cEXHj.png">

  - [x] Após escalonado, vamos atribuir valor arbitrário para o Xn e fazer o seguinte:

    Para k de n-1 a 1 com passo de -1 faça

      <img align="center" src="https://i.upmath.me/svg/x_k%20%3D%20(-%7B%5Csum_%7Bj%3Dk%2B1%7D%5Ena_%7Bk%2Cj%7Dx_j)%2Fa_%7Bk%2Ck%7D" alt="x_k = (-{\sum_{j=k+1}^na_{k,j}x_j)/a_{k,k}" />

  - [x] Por fim, vamos normalizar a solução encontrada.

- [x] Impressão (algumas ideias abaixo)
  - [x] Imprimir um ranking com as páginas
