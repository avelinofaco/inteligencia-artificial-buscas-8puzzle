
#Parte 4: Largura vs Profundidade com Ordem Aleatória dos Sucessores

import csv
import sys
import os
sys.path.append(os.path.abspath("../src"))

from puzzle import gerar_estado_inicial
from funcoes_custo import custo_c1, custo_c2, custo_c3, custo_c4
from algoritmos import busca_largura, busca_profundidade

FUNCOES_CUSTO = {
    "C1": custo_c1,
    "C2": custo_c2,
    "C3": custo_c3,
    "C4": custo_c4
}

def rodar_experimento():
    with open("resultados_parte4.csv", "w", newline="") as arquivo:
        writer = csv.writer(arquivo)
        writer.writerow([
            "ID", "Algoritmo", "Execucao", "FuncaoCusto",
            "CustoTotal", "Visitados", "Gerados", "TamanhoCaminho"
        ])

        for i in range(1, 16):  # 15 estados
            estado_inicial = gerar_estado_inicial()
            print(f"\n🔁 Cenário {i}/15")

            for execucao in range(1, 11):  # 10 execuções por algoritmo
                # BFS com ordem aleatória
                print(f"➡️ BFS Randomizado - Execução {execucao}")
                resultado = busca_largura(estado_inicial, custo_c1, randomizar=True)

                salvar_resultados(
                    writer, i, "Largura", execucao, resultado
                )

                # DFS com ordem aleatória
                print(f"➡️ DFS Randomizado - Execução {execucao}")
                resultado = busca_profundidade(estado_inicial, custo_c1, limite=50, randomizar=True)

                salvar_resultados(
                    writer, i, "Profundidade", execucao, resultado
                )

    print("\n Resultados salvos em resultados_parte4.csv")

def salvar_resultados(writer, id_estado, nome_alg, execucao, resultado):
    for nome_custo, func_custo in FUNCOES_CUSTO.items():
        custo = calcular_caminho_customizado(resultado["caminho"], func_custo) if resultado["caminho"] else "inf"
        tam_caminho = len(resultado["caminho"]) - 1 if resultado["caminho"] else 0
        writer.writerow([
            id_estado, nome_alg, execucao, nome_custo,
            custo, resultado["visitados"], resultado["gerados"], tam_caminho
        ])

def calcular_caminho_customizado(caminho, funcao_custo):
    custo_total = 0
    for idx in range(1, len(caminho)):
        anterior, _ = caminho[idx - 1]
        atual, acao = caminho[idx]
        custo_total += funcao_custo(anterior, atual, acao)
    return custo_total

if __name__ == "__main__":
    rodar_experimento()
