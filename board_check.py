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

def check_win(new_board) -> int:
    for list_str in new_board:
        if ''.join(list_str).find('B'*5) != -1:
            return 1
        elif ''.join(list_str).find('W'*5) != -1:
            return -1
        else:
            pass
    return 0

def check_win_horizonal(board):
    return check_win(board)
    
def check_win_vertical(board):
    return check_win([list(l) for l in zip(*board)])

def check_win_leftcross(board):
    board_left = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_left[x+y].append(board[x][y])
    return check_win(board_left)

def check_win_rightcross(board):
    board_right = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_right[x-y].append(board[x][y])
    return check_win(board_right)
        #
def check_win_all(board) -> int:
    board_t = show_board(board)
    if check_win_horizonal(board_t) + check_win_vertical(board_t) + check_win_leftcross(board_t) + check_win_rightcross(board_t) > 0:
        return 1
    elif check_win_horizonal(board_t) + check_win_vertical(board_t) + check_win_leftcross(board_t) + check_win_rightcross(board_t) < 0:
        return -1
    else:
        return 0

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
            # print (return_board)
            board[x][y] += return_board[x][y]
    return board

def divide_board(board):
    # matrix_0 = [[random.randint(-1,1) for i in range(15)] for i in range(15)]
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