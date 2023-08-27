class PuzzleState:
    def __init__(self, board, parent=None, action=None):
        self.board = board
        self.parent = parent
        self.action = action

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def get_blank_position(self):
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == 0:
                    return i, j

    def get_possible_moves(self):
        moves = []
        i, j = self.get_blank_position()

        if i > 0:
            moves.append('U')
        if i < len(self.board) - 1:
            moves.append('D')
        if j > 0:
            moves.append('L')
        if j < len(self.board[i]) - 1:
            moves.append('R')

        return moves

    def move(self, action):
        i, j = self.get_blank_position()

        new_board = [row[:] for row in self.board]
        if action == 'U':
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
        elif action == 'D':
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
        elif action == 'L':
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
        elif action == 'R':
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]

        return PuzzleState(new_board, self, action)


def solve_puzzle_dfs(initial_state, goal_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()

        if current_state == goal_state:
            return get_solution(current_state)

        visited.add(current_state)

        possible_moves = current_state.get_possible_moves()
        for move in possible_moves:
            new_state = current_state.move(move)
            if new_state not in visited:
                stack.append(new_state)

    return None


def get_solution(state):
    solution = []
    while state.parent is not None:
        solution.insert(0, state.action)
        state = state.parent
    return solution


# Testing the code
initial_board = [
    [1, 2, 3],
    [0, 4, 6],
    [7, 5, 8]
]

goal_board = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

initial_state = PuzzleState(initial_board)
goal_state = PuzzleState(goal_board)

print("Initial Board:")
for row in initial_state.board:
    print(row)

solution = solve_puzzle_dfs(initial_state, goal_state)

if solution is None:
    print("No solution found.")
else:
    print("Solution:")
    print(" -> ".join(solution))
