def board_transform(board):
    new_board = [['O']*15 for line in range(15)]
    for x in range(15):
        for y in range(15):
            if board[x][y] == 1: new_board[x][y] = 'B'
            elif board[x][y] == -1: new_board[x][y] = 'W'
            else: new_board[x][y] = 'O'
    return new_board

def check_win(new_board) -> bool:
    for list_str in new_board:
        if ''.join(list_str).find('B'*5) != -1:
            print ('Black Wins')
            return True
        elif ''.join(list_str).find('W'*5) != -1:
            print ('White wins')
            return True
        else:
            pass
    return False

# def check_win_left(new_board) -> bool:
#     for list_str in new_board:
#         print(''.join(list_str).find('B'*5))
#         if ''.join(list_str).find('B'*5) != -1:
#             print ('Black Wins')
#             return True
#         elif ''.join(list_str).find('W'*5) != -1:
#             print ('White wins')
#             return True
#         else:
#             pass
#     return False

def check_win_horizonal(board):
    return check_win(board)
    
def check_win_vertical(board):
    return check_win([list(l) for l in zip(*board)])

def check_win_leftcross(board):
    board_left = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_left[x+y].append(board[x][y])
    print (board_left)
    return check_win(board_left)

def check_win_rightcross(board):
    board_right = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_right[x-y].append(board[x][y])
    return check_win(board_right)
        
def check_win_all(board) -> bool:
    return check_win_horizonal(board) or check_win_vertical(board) or check_win_leftcross(board) or check_win_rightcross(board)

def set_stone(x:int, y:int, stone:int, board):
    if x<0 or x>14 or y<0 or y>14:
        print ('Wrong input. Select another place.')
        return False
    elif board[x][y] != 0:
        print ('There is a stone. Select another place.')
        return False
    else:
        return True
        
def print_board(board):
    for line in board:
        print(line)
        
def take_action(board, end_tag):
    pass
    
if __name__ == '__main__':
    board = [[0]*15 for line in range(15)]
    for i in range(0,226):
        if i == 225 and check_win_all(board_transform(board)) == False:
            print('Draw Game.')
            break
        end_tag = False
        if i%2 == 0:
            while True:
                print_board(board_transform(board))
                print ('Black turn to play.')
                # take_action (board, end_tag)
                try:
                    y = int(input('Horizonal coordination 1~15: '))
                    x = int(input('Vertical coordination 1~15: '))
                except ValueError:
                    continue
                if set_stone(x, y, 1, board):
                    board[x][y] = 1
                    if check_win_all(board_transform(board)):
                        end_tag = True
                        break
                    else:
                        break
                else:
                    continue
            if end_tag:
                break
        else:
            while True:
                print_board(board_transform(board))
                print ('White turn to play.')
                try:
                    y = int(input('Horizonal coordination 1~15: '))
                    x = int(input('Vertical coordination 1~15: '))
                except ValueError:
                    continue
                if set_stone(x, y, -1, board):
                    board[x][y] = -1
                    if check_win_all(board_transform(board)):
                        end_tag = True
                        break
                    else:
                        break
                else:
                    continue
            if end_tag:
                break
    print_board(board_transform(board))
    print('Game is over.')