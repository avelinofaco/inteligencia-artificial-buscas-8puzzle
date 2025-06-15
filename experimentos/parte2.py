
# Experimentos Parte 2: Busca de Custo Uniforme e A* 

import csv
import sys
import os
sys.path.append(os.path.abspath("../src"))

from puzzle import gerar_estado_inicial
from funcoes_custo import custo_c1, custo_c2, custo_c3, custo_c4
from heuristicas import h1, h2
from algoritmos import busca_custo_uniforme, busca_a_estrela

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
    with open("resultados_parte2.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "ID", "Algoritmo", "FuncaoCusto", "Heuristica",
            "CustoTotal", "Visitados", "Gerados", "TamanhoCaminho"
        ])

        for i in range(1, 31):  # 30 estados
            estado_inicial = gerar_estado_inicial()
            print(f"\n🔁 Executando cenário {i}/30...")

            # A3: Busca de Custo Uniforme (sem heurística)
            for nome_custo, func_custo in FUNCOES_CUSTO.items():
                print(f"➡️ CustoUniforme + {nome_custo}")
                resultado = busca_custo_uniforme(estado_inicial, func_custo)
                custo = resultado['custo'] if resultado['caminho'] else "inf"
                tam_caminho = len(resultado['caminho']) - 1 if resultado['caminho'] else 0
                writer.writerow([
                    i, "CustoUniforme", nome_custo, "-", custo,
                    resultado['visitados'], resultado['gerados'], tam_caminho
                ])

            # A5: Busca A*
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

    print("\n Resultados salvos em resultados_parte2.csv")

if __name__ == "__main__":
    rodar_experimento()
