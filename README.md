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

- [ ] Modificação da matriz
  - [ ] Criar uma matriz S cujo tamanho é nxn e cujas as entradas são todas iguais a 1/n
  - [ ] Definir a componente <img align="center" src="https://i.upmath.me/svg/%5Calpha" alt="\alpha" /> (alpha) como 0.15
  - [ ] Resolver a equação:
      <img align="center" src="https://i.upmath.me/svg/MM%20%3D%20(1%20-%20%5Calpha)M%20%2B%20%5Calpha%20S" alt="MM = (1 - \alpha)M + \alpha S" />, onde MM é a matriz modificada (ou que está sendo modificada)

- [ ] Encontrando o vetor x
  - [ ] Vamos construir uma matriz auxiliar A que satisfaça a equação: <img align="center" src="https://i.upmath.me/svg/A%20%3D%20MM%20-%20I" alt="A = MM - I" />
  - [ ] Escalonar usando o algoritmo descrito pelo professor:

      Para k de 1 a n-1 faça
        Determine <img src="https://i.upmath.me/svg/i_k" alt="i_k" />
 tal que <img src="https://i.upmath.me/svg/%7Ca_%7Bi_k%2Ck%7D%7C%20%3D%20max_%7Bi%20%5Cge%20k%7D%7Ca_%7Bi%2Ck%7D%7C" alt="|a_{i_k,k}| = max_{i \ge k}|a_{i,k}|" />
        Se <img src="https://i.upmath.me/svg/i_k%20%5Cne%20k" alt="i_k \ne k" /> troque as linhas k e <img src="https://i.upmath.me/svg/i_k" alt="i_k" /> da matriz A
        Para i de k+1 a n faça
          <img src="https://i.upmath.me/svg/%5Calpha_i%20%3D%20a_%7Bi%2Ck%7D%2Fa_%7Bk%2Ck%7D" alt="\alpha_i = a_{i,k}/a_{k,k}" />
          Para j de k a n faça
            <img src="https://i.upmath.me/svg/a_%7Bi%2Cj%7D%20%3D%20a_%7Bi%2Cj%7D%20-%20%5Calpha_i%20*%20a_%7Bk%2Cj%7D" alt="a_{i,j} = a_{i,j} - \alpha_i * a_{k,j}" />
          Fim do para
        Fim do para
      Fim do para
  - [ ] Após escalonado, vamos atribuir valor arbitrário para o Xn e fazer o seguinte:

    Para k de n-1 a 1 com passo de -1 faça
      <img align="center" src="https://i.upmath.me/svg/x_k%20%3D%20(-%7B%5Csum_%7Bj%3Dk%2B1%7D%5Ena_%7Bk%2Cj%7Dx_j)%2Fa_%7Bk%2Ck%7D" alt="x_k = (-{\sum_{j=k+1}^na_{k,j}x_j)/a_{k,k}" />
  - [ ] Por fim, vamos normalizar a solução encontrada.

- [ ] Impressão (algumas ideias abaixo)
  - [ ] Imprimir um ranking com as páginas
  - [ ] Apresentação visual com as páginas representadas por círculas cujas tamanhos refletem as respectivas importâncias
  - [ ] Lista simples
