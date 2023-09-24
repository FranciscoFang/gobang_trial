import numpy as np
from board_check import show_board, print_board, check_win_all, compare_board, combine_board, divide_board
from moves import machine_1, machine_2
from make_models import make_models
    
def ML_fit_1(allgame, allaction):
    a_game=np.array(allgame)
    a_action=np.array(allaction)
    model1.fit(a_game, a_action, epochs=200, verbose=0)
    prediction = model1.predict(np.array([divide_board(board)]))
    return np.argmax(prediction)

def ML_fit_2(allgame, allaction):
    a_game=np.array(allgame)
    a_action=np.array(allaction)
    model2.fit(a_game, a_action, epochs=200, verbose=0)
    prediction = model2.predict(np.array([divide_board(board)]))
    return np.argmax(prediction)

model1, model2 = make_models()

# if __name__ == '__main__':
epochs = 50 #as your wish
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
    allgame_black=[]
    allaction_black=[]
    allgame_white=[]
    allaction_white=[]
    black_play = True
    steps_count = 0
    while check_win_all(board) == 0:
        if len(sum_allgame_black) > 100:
            sum_allgame_black.pop(0)
            sum_allaction_black.pop(0)
            print("删除一个黑方旧样本")
        if len(sum_allgame_white) > 100:
            sum_allgame_white.pop(0)
            sum_allaction_white.pop(0)
            print("删除一个白方旧样本")
        if check_win_all(board) != 0: break
        print ("到黑方了")
        print (steps_count)
        while check_win_all(board) == 0 and black_play == True:
            return_board = machine_1(board, model1)
            allgame_black += [divide_board(board)]
            allaction_black += [return_board]
            board = combine_board(board, return_board)
            # print_board(show_board(board))
            steps_count += 1
            black_play = False
            if check_win_all(board) != 0: break
            if black_play == 0: break
            break
        if check_win_all(board) != 0: break
        print ("到白方了")
        print (steps_count)
        while check_win_all(board) == 0 and black_play == False:
            return_board = machine_2(board, model2)
            allgame_white += [divide_board(board)]
            allaction_white += [return_board]
            board = combine_board(board, return_board)
            # print_board(show_board(board))
            steps_count += 1
            black_play = True
            if check_win_all(board) != 0: break
            if black_play == True: break
            break
        if check_win_all(board) != 0: break
    if check_win_all(board) == 1:
        sum_allgame_black += allgame_black
        sum_allaction_black += allaction_black
        black_wins += 1
        print ("黑赢+1")
        ML_fit_1(np.asarray(sum_allgame_black), np.asarray(sum_allaction_black))
    if check_win_all(board) == -1:
        sum_allgame_white += allgame_white
        sum_allaction_white += allaction_white
        white_wins += 1
        print ("白赢+1")
        ML_fit_2(np.asarray(sum_allgame_white), np.asarray(sum_allaction_white))
    if  check_win_all(board) == 0 and steps_count == 225:
        draw_game += 1
        print ("平局+1")
    if steps_count == 225:
        break
print("黑AI获胜次数：",black_wins,"白AI获胜次数：",white_wins,"平局次数：",draw_game)