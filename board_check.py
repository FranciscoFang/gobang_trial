import copy

def show_board(board):
    new_board = [['O']*15 for line in range(15)]
    for x in range(15):
        for y in range(15):
            if board[x][y] == 1: new_board[x][y] = 'B'
            elif board[x][y] == -1: new_board[x][y] = 'W'
            else: new_board[x][y] = 'O'
    return new_board

def print_board(board):
    for line in board:
        print(line)

def check_win_b(new_board) -> bool:
    for list_str in new_board:
        if ''.join(list_str).find('B'*5) != -1:
            return True
    return False

def check_win_w(new_board) -> bool:
    for list_str in new_board:
        if ''.join(list_str).find('W'*5) != -1:
            return True
    return False

def check_win_horizonal_black(board):
    return check_win_b(board)
    
def check_win_vertical_black(board):
    return check_win_b([list(l) for l in zip(*board)])

def check_win_leftcross_black(board):
    board_left = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_left[x+y].append(board[x][y])
    return check_win_b(board_left)

def check_win_rightcross_black(board):
    board_right = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_right[x-y].append(board[x][y])
    return check_win_b(board_right)

def check_win_horizonal_white(board):
    return check_win_w(board)
    
def check_win_vertical_white(board):
    return check_win_w([list(l) for l in zip(*board)])

def check_win_leftcross_white(board):
    board_left = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_left[x+y].append(board[x][y])
    return check_win_w(board_left)

def check_win_rightcross_white(board):
    board_right = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_right[x-y].append(board[x][y])
    return check_win_w(board_right)

def check_win_black(board) -> bool:
    copy_board = copy.deepcopy(board)
    board_t = show_board(copy_board)
    horizonal = check_win_horizonal_black(board_t)
    vertical = check_win_vertical_black(board_t)
    left = check_win_leftcross_black(board_t)
    right = check_win_leftcross_black(board_t)
    if horizonal or vertical or left or right:
        return True
    return False
    
def check_win_white(board) -> bool:
    copy_board = copy.deepcopy(board)
    board_t = show_board(copy_board)
    board_t = show_board(copy_board)
    horizonal = check_win_horizonal_white(board_t)
    vertical = check_win_vertical_white(board_t)
    left = check_win_leftcross_white(board_t)
    right = check_win_leftcross_white(board_t)
    if horizonal or vertical or left or right:
        return True
    else:
        return False

def compare_board(return_board, game_board) -> bool:
    for x in range(15):
        for y in range(15):
            if return_board[x][y] != 0:
                if game_board[x][y] == 0: 
                    return True
                else: 
                    return False

def combine_board(board, return_board):
    for x in range(15):
        for y in range(15):
            board[x][y] += return_board[x][y]
    return board

def divide_board(board):
    output_matrix = [[[]*2 for i in range(15) ] for i in range(15)]
    for x in range(15):
        for y in range(15):
            if board[x][y] == 1:
                output_matrix[x][y] = [1,0]
            elif board[x][y] == -1:
                output_matrix[x][y] = [0,1]
            else:
                output_matrix[x][y] = [0,0]
                output_matrix[x][y] = [0,0]
    return output_matrix

def reverse_board(board):
    output_matrix = [[[]*2 for i in range(15) ] for i in range(15)]
    for x in range(15):
        for y in range(15):
            output_matrix[x][y] = (~board[x][y]) + 1
    return output_matrix