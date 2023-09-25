import numpy as np
import random
from board_check import show_board, compare_board, print_board, check_win_black, check_win_white, divide_board
from forbidden import long_forbidden, double_4, double_3
import copy

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
    return answer_board, x, y

def find_max_values_black(prediction, board, one_step):
    # 取 10 次迭代
    index_sort = np.argsort(np.array(prediction[0]).flatten())
    i = -1
    while True:
        # print ("will select ", i, "-th, index is ", index_sort[i],", value is ", np.array(prediction[0]).flatten()[index_sort[i]], "")
        answer_board, x, y, = make_answer_board_black(index_sort[i])
        if compare_board(answer_board, board) == False:
            i -= 1
            continue
        else:
            one_step[x][y] = 1
            show_next = show_board(one_step)
            if double_4(x, y, show_next) == True: 
                print ("黑棋策略搜索阶段：规避4-4")
                print (print_board(show_next))
                one_step[x][y] = 0
                i -= 1
                continue # 4-4 continue
            if double_3(x, y, show_next) == True: 
                print ("黑棋策略搜索阶段：规避3-3")
                print (print_board(show_next))
                one_step[x][y] = 0
                i -= 1
                continue # 3-3 continue
            return answer_board, x, y
        break
    return answer_board

def find_max_values_white(prediction, board, one_step):
    index_sort = np.argsort(np.array(prediction[0]).flatten())
    i = -1
    while True:
        # print ("will select ", i, "-th, index is ", index_sort[i],", value is ", np.array(prediction[0]).flatten()[index_sort[i]], "")
        answer_board, x, y = make_answer_board_white(index_sort[i])
        if compare_board(answer_board, board) == False: #已经有其他棋子占据
            i -= 1
            continue
        else: # 没有占据
            return answer_board, x, y
            # one_step[x][y] = 1
            # if check_win_black(one_step) == True: 
            #     print ("白棋策略搜索阶段：计算评估直接获胜")
            #     one_step[x][y] = 0
            #     return answer_board
            # one_step[x][y] = 0
            # continue
        break
    return answer_board

def machine_1(board, model1):
    return_board = [[0]*15 for i in range(15)]
    one_step = copy.deepcopy(board)
    decision_board_black = [[0]*15 for i in range(15)]
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                one_step[x][y] = 1
                next_one_frame = show_board(one_step)
                if long_forbidden(next_one_frame) == True: # 查6 - continue
                    print ("黑棋全局搜索阶段：规避长连")
                    one_step[x][y] = 1
                    continue
                else:
                    pass
                if check_win_black(one_step) == True: #查5
                    print("黑棋全局搜索阶段：搜索直接获胜")
                    return_board[x][y] = 1
                    decision_board_black[x][y] = 1
                    one_step[x][y] = 0
                    return return_board, decision_board_black
                else:
                    one_step[x][y] = 0
                break
    prediction_black = model1.predict([divide_board(board)])
    # 10~100次采样，取总值（均值）最大的。
    one_step = copy.deepcopy(board)
    if np.argmax(prediction_black[0]) != -1:
        # print ("黑棋：有最大值")
        return_board, x, y = find_max_values_black(prediction_black, board, one_step)
        decision_board_black[x][y] = 1
        return return_board, decision_board_black
    else:
        print("============黑棋：没有最大值=================")
        # print (print_board(prediction_black[0]))
        # print (print_board(show_board(board)))
        # print (np.argmax(prediction_black[0]))
        # sleep()
        return_board, decision_board_black = machine_1_random(board)
        return return_board, decision_board_black

def machine_2(board, model2):
    return_board = [[0]*15 for i in range(15)]
    one_step = copy.deepcopy(board)
    decision_board_white = [[0]*15 for i in range(15)]
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                one_step[x][y] = -1
                if check_win_white(one_step) == True:
                    return_board[x][y] = -1
                    decision_board_white[x][y] = 1
                    one_step[x][y] = 0
                    print ("白棋全局搜索阶段：直接获胜")
                    return return_board, decision_board_white
                else:
                    one_step[x][y] = 0
    prediction_white = model2.predict([divide_board(board)])
    if np.argmax(prediction_white[0]) != -1:
        # print ("白棋：有最大值")
        answer_board, x, y = find_max_values_white(prediction_white, board, one_step)
        decision_board_white[x][y] = 1
        return answer_board, decision_board_white
    else:
        print("============白棋：没有最大值=================")
        # print (print_board(prediction_white[0]))
        # print (print_board(show_board(board)))
        # print (np.argmax(prediction_white[0]))
        # sleep()
        answer_board, decision_board_white = machine_2_random(board)
        return answer_board, decision_board_white

def machine_1_random(board):
    one_step = copy.deepcopy(board)
    answer_board = [[0]*15 for k in range(15)]
    decision_board_black = [[0]*15 for k in range(15)]
    while True:
        i = random.randint(0,14)
        j = random.randint(0,14)
        if board[i][j] == 0:
            one_step[i][j] = 1
            one_step_board = show_board(one_step)
            if long_forbidden(one_step_board) == True: # 查6 - continue
                print("黑棋随机搜索阶段：规避长连")
                one_step[i][j] = 0
                continue
            if check_win_black(one_step) == True: #查5
                print("黑棋随机搜索阶段：直接获胜")
                answer_board[i][j] = 1
                decision_board_black[i][j] = 1
                one_step[i][j] = 0
                return answer_board, decision_board_black
            if double_4(i, j, one_step_board) == True: 
                print ("黑棋随机搜索阶段：规避4-4")
                one_step[i][j] = 0
                continue # 4-4 continue
            if double_3(i, j, one_step_board) == True: 
                print ("黑棋随机搜索阶段：规避3-3")
                one_step[i][j] = 0
                continue
            answer_board[i][j] = 1
            decision_board_black[i][j] = 1
            return answer_board, decision_board_black
        else:
            continue
        break # insurance
    return answer_board # insurance
    

def machine_2_random(board):
    one_step = copy.deepcopy(board)
    answer_board = [[0]*15 for k in range(15)]
    decision_board_white = [[0]*15 for k in range(15)]
    while True:
        i = random.randint(0,14)
        j = random.randint(0,14)
        if board[i][j] == 0:
            one_step[i][j] = -1
            if check_win_white(one_step) == True: #查5
                print("白棋随机搜索阶段：直接获胜")
                answer_board[i][j] = -1
                decision_board_white[i][j] = 1
                one_step[i][j] = 0
                return answer_board, decision_board_white
            answer_board[i][j] = -1
            decision_board_white[i][j] = 1
            return answer_board, decision_board_white
        else:
            continue
        break # insurance
    return answer_board # insurance
