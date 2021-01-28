"""
Tic Tac Toe Player
"""
import copy
import math
from typing import Optional

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    turn = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] != EMPTY:
                turn+=1
    if turn % 2 != 0:
        return O
    else:
        return X 


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possibles_actions = []
    
    if terminal(board):
        return None

    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                possibles_actions.append((i,j))
    return possibles_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # if board[action[0]][action[1]] != EMPTY:
    #     raise ValueError
    
    copy_board = copy.deepcopy(board)
    copy_board[action[0]][action[1]] = player(copy_board)
    return copy_board
    


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if board[0][0] != EMPTY and (board[0][0] == board[0][1] == board[0][2] 
        or board[0][0] == board[1][1] == board[2][2] 
        or board[0][0] == board[1][0] == board[2][0]):
        return board[0][0]

    elif board[1][1] != EMPTY and (board[1][0] == board[1][1] == board[1][2]
        or board[0][1] == board[1][1] == board[2][1]):
        return board[1][1]
    
    elif board[2][2] != EMPTY and (board[0][2] == board[1][2] == board[2][2]
        or board[2][0] == board[2][1] == board[2][2]):
        return board[2][2]
    
    elif board[2][0] != EMPTY and (board[2][0] == board[1][1] == board[0][2]):
        return board[2][0]
    
    else:
        None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if not winner(board):
        for i in range(3):
          for j in range(3):
              if board[i][j] == EMPTY:
                  return False
    return True



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winner_player = winner(board)
    if winner_player == X:
        return 1
    elif winner_player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    
    if terminal(board):
        return 
    if current_player == X:
        optimal_value = -math.inf
    
    else:
        optimal_value = math.inf
    
    for action in actions(board):
        new_board = result(board, action)
        
        minimax_value = minimax_aux(new_board, optimal_value)

        if current_player == X:
            minimax_value = max(optimal_value, minimax_value)

        if current_player == O:
            minimax_value = min(optimal_value, minimax_value)

        if optimal_value != minimax_value:
            optimal_value = minimax_value
            optimal_move = action

    return optimal_move

def minimax_aux(board, value):
  
    # When board is filled, when the recursion 'state' is on a leaf
    if terminal(board):
        return utility(board)

    current_player = player(board)
    
    if current_player == X:
        optimal_value = -math.inf

    else:
        optimal_value = math.inf

    for action in actions(board):
        new_board = result(board, action)
        minimax_value = minimax_aux(new_board, optimal_value)

        if current_player == X:
            if minimax_value > value:
                return minimax_value
            optimal_value = max(optimal_value, minimax_value)

        if current_player == O:
            if minimax_value < value:
                return minimax_value
            optimal_value = min(optimal_value, minimax_value)
    
    return optimal_value