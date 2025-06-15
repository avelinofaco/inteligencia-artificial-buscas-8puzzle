def custo_c1(estado_atual, proximo_estado, acao):
    """C1: Todas as ações custam 2"""
    return 2


def custo_c2(estado_atual, proximo_estado, acao):
    """
    C2: Verticais (up, down) = 2
        Horizontais (left, right) = 3
    """
    if acao in ['up', 'down']:
        return 2
    return 3


def custo_c3(estado_atual, proximo_estado, acao):
    """
    C3: Verticais (up, down) = 3
        Horizontais (left, right) = 2
    """
    if acao in ['up', 'down']:
        return 3
    return 2


def custo_c4(estado_atual, proximo_estado, acao):
    """
    C4: Igual à C2, MAS se o espaço vazio for movido para o centro (índice 4),
    o custo será 5 independentemente da direção.
    """
    pos_central = 4
    if proximo_estado.empty_index == pos_central:
        return 5
    return custo_c2(estado_atual, proximo_estado, acao)
