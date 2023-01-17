# function for control win status in board. For this case we use flatten board (1D instead 3x3 2D)
from random import randint, choice


def control_win(board):
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
        
        
        
# function for stopping game when board is full

def activate_end(board):
    for element in board:
        if element != '_':
            active = True
        else:
            active = False
            break
    return active



# strategy of random player

def random_player(board, sign):
    while True:
        place = randint(0, 8)
        if board[place] == '_':
            board[place] = sign
            break
        
        
# Naive strategy of "teacher" player - prior choice is center, second corners, and last sides.
# In case corners and sides we use element of randomization

def teacher_player(board, sign):
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
                    

# Function for finding all legal moves - for using with Q_table

def all_proper_move(board, sign):
    all_move = []
    for k in range(9):
        if board[k] == '_':
            move = board.copy()
            move[k] = sign
            all_move.append(''.join(move))
    return all_move


# Strategy of Q_learner player - we assume +1 for "O" winning and -1 for "X" winnig,
# so Q_learner choose maximum value from Q table if play with "O" and choose minimum in opposite.

def q_learner_player(board, sign, Q_table):
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