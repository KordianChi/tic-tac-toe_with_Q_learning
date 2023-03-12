from random import choice
from utils import all_proper_move
from utils import activate_end
from utils import control_win
from utils import random_player




def q_table_generator(test_games):

    
    '''
    Our Q table is a dictionary where key is string with board state.
    Firstly we assume value 0 for all state, except winning state.
    We generate Q table with all legal state by,
    significant number games between random players. 
    Number of legal state in tic tac toe is 5478,
    there is no obviously way to calculate that.
    '''
    
    ALPHA = 0.9
    GAMMA = 0.9
    
    
    legal_state_number = 5478
    
    
    Q_table = {}
    
    BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
    Q_table[''.join(BOARD)] = 0
    while len(Q_table) < legal_state_number:
        BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        sign = 'O'
        turn = choice(['player_1', 'player_2'])
        while not activate_end(BOARD):
            if turn == 'player_1':
                random_player(BOARD, sign)
            else:
                random_player(BOARD, sign)
            if control_win(BOARD):
                if sign == 'O':
                    Q_table[''.join(BOARD)] = 1
                else:
                    Q_table[''.join(BOARD)] = -1
                break
            else:
                Q_table[''.join(BOARD)] = 0
            if sign == 'O':
                sign = 'X'
            else:
                sign = 'O'
            if turn == 'player_1':
                turn = 'player_2'
            else:
                turn = 'player_1'
                
                
    
    Q_control = dict(zip(Q_table.keys(),
                         [0 for k in range(len(Q_table.values()))]))  
    # Completing Q table by game with random players in purly exploration way
    
    for k in range(test_games):
        BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
        sign = 'O'
        episode = []
        signs = []
        episode.append(''.join(BOARD))
        while not activate_end(BOARD):
    
            if sign == 'O':
                if not Q_control[''.join(BOARD)]:
                  Q_control[''.join(BOARD)] = 1
    
                random_player(BOARD, sign)
                signs.append(sign)
                episode.append(''.join(BOARD))
            else:
                if not Q_control[''.join(BOARD)]:
                  Q_control[''.join(BOARD)] = 1
     
                random_player(BOARD, sign)
                signs.append(sign)
                episode.append(''.join(BOARD))
    
            if control_win(BOARD):
                break
            if sign == 'O':
                sign = 'X'
            else:
                sign = 'O'
    
        
        episode = episode[:len(episode) - 1]
        episode = episode[::-1]
        signs = signs[::-1]
        for k in range(len(episode)):
            Q_table[episode[k]] = Q_table[episode[k]] + ALPHA * (GAMMA *\
            max([Q_table[element] for element in all_proper_move([*episode[k]], signs[k])])\
            - Q_table[episode[k]])   

    return Q_table, Q_control