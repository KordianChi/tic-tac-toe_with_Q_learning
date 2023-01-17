from random import choice
from functions import random_player, activate_end, control_win, all_proper_move


def q_table_generator():

    ALPHA = 0.9
    GAMMA = 0.9
    
    
    # Our Q table is a dictionary where key is string with board state. Firstly we assume value 0
    # for all state, except winning state.
    # We generate Q table with all legal state by, significant number games between random players. 
    # Number of legal state in tic tac toe is 5478, there is no obviously way to calculate that.
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
                
                
    
    # Completing Q table by game with random players in purly exploration way
    
    for k in range(30000):
            BOARD = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
            sign = 'O'
            turn = choice(['player_1', 'player_2'])
            while not activate_end(BOARD):
                if turn == 'player_1':
                    if sign == 'O':
                        
                        Q_table[''.join(BOARD)] = Q_table[''.join(BOARD)] + ALPHA\
                                * (GAMMA * max([Q_table[element]
                                for element in all_proper_move(BOARD, sign)])\
                                - Q_table[''.join(BOARD)])
                                
                        random_player(BOARD, sign)
                    else:
                        
                        Q_table[''.join(BOARD)] = Q_table[''.join(BOARD)] + ALPHA\
                                * (GAMMA * min([Q_table[element]
                                for element in all_proper_move(BOARD, sign)])\
                                - Q_table[''.join(BOARD)])
                                    
                        random_player(BOARD, sign)
                else:
                    if sign == 'O':
                        
                        Q_table[''.join(BOARD)] = Q_table[''.join(BOARD)] + ALPHA\
                                * (GAMMA * max([Q_table[element]
                                for element in all_proper_move(BOARD, sign)])\
                                - Q_table[''.join(BOARD)])
                                    
                        random_player(BOARD, sign)
                    else:
                        
                        Q_table[''.join(BOARD)] = Q_table[''.join(BOARD)] + ALPHA\
                                * (GAMMA * min([Q_table[element]
                                for element in all_proper_move(BOARD, sign)])\
                                - Q_table[''.join(BOARD)])
                                    
                        random_player(BOARD, sign)
                if control_win(BOARD):
                    break
                if sign == 'O':
                    sign = 'X'
                else:
                    sign = 'O'
                if turn == 'player_1':
                    turn = 'player_2'
                else:
                    turn = 'player_1'
                    

    return Q_table