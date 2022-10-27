import json
from isOdd import isOdd

#Создайте программу для игры в "Крестики-нолики" при помощи 
#виртуального окружения и PIP

board = list(range(1,10))

def design_board(board):
    print('-'*12)
    for i in range(3):
        print('|', board[0+i*3],'|', board[1+i*3], '|', board[2+i*3], '|')
        print('-'*12)


def choice(move):
    valid = False
    while not valid:
        player_index = input('Ваш ход, выберите ячейку ' + move + ' --> ')
        try:
            player_index =int(player_index)
        except:
            print('Что то не то нажали')
            continue
        if player_index >= 1 and player_index <= 9:
            if(str(board[player_index-1]) not in 'X0'): 
                board[player_index-1] = move
                valid = True
            else:
                print('Занято')
        else:
            print('Еще раз попробуй')

def victory_comb(board):
    victory = ((0,1,2),(3,4,5),(6,7,8),
               (0,3,6),(1,4,7),(2,5,8),
               (0,4,8),(2,4,6))
    for i in victory:
        if board[i[0]] == board[i[1]] == board[i[2]]:
            return board[i[0]]
    return False

def get_data():
    with open('file.json', 'r', encoding='utf-8') as f: 
        elem = json.load(f) 
        return elem

elem = get_data()

def game(board, elem):
    counter =0
    vic = False
    while not vic:
        design_board(board)
        if isOdd(counter):
            choice(elem["cross"])
        else:
            choice(elem["zero"])
        counter +=1
        
        if counter > 4:
            tt_win = victory_comb(board)
            if tt_win:
                print(tt_win,'Победа')
                vic = True
                break
        if counter == 9:
            print('Победила, ДРУЖБА)')
            break
        
game(board,elem)