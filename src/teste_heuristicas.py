from puzzle import PuzzleState
from heuristicas import h1, h2

# 🧩 Tabuleiro de teste do enunciado
estado_exemplo = PuzzleState([4, 3, 2, 8, 7, 5, 1, 6, 0])

print("🧪 Teste das Heurísticas\n")
print("Estado Atual:")
print(estado_exemplo)

# Calcula H1 e H2
valor_h1 = h1(estado_exemplo)
valor_h2 = h2(estado_exemplo)

print(f"H1 - Peças fora do lugar x2: {valor_h1}")
print(f"H2 - Soma das distâncias Manhattan x2: {valor_h2}")
