import math
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def minimax(board, depth, is_maximizing, alpha, beta):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    elif is_board_full(board):
        return 0

    if is_maximizing:
        max_eval = -math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = math.inf
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval

def find_best_move(board):
    best_move = None
    best_value = -math.inf
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'X'
                move_value = minimax(board, 0, False, -math.inf, math.inf)
                board[i][j] = ' '
                if move_value > best_value:
                    best_value = move_value
                    best_move = (i, j)
    return best_move


def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'O'

    while True:
        print_board(board)
        winner = check_winner(board)
        if winner:
            print(f"Winner is : {winner}")
            break
        elif is_board_full(board):
            print("Tie !")
            break

        if current_player == 'O':
            row = int(input("please enter row number(0,1,2) : "))
            col = int(input("please enter column number(0,1,2) : "))
            if board[row][col] == ' ':
                board[row][col] = 'O'
                current_player = 'X'
            else:
                print("this is full cell .")
        else:
            print("computer is moving")
            move = find_best_move(board)
            if move:
                board[move[0]][move[1]] = 'X'
                current_player = 'O'


play_game()
