from puzzle import gerar_estado_inicial
from funcoes_custo import custo_c2
from heuristicas import h2
from algoritmos import (
    busca_largura,
    busca_profundidade,
    busca_custo_uniforme,
    busca_gulosa,
    busca_a_estrela
)

def imprimir_resultado(nome, resultado):
    print(f"\n{'='*60}")
    print(f" Resultado da {nome}")
    print(f"{'='*60}")

    if resultado["caminho"] is None:
        print(" Nenhuma solução encontrada.")
        return

    print(f" Estado Objetivo:\n{resultado['estado_objetivo']}")

    print(f" Custo total: {resultado['custo']}")
    print(f" Nós visitados: {resultado['visitados']}")
    print(f" Nós gerados: {resultado['gerados']}")
    print(f" Tamanho do caminho: {len(resultado['caminho']) - 1} movimentos\n")
    
    print("📍 Caminho (ação + estado):")
    for estado, acao in resultado["caminho"]:
        if acao:
            print(f"Ação: {acao}")
        print(estado)

if __name__ == "__main__":
    print("\n Gerando estado inicial aleatório...")
    estado = gerar_estado_inicial()
    print(" Estado Inicial:")
    print(estado)

    # A1 - Largura
    resultado = busca_largura(estado, custo_c2)
    imprimir_resultado("Busca em Largura (A1)", resultado)

    # A2 - Profundidade
    resultado = busca_profundidade(estado, custo_c2, limite=50)
    imprimir_resultado("Busca em Profundidade (A2)", resultado)

    # A3 - Custo Uniforme
    resultado = busca_custo_uniforme(estado, custo_c2)
    imprimir_resultado("Busca de Custo Uniforme (A3)", resultado)

    # A4 - Busca Gulosa
    resultado = busca_gulosa(estado, h2, custo_c2)
    imprimir_resultado("Busca Gulosa com H2 (A4)", resultado)

    # A5 - Busca A*
    resultado = busca_a_estrela(estado, h2, custo_c2)
    imprimir_resultado("Busca A* com H2 (A5)", resultado)
