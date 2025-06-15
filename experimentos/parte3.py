
# Experimentos Parte 3: Busca Gulosa vs A*

import csv
import sys
import os
sys.path.append(os.path.abspath("../src"))

from puzzle import gerar_estado_inicial
from funcoes_custo import custo_c1, custo_c2, custo_c3, custo_c4
from heuristicas import h1, h2
from algoritmos import busca_gulosa, busca_a_estrela

FUNCOES_CUSTO = {
    "C1": custo_c1,
    "C2": custo_c2,
    "C3": custo_c3,
    "C4": custo_c4
}

HEURISTICAS = {
    "H1": h1,
    "H2": h2
}

def rodar_experimento():
    with open("resultados_parte3.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "ID", "Algoritmo", "FuncaoCusto", "Heuristica",
            "CustoTotal", "Visitados", "Gerados", "TamanhoCaminho"
        ])

        for i in range(1, 31):
            estado_inicial = gerar_estado_inicial()
            print(f"\n🔁 Cenário {i}/30")

            # Busca Gulosa
            for nome_heur, func_heur in HEURISTICAS.items():
                print(f"➡️ Gulosa + {nome_heur}")
                resultado = busca_gulosa(estado_inicial, func_heur, custo_c1)  # qualquer custo para execução
                for nome_custo, func_custo in FUNCOES_CUSTO.items():
                    custo = calcular_caminho_customizado(resultado["caminho"], func_custo) if resultado["caminho"] else "inf"
                    tam_caminho = len(resultado['caminho']) - 1 if resultado['caminho'] else 0
                    writer.writerow([
                        i, "Gulosa", nome_custo, nome_heur, custo,
                        resultado['visitados'], resultado['gerados'], tam_caminho
                    ])

            # Busca A*
            for nome_custo, func_custo in FUNCOES_CUSTO.items():
                for nome_heur, func_heur in HEURISTICAS.items():
                    print(f"➡️ A* + {nome_custo} + {nome_heur}")
                    resultado = busca_a_estrela(estado_inicial, func_heur, func_custo)
                    custo = resultado['custo'] if resultado['caminho'] else "inf"
                    tam_caminho = len(resultado['caminho']) - 1 if resultado['caminho'] else 0
                    writer.writerow([
                        i, "A*", nome_custo, nome_heur, custo,
                        resultado['visitados'], resultado['gerados'], tam_caminho
                    ])

    print("\n✅ Resultados salvos em resultados_parte3.csv")

def calcular_caminho_customizado(caminho, funcao_custo):
    custo_total = 0
    for idx in range(1, len(caminho)):
        anterior, _ = caminho[idx - 1]
        atual, acao = caminho[idx]
        custo_total += funcao_custo(anterior, atual, acao)
    return custo_total

if __name__ == "__main__":
    rodar_experimento()
