# 🕹️ Puzzle do 8 em Python

Puzzle do 8 (joguinho de deslocar blocos) desenvolvido em Python. Usa um busca cega ou busca orientada(IA) para tentar encontrar uma solução para o problema.
A capacidade do algoritmo resolver o problema é bem limitada, geralmente não conseguindo gerar um resultado quando são necessários 20 ou mais movimentos

# ⚙️ Como Executar o Projeto?

É muito simples: basta ter instalado o Python, em sua versão mais recente, no seu computador, e também ter instalado o pacote Tkinter
Para isso, basta executar o seguinte no terminal:

```
pip install tkinter
```

Feito isso, acesse a pasta principal do projeto e execute o programa com 

```
python Main.py
```

# 🖼️ Mostrando o Projeto

<h2><Strong>Formato Inicial: </Strong></h2>
<p align="center">
  <img src="https://github.com/CodeByBreno/8-Puzzle-Game-IA-Python/assets/132024181/ab3980a1-1efc-475b-b529-a07e63482f3b" width="800" alt="jogodavelha">
</p>

A interface conta com:
- Tabuleiro
- Log (mostra o resultado da tentativa de resolver o puzzle - feita pelo computador, quando solicitado - ) 
- Botão para pedir ao computador que solucione o problema
- Botão para Mostrar Números : Apresente um número relativo à cada peça (o objetivo é deixar os números em ordem )
- Botão para Embaralhar o Jogo
- Botão para Reiniciar (Restaurar o Caso Original)
  
<h2><Strong>Jogo Bagunçado: </Strong></h2>
<p align="center">
  <img src="https://github.com/CodeByBreno/8-Puzzle-Game-IA-Python/assets/132024181/35e05f0c-7a33-4dfd-acc1-e6d05d290572" width="800" alt="jogodavelha">
</p>

O jogador pode mover as peças adjacentes ao espaço vazio (peça escurecida) clicando na peça desejada ou usado W-A-S-D no teclado

<h2><Strong>Exemplo de Caso com Resolução: (e Números no Tabuleiro) </Strong></h2>
<p align="center">
  <img src="https://github.com/CodeByBreno/8-Puzzle-Game-IA-Python/assets/132024181/fc56966d-8077-4ef9-a0e2-f620cdef1d9c" width="800" alt="jogodavelha">
</p>

Nesse caso, o algoritmo de busca foi capaz de encontrar uma sequência de passos que soluciona o problema, e essa foi apresentada no log

<h2><Strong>Exemplo de Caso sem Resolução: </Strong></h2>
<p align="center">
  <img src="https://github.com/CodeByBreno/8-Puzzle-Game-IA-Python/assets/132024181/7c124fea-106e-4458-9fb7-102de5adce40" width="800" alt="jogodavelha">
</p>

Já nesse caso, o problema era complexo demais e o algoritmo não conseguiu encontrar uma resposta até a profundidade tentada

# 📝 Personalizando o Funcionamento

<h2><Strong>global_data.py</Strong></h2>
<p align="center">
  <img src="https://github.com/CodeByBreno/8-Puzzle-Game-IA-Python/assets/132024181/88c9dfc0-c37d-4527-b037-af2db977d738" width="800" alt="jogodavelha">
</p>

No arquivo acima é possível personalizar algumas coisas a respeito do funcionamento do código:
- <p>Primeiro, que o algoritmo de busca utilizará o mecanismo especificado em SEARCH_TYPE, podendo ser de três tipos: DEPTH, WIDTH e PRIORITY. Os dois primeiros são buscas cegas em profundidade e largura, respectivamente. O terceiro é uma busca orientada por uma heurística - uma busca gulosa - que seguem preferencialmente por caminhos que possuem um maior número de peças corretas </p>
- Além disso, existe uma configuração (MAX_LEVELS) que determina a profundidade máxima que o algoritmo irá alcançar - isso é equivalente ao máximo de jogadas seguidas que ele pode fazer -. Colocar valores maiores que 10 geralmente faz o algoritmo demorar demais para processar a entrada. Lembrando que ele deverá tentar 3^MAX_LEVELS (em média) possibilidades antes de gerar um resultado. Assim, com o valor de 20, serão explorados 3.486.784.401 casos diferentes!
- As demais são variáveis menos relevantes: <Strong>buttons_grid</Strong> é usada para determinar quais peças mudaram ao fazer uma jogada, <Strong>DEFAULT_GRID</Strong> é a organização inicial do jogo e <Strong>texto_resposta</Strong> é o texto padrão mostrado no log 

