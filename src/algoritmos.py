from collections import deque
from puzzle import PuzzleState
import heapq

def busca_largura(estado_inicial, funcao_custo, randomizar=False):
    """
    A1 - Busca em Largura (BFS)

    Parâmetros:
        - estado_inicial: objeto PuzzleState
        - funcao_custo: função de custo (mesmo que não afete o caminho, será usada ao final)

    Retorna:
        - dicionário com:

            'estado_objetivo', 'caminho', 'custo', 'visitados', 'gerados'
    """
    fila = deque()
    visitados = set()
    pai = {}              # Para reconstruir o caminho
    acao_que_leva = {}    # Mapeia o estado atual para a ação usada

    fila.append(estado_inicial)
    visitados.add(tuple(estado_inicial.board))
    pai[tuple(estado_inicial.board)] = None
    acao_que_leva[tuple(estado_inicial.board)] = None

    gerados = 1
    visitados_count = 0

    while fila:
        atual = fila.popleft()
        visitados_count += 1

        if atual.is_goal():
            return {
                "estado_objetivo": atual,
                "caminho": reconstruir_caminho(atual, pai, acao_que_leva),
                "custo": calcular_custo(atual, pai, acao_que_leva, funcao_custo),
                "visitados": visitados_count,
                "gerados": gerados
            }

        for sucessor, acao in atual.get_successors(randomize=randomizar):
            chave = tuple(sucessor.board)
            if chave not in visitados:
                fila.append(sucessor)
                visitados.add(chave)
                pai[chave] = atual
                acao_que_leva[chave] = acao
                gerados += 1

    return {
        "estado_objetivo": None,
        "caminho": None,
        "custo": float('inf'),
        "visitados": visitados_count,
        "gerados": gerados
    }


def reconstruir_caminho(estado_final, pai, acao_que_leva):
    caminho = []
    atual = estado_final
    while pai[tuple(atual.board)] is not None:
        acao = acao_que_leva[tuple(atual.board)]
        caminho.insert(0, (atual, acao))  # estado e a ação que levou a ele
        atual = pai[tuple(atual.board)]
    caminho.insert(0, (atual, None))  # adiciona o estado inicial
    return caminho


def calcular_custo(estado_final, pai, acao_que_leva, funcao_custo):
    custo_total = 0
    atual = estado_final

    while pai[tuple(atual.board)] is not None:
        anterior = pai[tuple(atual.board)]
        acao = acao_que_leva[tuple(atual.board)]
        custo_total += funcao_custo(anterior, atual, acao)
        atual = anterior

    return custo_total



# Busca em profundidade

def busca_profundidade(estado_inicial, funcao_custo, limite=50, randomizar=False):
    """
    A2 - Busca em Profundidade (DFS) com limite de profundidade padrão de 50

    Parâmetros:
        - estado_inicial: objeto PuzzleState
        - funcao_custo: função de custo (será usada apenas no final)
        - limite: profundidade máxima (evita recursão infinita)

    Retorna:
        - dicionário com estado objetivo, caminho, custo, visitados, gerados
    """
    pilha = []
    visitados = set()
    pai = {}
    acao_que_leva = {}

    pilha.append((estado_inicial, 0))  # (estado, profundidade)
    visitados.add(tuple(estado_inicial.board))
    pai[tuple(estado_inicial.board)] = None
    acao_que_leva[tuple(estado_inicial.board)] = None

    gerados = 1
    visitados_count = 0

    while pilha:
        atual, profundidade = pilha.pop()
        visitados_count += 1

        if atual.is_goal():
            return {
                "estado_objetivo": atual,
                "caminho": reconstruir_caminho(atual, pai, acao_que_leva),
                "custo": calcular_custo(atual, pai, acao_que_leva, funcao_custo),
                "visitados": visitados_count,
                "gerados": gerados
            }

        if profundidade < limite:
            for sucessor, acao in reversed(atual.get_successors(randomize=randomizar)):  # reversed para manter a ordem dos operadores
                chave = tuple(sucessor.board)
                if chave not in visitados:
                    pilha.append((sucessor, profundidade + 1))
                    visitados.add(chave)
                    pai[chave] = atual
                    acao_que_leva[chave] = acao
                    gerados += 1

    return {
        "estado_objetivo": None,
        "caminho": None,
        "custo": float('inf'),
        "visitados": visitados_count,
        "gerados": gerados
    }



# Algoritmo de busca de custo uniforme

def busca_custo_uniforme(estado_inicial, funcao_custo):
    """
    A3 - Busca de Custo Uniforme (Dijkstra)

    Parâmetros:
        - estado_inicial: objeto PuzzleState
        - funcao_custo: função que retorna custo entre dois estados

    Retorna:
        - dicionário com estado objetivo, caminho, custo, visitados, gerados
    """
    heap = []  # fila de prioridade: (custo, contador, estado)
    visitados = set()
    pai = {}
    acao_que_leva = {}
    custo_ate_agora = {}

    contador = 0
    heapq.heappush(heap, (0, contador, estado_inicial))
    pai[tuple(estado_inicial.board)] = None
    acao_que_leva[tuple(estado_inicial.board)] = None
    custo_ate_agora[tuple(estado_inicial.board)] = 0

    visitados_count = 0
    gerados = 1

    while heap:
        custo_atual, _, atual = heapq.heappop(heap)
        chave_atual = tuple(atual.board)

        if chave_atual in visitados:
            continue

        visitados.add(chave_atual)
        visitados_count += 1

        if atual.is_goal():
            return {
                "estado_objetivo": atual,
                "caminho": reconstruir_caminho(atual, pai, acao_que_leva),
                "custo": custo_atual,
                "visitados": visitados_count,
                "gerados": gerados
            }

        for sucessor, acao in atual.get_successors():
            chave_sucessor = tuple(sucessor.board)
            novo_custo = custo_ate_agora[chave_atual] + funcao_custo(atual, sucessor, acao)

            if chave_sucessor not in custo_ate_agora or novo_custo < custo_ate_agora[chave_sucessor]:
                custo_ate_agora[chave_sucessor] = novo_custo
                contador += 1
                heapq.heappush(heap, (novo_custo, contador, sucessor))
                pai[chave_sucessor] = atual
                acao_que_leva[chave_sucessor] = acao
                gerados += 1

    return {
        "estado_objetivo": None,
        "caminho": None,
        "custo": float('inf'),
        "visitados": visitados_count,
        "gerados": gerados
    }



# Algoritmo de busca gulosa 

def busca_gulosa(estado_inicial, heuristica, funcao_custo):
    """
    A4 - Busca Gulosa (Greedy)

    Parâmetros:
        - estado_inicial: PuzzleState
        - heuristica: função heurística (h1 ou h2)
        - funcao_custo: função de custo (usada só ao final)

    Retorna:
        - dicionário com estado objetivo, caminho, custo, visitados, gerados
    """
    heap = []  # fila de prioridade com base na heurística
    visitados = set()
    pai = {}
    acao_que_leva = {}

    contador = 0
    prioridade_inicial = heuristica(estado_inicial)
    heapq.heappush(heap, (prioridade_inicial, contador, estado_inicial))
    pai[tuple(estado_inicial.board)] = None
    acao_que_leva[tuple(estado_inicial.board)] = None

    visitados_count = 0
    gerados = 1

    while heap:
        _, _, atual = heapq.heappop(heap)
        chave = tuple(atual.board)

        if chave in visitados:
            continue

        visitados.add(chave)
        visitados_count += 1

        if atual.is_goal():
            return {
                "estado_objetivo": atual,
                "caminho": reconstruir_caminho(atual, pai, acao_que_leva),
                "custo": calcular_custo(atual, pai, acao_que_leva, funcao_custo),
                "visitados": visitados_count,
                "gerados": gerados
            }

        for sucessor, acao in atual.get_successors():
            chave_sucessor = tuple(sucessor.board)
            if chave_sucessor not in visitados:
                contador += 1
                prioridade = heuristica(sucessor)
                heapq.heappush(heap, (prioridade, contador, sucessor))
                pai[chave_sucessor] = atual
                acao_que_leva[chave_sucessor] = acao
                gerados += 1

    return {
        "estado_objetivo": None,
        "caminho": None,
        "custo": float('inf'),
        "visitados": visitados_count,
        "gerados": gerados
    }


# Busca A* (A estrela)
def busca_a_estrela(estado_inicial, heuristica, funcao_custo):
    """
    A5 - Busca A* (A estrela)

    Parâmetros:
        - estado_inicial: PuzzleState
        - heuristica: função heurística (h1 ou h2)
        - funcao_custo: função de custo (c1 a c4)

    Retorna:
        - dicionário com estado objetivo, caminho, custo, visitados, gerados
    """
    heap = []
    visitados = set()
    pai = {}
    acao_que_leva = {}
    custo_ate_agora = {}

    contador = 0
    custo_inicial = 0
    prioridade_inicial = custo_inicial + heuristica(estado_inicial)
    heapq.heappush(heap, (prioridade_inicial, contador, estado_inicial))
    pai[tuple(estado_inicial.board)] = None
    acao_que_leva[tuple(estado_inicial.board)] = None
    custo_ate_agora[tuple(estado_inicial.board)] = 0

    visitados_count = 0
    gerados = 1

    while heap:
        _, _, atual = heapq.heappop(heap)
        chave_atual = tuple(atual.board)

        if chave_atual in visitados:
            continue

        visitados.add(chave_atual)
        visitados_count += 1

        if atual.is_goal():
            return {
                "estado_objetivo": atual,
                "caminho": reconstruir_caminho(atual, pai, acao_que_leva),
                "custo": custo_ate_agora[chave_atual],
                "visitados": visitados_count,
                "gerados": gerados
            }

        for sucessor, acao in atual.get_successors():
            chave_sucessor = tuple(sucessor.board)
            novo_custo = custo_ate_agora[chave_atual] + funcao_custo(atual, sucessor, acao)

            if chave_sucessor not in custo_ate_agora or novo_custo < custo_ate_agora[chave_sucessor]:
                custo_ate_agora[chave_sucessor] = novo_custo
                prioridade = novo_custo + heuristica(sucessor)
                contador += 1
                heapq.heappush(heap, (prioridade, contador, sucessor))
                pai[chave_sucessor] = atual
                acao_que_leva[chave_sucessor] = acao
                gerados += 1

    return {
        "estado_objetivo": None,
        "caminho": None,
        "custo": float('inf'),
        "visitados": visitados_count,
        "gerados": gerados
    }