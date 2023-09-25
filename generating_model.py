import numpy as np
from board_check import show_board, print_board, check_win_black, check_win_white, compare_board, combine_board, reverse_board, divide_board # _black, divide_board_white
from moves import machine_1, machine_2, machine_1_random, machine_2_random
from make_models import make_models
    
def ML_fit_1(allgame, allaction):
    a_game=np.array(allgame)
    a_action=np.array(allaction)
    model1.fit(a_game, a_action, epochs=200, verbose=0)
    # prediction = model1.predict(np.array([divide_board(board)]))
    # return np.argmax(prediction)

def ML_fit_2(allgame, allaction):
    a_game=np.array(allgame)
    a_action=np.array(allaction)
    model2.fit(a_game, a_action, epochs=200, verbose=0)
    # prediction = model1.predict(np.array([divide_board(board)]))
    # return np.argmax(prediction)

model1, model2 = make_models()

if __name__ == '__main__':
    model1, model2 = make_models()
    logs = open('logs.txt', 'w')
    epochs = 10 #as your wish
    black_wins = 0
    white_wins = 0
    draw_game = 0
    i = 0
    sum_allgame_black = []
    sum_allaction_black = []
    sum_allgame_white = []
    sum_allaction_white = []
    while i<epochs:
        i+=1
        board=[[0]*15 for line in range(15)]
        # board[7][7] = 1
        allgame_black=[]
        allaction_black=[]
        allgame_white=[]
        allaction_white=[]
        black_play = True
        steps_count = 0
        while check_win_black(board) or check_win_white(board) == False:
            if len(sum_allgame_black) > 1000:
                sum_allgame_black.pop(0)
                sum_allaction_black.pop(0)
                # print("删除一个黑方旧样本")
            if len(sum_allgame_white) > 1000:
                sum_allgame_white.pop(0)
                sum_allaction_white.pop(0)
                # print("删除一个白方旧样本")
            # print ("到黑方了")
            while check_win_black(board) == False and check_win_white(board) == False and black_play == True:  #黑棋走
                # print ("黑走:", steps_count)
                # print (check_win_black(board), black_play)
                black_play = False
                return_board_black, decision_board_black = machine_1(board, model1)
                if return_board_black == []: print("黑棋返回为空")
                if ''.join(str(return_board_black)).find('1') == -1 : print("检查黑棋是否在下子")
                allgame_black += [divide_board(board)]
                allaction_black += [decision_board_black]
                board = combine_board(board, return_board_black)
                steps_count += 1
                # print ("黑完成一步")
                # print (steps_count)
                if check_win_black(board) == True: break #黑棋赢了跳出
                if check_win_black(board) == False and check_win_white(board) == False and steps_count >= 225: break #平局跳出
                break
            while check_win_black(board) == False and check_win_white(board) == False and black_play == False: #白棋走
                # print ("白走:", steps_count)
                # print (check_win_white(board), black_play)
                black_play = True
                return_board_white, decision_board_white = machine_2(board, model2) #
                if return_board_white == []: print("白棋返回为空")
                if ''.join(str(return_board_white)).find('-1') == -1 : print("检查白棋是否在下子")
                allgame_white += [divide_board(board)]
                allaction_white += [decision_board_white]
                board = combine_board(board, return_board_white)
                steps_count += 1
                # print ("白完成一步")
                # print (steps_count)
                if check_win_white(board) == True: break #白棋赢了跳出
                if check_win_black(board) == False and check_win_white(board) == False and steps_count >= 225: break #平局跳出
                break
            if  check_win_black(board) == False and check_win_white(board) == False and steps_count >= 225: #全部跳出后判断是否平局
                print (steps_count)
                draw_game += 1
                print ("平局+1")
                break
            if check_win_black(board) == True: #全部跳出后判断黑棋是否赢
                sum_allgame_black += allgame_black
                sum_allaction_black += allaction_black
                black_wins += 1
                print ("黑赢+1", "黑AI获胜次数：", black_wins, "白AI获胜次数：", white_wins, "平局次数：", draw_game, "", file=logs)
                # print ("from black training")
                # ML_fit_1(np.asarray(sum_allgame_black), np.asarray(sum_allaction_black))
                # sum_allgame_black = []
                # sum_allaction_black = []
                # print ("from black training: done")
                # # ML_fit_2(np.asarray(sum_allgame_white), np.asarray(sum_allaction_white))
                break
            if check_win_white(board) == True: #全部跳出后判断黑棋是否赢
                sum_allgame_white += allgame_white
                sum_allaction_white += allaction_white
                white_wins += 1
                print ("白赢+1", "黑AI获胜次数：", black_wins, "白AI获胜次数：", white_wins, "平局次数：", draw_game, "", file=logs)
            if i%50 == 0:
                # 选择其中胜率较高的一方，然后黑棋化，训练。每50次双方都采取相同策略。
                # print ("from white training")
                # ML_fit_2(np.asarray(sum_allgame_white), np.asarray(sum_allaction_white))
                # sum_allgame_white = []
                # sum_allaction_white = []
                # print ("from white training: done")
                # ML_fit_1(np.asarray(sum_allgame_black), np.asarray(sum_allaction_black))
                break
        # if i%10 == 0: print ("局目总数：", i, "黑AI获胜次数：", black_wins, "白AI获胜次数：", white_wins, "平局次数：", draw_game)
    logs.close()
    print("黑AI获胜次数：",black_wins,"白AI获胜次数：",white_wins,"平局次数：",draw_game)