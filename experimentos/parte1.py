            
            #Parte 1: Largura vs Profundidade vs Custo Uniforme
import sys
import os
sys.path.append(os.path.abspath("../src")) 

import csv
from puzzle import gerar_estado_inicial
from funcoes_custo import custo_c1, custo_c2, custo_c3, custo_c4
from algoritmos import busca_largura, busca_profundidade, busca_custo_uniforme

FUNCOES_CUSTO = {
    "C1": custo_c1,
    "C2": custo_c2,
    "C3": custo_c3,
    "C4": custo_c4
}

ALGORITMOS = {
    "Largura": busca_largura,
    "Profundidade": busca_profundidade,
    "CustoUniforme": busca_custo_uniforme
}

def rodar_experimento():
    with open("resultados_parte1.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "ID", "Algoritmo", "FuncaoCusto",
            "CustoTotal", "Visitados", "Gerados", "TamanhoCaminho"
        ])

        for i in range(1, 31):  # 30 estados
            estado_inicial = gerar_estado_inicial()
            print(f"\n🔁 Executando cenário {i}/30...")

            for nome_alg, func_alg in ALGORITMOS.items():
                for nome_custo, func_custo in FUNCOES_CUSTO.items():
                    print(f"➡️ {nome_alg} + {nome_custo}")
                    if nome_alg == "Profundidade":
                        resultado = func_alg(estado_inicial, func_custo, limite=50)
                    else:
                        resultado = func_alg(estado_inicial, func_custo)

                    custo = resultado['custo'] if resultado['caminho'] else "inf"
                    tam_caminho = len(resultado['caminho']) - 1 if resultado['caminho'] else 0
                    writer.writerow([
                        i,
                        nome_alg,
                        nome_custo,
                        custo,
                        resultado['visitados'],
                        resultado['gerados'],
                        tam_caminho
                    ])

    print("\n✅ Resultados salvos em resultados_parte1.csv")

if __name__ == "__main__":
    rodar_experimento()
