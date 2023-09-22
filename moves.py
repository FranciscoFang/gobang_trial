import numpy as np
import random
from board_check import compare_board, print_board, check_win_all, divide_board

def make_answer_board_black(argmax_index):
    x = (argmax_index)//15
    y = (argmax_index)%15
    answer_board = [[0]*15 for i in range(15)]
    answer_board[x][y] = 1
    # print(answer_board)
    return answer_board

def make_answer_board_white(argmax_index):
    x = (argmax_index)//15
    y = (argmax_index)%15
    answer_board = [[0]*15 for i in range(15)]
    answer_board[x][y] = -1
    # print(answer_board)
    return answer_board

def find_max_values_black(prediction, board):
    index_sort = np.argsort(np.array(prediction[0]).flatten())
    i = -1
    while True:
        # print ("will select ", i, "-th, index is ", index_sort[i],", value is ", np.array(prediction[0]).flatten()[index_sort[i]], "")
        answer_board = make_answer_board_black(index_sort[i])
        if compare_board(answer_board, board) == True:
            break
        else:
            i -= 1
            continue
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

def machine_1(board, model1):
    return_board = [[0]*15 for i in range(15)]
    one_step = board
    for x in range(15):
        for y in range(15):
            if board[x][y] == 0:
                one_step[x][y] = 1
                if check_win_all(one_step) == 1:
                    return_board[x][y] = 1
                    one_step[x][y] = 0
                    return return_board
                else:
                    one_step[x][y] = 0
    prediction = model1.predict([divide_board(board)])
    if np.argmax(prediction[0]) != 0:
        answer_board = find_max_values_black(prediction, board)
        return (answer_board)
    else:
        print("============黑棋：没有最大值=================")
        answer_board = [[0]*15 for k in range(15)]
        while True:
            i = random.randint(0,14)
            j = random.randint(0,14)
            if board[i][j] == 0:
                answer_board[i][j] = 1
                break
        print (print_board(answer_board))
        return answer_board

def machine_2(board, model2):
    return_board = [[0]*15 for i in range(15)]
    one_step = board
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
    prediction = model2.predict([divide_board(board)])
    if np.argmax(prediction[0]) != 0:
        answer_board = find_max_values_white(prediction, board)
        return (answer_board)
    else:
        print("============白棋：没有最大值=================")
        answer_board = [[0]*15 for k in range(15)]
        while True:
            i = random.randint(0,14)
            j = random.randint(0,14)
            if board[i][j] == 0:
                answer_board[i][j] = -1
                break
        print (print_board(answer_board))
        return answer_board