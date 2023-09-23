import numpy as np
import random
from board_check import show_board, compare_board, print_board, check_win_all, divide_board
from forbidden import long_forbidden, double_4, double_3
import copy
import time

def make_answer_board_black(argmax_index):
    x = (argmax_index)//15
    y = (argmax_index)%15
    answer_board = [[0]*15 for i in range(15)]
    answer_board[x][y] = 1
    return answer_board, x, y

def make_answer_board_white(argmax_index):
    x = (argmax_index)//15
    y = (argmax_index)%15
    answer_board = [[0]*15 for i in range(15)]
    answer_board[x][y] = -1
    return answer_board

def find_max_values_black(prediction, board, onestep):
    index_sort = np.argsort(np.array(prediction[0]).flatten())
    i = -1
    while True:
        # print ("will select ", i, "-th, index is ", index_sort[i],", value is ", np.array(prediction[0]).flatten()[index_sort[i]], "")
        answer_board, x, y, = make_answer_board_black(index_sort[i])
        if compare_board(answer_board, board) == False:
            i -= 1
            continue
        else:
            onestep[x][y] = 1
            show_next = show_board(onestep)
            if long_forbidden(show_next) == True:
                print ("计算评估阶段：规避长连")
                print (print_board(show_next))
                onestep[x][y] = 0
                i -= 1
                continue
            # else:
            #     pass # 长连 continue
            if check_win_all(onestep) == 1: 
                print ("计算评估阶段：直接获胜")
                onestep[x][y] = 0
                return answer_board # 五连 return
            # else:
            #     pass
            if double_4(x, y, show_next) == True: 
                print ("计算评估阶段：规避4-4")
                print (print_board(show_next))
                onestep[x][y] = 0
                i -= 1
                continue # 4-4 continue
            # else:
            #     pass
            if double_3(x, y, show_next) == True: 
                print ("计算评估阶段：规避3-3")
                print (print_board(show_next))
                onestep[x][y] = 0
                i -= 1
                continue # 3-3 continue
            # else:
            #     pass
        break
    return answer_board

def find_max_values_white(prediction, board):
    index_sort = np.argsort(np.array(prediction[0]).flatten())
    i = -1
    while True:
        # print ("will select ", i, "-th, index is ", index_sort[i],", value is ", np.array(prediction[0]).flatten()[index_sort[i]], "")
        answer_board = make_answer_board_white(index_sort[i])
        if compare_board(answer_board, board) == True:
            break
        else:
            i -= 1
            continue
    return answer_board

def machine_1_random(board):
    answer_board = [[0]*15 for k in range(15)]
    while True:
        i = random.randint(0,14)
        j = random.randint(0,14)
        if board[i][j] == 0:
            answer_board[i][j] = 1
            break
    return answer_board

def machine_1(board, model1):
    return_board = [[0]*15 for i in range(15)]
    one_step = copy.deepcopy(board)
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                one_step[x][y] = 1
                next_one_frame = show_board(one_step)
                if long_forbidden(next_one_frame) == True: # 查6 - continue
                    print ("搜索阶段：规避长连")
                    print (print_board(next_one_frame))
                    one_step[x][y] = 1
                    continue
                else:
                    pass
                if check_win_all(one_step) == 1: #查5
                    print("搜索阶段：直接获胜")
                    return_board[x][y] = 1
                    one_step[x][y] = 0
                    return return_board
                else:
                    one_step[x][y] = 0
                break
    prediction_black = model1.predict([divide_board(board)])
    one_step = copy.deepcopy(board)
    # print(np.argmax(prediction_black[0]))
    # print(prediction_black[0])
    if np.argmax(prediction_black[0]) != 0:
        answer_board = find_max_values_black(prediction_black, board, one_step)
        return (answer_board)
    else:
        print("============黑棋：没有最大值=================")
        print(prediction_black[0])
        time.sleep(60)
        one_step = copy.deepcopy(board)
        answer_board = [[0]*15 for k in range(15)]
        while True:
            i = random.randint(0,14)
            j = random.randint(0,14)
            if board[i][j] == 0: 
                answer_board[i][j] = 1
                one_step[i][j] = 1
                one_step_board = show_board(one_step)
                if long_forbidden(one_step_board) == True: # 查6 - continue
                    print("搜索阶段：规避长连")
                    one_step[i][j] = 0
                    answer_board[i][j] = 0
                    continue
                if check_win_all(one_step) == 1: #查5
                    print("搜索阶段：直接获胜")
                    return_board[x][y] = 1
                    one_step[x][y] = 0
                    return return_board
                if double_4(x, y, one_step_board) == True: 
                    print ("计算评估阶段：规避4-4")
                    print (print_board(one_step_board))
                    one_step[x][y] = 0
                    answer_board[i][j] = 0
                    continue # 4-4 continue
                if double_3(x, y, one_step_board) == True: 
                    print ("计算评估阶段：规避3-3")
                    print (print_board(one_step_board))
                    one_step[x][y] = 0
                    answer_board[i][j] = 0
                    continue
                return answer_board
            break
        return answer_board

def machine_2(board, model2):
    return_board = [[0]*15 for i in range(15)]
    one_step = copy.deepcopy(board)
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                one_step[x][y] = -1
                if check_win_all(one_step) == -1:
                    return_board[x][y] = -1
                    one_step[x][y] = 0
                    return return_board
                else:
                    one_step[x][y] = 0
    prediction_white = model2.predict([divide_board(board)])
    if np.argmax(prediction_white[0]) != 0:
        answer_board = find_max_values_white(prediction_white, board)
        return (answer_board)
    else:
        print("============白棋：没有最大值=================")
        print(prediction_white[0])
        time.sleep(60)
        answer_board = [[0]*15 for k in range(15)]
        while True:
            i = random.randint(0,14)
            j = random.randint(0,14)
            if board[i][j] == 0:
                answer_board[i][j] = -1
                break
        return answer_board
    
def machine_2_random(board):
    answer_board = [[0]*15 for k in range(15)]
    while True:
        i = random.randint(0,14)
        j = random.randint(0,14)
        if board[i][j] == 0:
            answer_board[i][j] = -1
            break
    return answer_board
