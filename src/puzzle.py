import random

#Lista com os 9 estados objetivo possíveis (números 1 a 8 em ordem crescente)
OBJETIVOS = [
    [1, 2, 3, 4, 5, 6, 7, 8, 0],
    [0, 1, 2, 3, 4, 5, 6, 7, 8],
    [1, 0, 2, 3, 4, 5, 6, 7, 8],
    [1, 2, 0, 3, 4, 5, 6, 7, 8],
    [1, 2, 3, 0, 4, 5, 6, 7, 8],
    [1, 2, 3, 4, 0, 5, 6, 7, 8],
    [1, 2, 3, 4, 5, 0, 6, 7, 8],
    [1, 2, 3, 4, 5, 6, 0, 7, 8],
    [1, 2, 3, 4, 5, 6, 7, 0, 8],
]

class PuzzleState:
    def __init__(self, board):
        self.board = board  # Lista de 9 números (0 representa o espaço vazio)
        self.empty_index = self.board.index(0)

    def __repr__(self):
        """Retorna o estado em formato 3x3 para visualização"""
        return f"{self.board[:3]}\n{self.board[3:6]}\n{self.board[6:]}\n"

    def is_goal(self):
        """Verifica se o estado atual está entre os estados objetivo"""
        return self.board in OBJETIVOS

    def clone(self):
        """Cria uma cópia do estado atual"""
        return PuzzleState(self.board.copy())

    def move(self, direction):
        """Aplica uma ação (movimento) e retorna novo estado ou None se inválido"""
        moves = {
            'up': -3,
            'down': 3,
            'left': -1,
            'right': 1
        }

        if direction not in moves:
            return None

        target = self.empty_index + moves[direction]

        # Impede movimentos inválidos nas bordas
        if direction == 'left' and self.empty_index % 3 == 0:
            return None
        if direction == 'right' and self.empty_index % 3 == 2:
            return None
        if target < 0 or target >= 9:
            return None

        new_board = self.board.copy()
        new_board[self.empty_index], new_board[target] = new_board[target], new_board[self.empty_index]
        return PuzzleState(new_board)

    def get_successors(self, randomize=False):
        """Gera sucessores aplicando as ações possíveis"""
        directions = ['up', 'down', 'left', 'right']
        if randomize:
            random.shuffle(directions)

        successors = []
        for d in directions:
            moved = self.move(d)
            if moved:
                successors.append((moved, d))  # (novo estado, ação)
        return successors

# Geração de estado inicial aleatório e solúvel
def gerar_estado_inicial():
    while True:
        estado = list(range(9))  # números de 0 a 8
        random.shuffle(estado)
        if is_solvable(estado):
            return PuzzleState(estado)

# Verifica se o estado é solúvel com base na contagem de inversões
def is_solvable(board):
    inv = 0
    for i in range(8):
        for j in range(i+1, 9):
            if board[i] != 0 and board[j] != 0 and board[i] > board[j]:
                inv += 1
    return inv % 2 == 0

# Teste rápido
if __name__ == "__main__":
    estado = gerar_estado_inicial()
    print("Estado Inicial:")
    print(estado)

    print("É objetivo?", estado.is_goal())

    print("\n Sucessores:")
    for s, acao in estado.get_successors():
        print(f"Ação: {acao}\n{s}")
