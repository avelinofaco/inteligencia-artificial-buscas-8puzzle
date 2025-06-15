from puzzle import OBJETIVOS

def h1(estado):
    """
    H1: Número de peças fora do lugar (excluindo o 0), vezes 2.
    Considera o menor valor entre os 9 estados objetivos.
    """
    min_erros = float('inf')
    for objetivo in OBJETIVOS:
        erros = sum(
            1 for i in range(9)
            if estado.board[i] != 0 and estado.board[i] != objetivo[i]
        )
        min_erros = min(min_erros, erros)
    return 2 * min_erros


def h2(estado):
    """
    H2: Soma das distâncias de Manhattan (excluindo o 0), vezes 2.
    Considera o menor valor entre os 9 estados objetivos.
    """
    min_total = float('inf')
    for objetivo in OBJETIVOS:
        total = 0
        for num in range(1, 9):  # de 1 a 8
            pos_atual = estado.board.index(num)
            pos_objetivo = objetivo.index(num)
            linha_atual, col_atual = divmod(pos_atual, 3)
            linha_obj, col_obj = divmod(pos_objetivo, 3)
            total += abs(linha_atual - linha_obj) + abs(col_atual - col_obj)
        min_total = min(min_total, total)
    return 2 * min_total
