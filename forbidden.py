from search_chain import search_for_4, search_for_3 

def long_forbidden(board) -> bool:
    if long_line(board) == True:
        return True # 长连禁手成立
    else:
        pass
    return False

def long_line(board):
    return check_horizonal(board) or check_vertical(board) or check_leftcross(board) or check_rightcross(board)

def check_horizonal(board):
    return check_long_line(board)
    
def check_vertical(board):
    return check_long_line([list(l) for l in zip(*board)])

def check_leftcross(board):
    board_left = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_left[x+y].append(board[x][y])
    # print (board_left)
    return check_long_line(board_left)

def check_rightcross(board):
    board_right = [[] for line in range(29)]
    for x in range(15):
        for y in range(15):
            board_right[x-y].append(board[x][y])
    return check_long_line(board_right)

def check_long_line(board) -> bool:
    for list_str in board:
        if ''.join(list_str).find('B'*6) != -1:
            return True
        else:
            pass
    return False

#先查长连，然后查5，然后查44，最后查33

def border_extend(board):
    border = [['Z'] * 17] + [ ['Z', *row, 'Z'] for row in board] + [['Z'] * 17]
    return border
    
def chain_query_horizonal(x, y, border_extend):
    _list = []
    _list.append(border_extend[x][y])
    for i in range(1,6):
        if x+i < 17:
            _list.append(border_extend[x+i][y])
        else:
            pass
        if x-i >= 0:
            _list = [border_extend[x-i][y]] + _list
        else:
            pass
    return _list

def chain_query_vertical(x, y, border_extend):
    _list = []
    _list.append(border_extend[x][y])
    for i in range(1,6):
        if y+i < 17:
            _list.append(border_extend[x][y+i])
        else:
            pass
        if y-i >= 0:
            _list = [border_extend[x][y-i]] + _list
        else:
            pass
    return _list

def chain_query_leftcross(x, y, border_extend):
    _list = []
    _list.append(border_extend[x][y])
    for i in range(1,6):
        if x+i < 17 and y-i>= 0:
            _list.append(border_extend[x+i][y-i])
        else:
            pass
        if x-i >= 0 and y+i < 17:
            _list = [border_extend[x-i][y+i]] + _list
        else:
            pass
    return _list

def chain_query_rightcross(x, y, border_extend):
    _list = []
    _list.append(border_extend[x][y])
    for i in range(1,6):
        if x-i >= 0 and y-i >= 0:
            _list = [border_extend[x-i][y-i]] + _list
        else:
            pass
        if x+i < 17 and y+i < 17:
            _list.append(border_extend[x+i][y+i])
        else:
            pass
    return _list

def double_4(x, y, board) -> bool:
    check_tag = 0
    extended_board = border_extend(board)
    check_tag += search_for_4(chain_query_horizonal(x, y, extended_board))
    check_tag += search_for_4(chain_query_vertical(x, y, extended_board))
    check_tag += search_for_4(chain_query_leftcross(x, y, extended_board))
    check_tag += search_for_4(chain_query_rightcross(x, y, extended_board))
    if check_tag > 1:
        return True
    else:
        return False

def double_3(x, y, board):
    check_tag = 0
    extended_board = border_extend(board)
    check_tag += search_for_3(chain_query_horizonal(x, y, extended_board))
    check_tag += search_for_3(chain_query_vertical(x, y, extended_board))
    check_tag += search_for_3(chain_query_leftcross(x, y, extended_board))
    check_tag += search_for_3(chain_query_rightcross(x, y, extended_board))
    if check_tag > 1:
        return True
    else:
        return False
    
