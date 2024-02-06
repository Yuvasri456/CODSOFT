import math
import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("..."* 3)

def empty_squares(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def is_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

def evaluate(board):
    if is_winner(board, "O"):
        return 1
    elif is_winner(board, "X"):
        return -1
    elif is_board_full(board):
        return 0
    return None

def minimax(board, depth, alpha, beta, max_player):
    score = evaluate(board)

    if score is not None:
        return score

    if max_player:
        max_eval = -math.inf
        for row, col in empty_squares(board):
            board[row][col] = "O"
            eval = minimax(board, depth + 1, alpha, beta, False)
            board[row][col] = " "
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break
        return max_eval
    else:
        min_eval = math.inf
        for row, col in empty_squares(board):
            board[row][col] = "X"
            eval = minimax(board, depth + 1, alpha, beta, True)
            board[row][col] = " "
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break
        return min_eval

def get_best_move(board):
    best_val = -math.inf
    best_move = None

    for row, col in empty_squares(board):
        board[row][col] = "O"
        move_val = minimax(board, 0, -math.inf, math.inf, False)
        board[row][col] = " "

        if move_val > best_val:
            best_move = (row, col)
            best_val = move_val
    return best_move

def play_tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]

    print("Welcome to Tic-Tac-Toe Game!")
    print_board(board)

    while True:
        row, col = map(int, input("Enter your move : ").split())
        
        if board[row][col] == " ":
            board[row][col] = "X"
        else:
            print("Check your move be careful")
            continue

        print_board(board)

        if is_winner(board, "X"):
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

        print("Think a while AI is making a move...")
        ai_row, ai_col = get_best_move(board)
        board[ai_row][ai_col] = "O"

        print_board(board)

        if is_winner(board, "O"):
            print("AI wins!")
            break
        elif is_board_full(board):
            print("It's a tie!")
            break

if __name__ == "__main__":
    play_tic_tac_toe()
