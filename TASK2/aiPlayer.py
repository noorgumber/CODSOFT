import math

def is_win(board, player):
    win_condition = [
        [0,1,2], [3,4,5], [6,7,8], 
        [0,3,6], [1,4,7], [2,5,8], 
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == player for i in combo) for combo in win_condition)

def is_draw(board):
    return ' ' not in board

def avl_move(board):
    return [i for i in range(9) if board[i] == ' ']

def minimax(board, depth, is_maximizing, alpha=-math.inf, beta=math.inf):
    if is_win(board, 'O'): return 1
    if is_win(board, 'X'): return -1
    if is_draw(board): return 0

    if is_maximizing:  # AI is 'O'
        max_score = -math.inf
        for move in avl_move(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False, alpha, beta)
            board[move] = ' '
            max_score = max(max_score, score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return max_score
    else:  # Player is 'X'
        min_score = math.inf
        for move in avl_move(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True, alpha, beta)
            board[move] = ' '
            min_score = min(min_score, score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return min_score

def best_turn(board):
    best_score = -math.inf
    move = None
    for i in avl_move(board):
        board[i] = 'O'
        score = minimax(board, 0, False)  # simulate opponent next
        board[i] = ' '
        if score > best_score:
            best_score = score
            move = i
    return move
