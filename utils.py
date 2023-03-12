# This file contains the necessary functions to conduct test games.

from pandas import Series
from random import choice
from random import randint
import numpy as np
from keras.models import load_model

### --- GAME FUNCTIONS --- ###

def control_win(board):
    
    '''
    The given code defines a function named "control_win" that takes one
    argument, "board", which is expected to be a list of 9 elements
    representing a tic-tac-toe board.

    The function checks for all possible winning combinations in the board
    and returns True if any of the combinations is found.
    Otherwise, it returns False.
    '''
    
    for k in [0, 3, 6]:
        if board[k] == board[k + 1] == board[k + 2] and board[k] != '_':
            return True
    for k in [0, 1, 2]:
        if board[k] == board[k + 3] == board[k + 6] and board[k] != '_':
            return True
    if board[0] == board[4] == board[8] and board[0] != '_':
        return True
    elif board[2] == board[4] == board[6] and board[2] != '_':
        return True
    else:
        return False


def activate_end(board):
    
    '''
    The given code defines a function named "activate_end"
    that takes one argument, "board", which is expected to be a list
    of 9 elements representing a tic-tac-toe board.
    '''
    
    for element in board:
        if element != '_':
            active = True
        else:
            active = False
            break
    return active


def all_proper_move(board, sign):
    
    '''
    This function is for creating a list of all possible moves
    that a player can make at a given state of the game.
    '''
    
    all_move = []
    for k in range(9):
        if board[k] == '_':
            move = board.copy()
            move[k] = sign
            all_move.append(''.join(move))
    return all_move

#################################
### --- STRATEGY FUCNTION --- ###


def random_player(board, sign):
    
    '''
    This function represents a basic computer player that randomly selects
    an empty square on the board to place its symbol.
    '''
    
    while True:
        place = randint(0, 8)
        if board[place] == '_':
            board[place] = sign
            break
    


def q_learner_player(board, sign, Q_table):
    
    '''
    The function then selects the move with the highest Q-value using the "max"
    function with the "move_list" dictionary as the argument.
    The resulting move is then converted back to a list
    and returned by the function.
    '''
    if sign == 'O':
        state_list = all_proper_move(board, sign)
        move_list = dict([(element, Q_table[element]) for element in state_list])
        board = list(max(move_list, key=move_list.get))
        return board
    else:
        state_list = all_proper_move(board, sign)
        move_list = dict([(element, Q_table[element]) for element in state_list])
        board = list(min(move_list, key=move_list.get))
        return board


def teacher_player(board, sign):
    
    '''
    This function is designed to serve as a basic strategy for a player in
    a tic-tac-toe game. It first attempts to claim the center square,
    which is considered a strong move. If the center square is already taken,
    the function tries to claim one of the corner squares,
    which are also considered strong moves. If none of the corner squares
    are available, the function selects one of the remaining squares at random,
    which is considered a weaker move.
    '''
    
    if board[4] == '_':
        board[4] = sign
        return None
    else:
        for element in [0, 2, 6, 8]:
            if board[element] == '_':
                while True:
                    place = choice([0, 2, 6, 8])
                    if board[place] == '_':
                        board[place] = sign
                        return None

        for element in [1, 3, 5, 7]:
            if board[element] == '_':
                while True:
                    place = choice([1, 3, 5, 7])
                    if board[place] == '_':
                        board[place] = sign
                        return None

###############################
### --- FUCTIONS FOR ML --- ###


def table_to_numbers(key):
    
    '''
    The given code defines a function named "table_to_numbers" that takes
    one argument, "key", which is expected to be a string representing
    a tic-tac-toe board in table format (e.g., "X_O_X___O").
    
    It then creates a dictionary named "my_dict" that maps each symbol
    ('X', '_', 'O')to a numeric value (-1.0, 0.0, 1.0), respectively,
    that can be used as input to a machine learning model.
    '''  
    
    sign_list = [*key]
    my_dict = {'X': -1.0, '_': 0.0, 'O': 1.0}
    return list(Series(sign_list).map(my_dict))


def q_table_ann(model_name, D_table, Q_control):
    
    '''
    This function seems to use a trained Keras model to update a Q-table
    for a reinforcement learning task. Note that this function assumes that
    the Keras model has been trained to predict Q-values for state-action
    pairs, and that the state representation used in the Q-table is compatible
    with the input format of the Keras model.
    '''
    
    policy = load_model(model_name)
    
    for key in Q_control.keys():
      policy_input = np.asarray(table_to_numbers(key)).reshape((1, 9))
      q_value = policy.predict(policy_input, verbose=0)
      D_table[key] = q_value

##############################
