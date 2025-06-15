# Algoritmos de Busca no 8-Puzzle


## 1. Introdução

Este relatório apresenta o desenvolvimento e a análise de diferentes algoritmos de busca aplicados ao problema do 8-Puzzle, como parte do trabalho avaliativo AT1 da disciplina de Inteligência Artificial (UFC Quixadá, 2025.1). O objetivo é estudar o desempenho de algoritmos clássicos em diferentes configurações de função de custo e heurísticas.

---

## 2. Objetivos

- Implementar os algoritmos: Largura (A1), Profundidade (A2), Custo Uniforme (A3), Gulosa (A4) e A* (A5)
- Aplicar diferentes funções de custo (C1 a C4) e heurísticas (H1 e H2)
- Realizar experimentos para avaliar o desempenho, custo e eficiência dos algoritmos
- Documentar os resultados com base em dados reais coletados automaticamente

---

## 3. Implementação

O sistema foi desenvolvido em Python 3, utilizando bibliotecas padrão (`heapq`, `deque`, `csv`). O projeto foi modularizado em arquivos para representar os estados, funções de custo, heurísticas e algoritmos. Cada algoritmo aceita funções e suporta randomização dos operadores.

---

## 4. Algoritmos de Busca

| Código | Nome                   | Tipo           |
|--------|------------------------|----------------|
| A1     | Busca em Largura       | Não-informado  |
| A2     | Busca em Profundidade  | Não-informado  |
| A3     | Busca de Custo Uniforme| Informado (g)  |
| A4     | Busca Gulosa           | Informado (h)  |
| A5     | Busca A*               | Informado (g+h)|

---

## 5. Heurísticas e Funções de Custo

### Heurísticas:
- **H1**: Número de peças fora do lugar ×2
- **H2**: Soma das distâncias Manhattan ×2

### Funções de custo:
- **C1**: Todas as ações = 2
- **C2**: Verticais = 2, Horizontais = 3
- **C3**: Verticais = 3, Horizontais = 2
- **C4**: Igual à C2, mas ir para o centro = 5

---

## 6. Metodologia Experimental

Experimentos divididos em 4 partes:

| Parte | Descrição |
|-------|-----------|
| Parte 1 | A1, A2, A3 com C1–C4 (30 estados) |
| Parte 2 | A3 vs A* com C1–C4 e H1/H2 |
| Parte 3 | Gulosa vs A* com C1–C4 e H1/H2 |
| Parte 4 | DFS e BFS com vizinhança aleatória (10x cada em 15 estados) |

Cada execução salva: custo, nós visitados, gerados, e tamanho do caminho.

---

## 7. Análise dos Resultados

Os resultados mostraram que:
- **A\*** com H2 teve o melhor desempenho geral
- **Busca Gulosa** foi rápida, mas menos confiável
- **Profundidade** sofreu com instabilidade devido à ordem de operadores
- **Randomização** impactou fortemente o desempenho da DFS e BFS

---

## 8. Considerações Finais

Este trabalho reforçou a importância de escolher algoritmos e heurísticas adequadas ao problema. A modularidade do código permitiu executar mais de 2.000 experimentos automatizados com consistência. O A* mostrou-se o algoritmo mais eficiente e robusto.

---

## 9. Apêndice

- Scripts de experimentação: `experimento_parte1.py` a `parte4.py`
- Resultados: `resultados_parte1.csv`, `parte2.csv`, etc.
- Código-fonte: `src/algoritmos.py`, `heuristicas.py`, `puzzle.py`
- Repositório: https://github.com/avelinofaco/inteligencia-artificial-buscas-8puzzle.git

---
