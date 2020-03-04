#a tic tac toe game for 2 players to play on the same computer

from random import randint

def display_board(board):
    print('\n'*100)
    print('{}|{}|{}'.format(board[7],board[8],board[9]))
    print('---------')
    print('{}|{}|{}'.format(board[4],board[5],board[6]))
    print('---------')
    print('{}|{}|{}'.format(board[1],board[2],board[3]))

def assign_marker():
    marker = ''
    while not (marker == 'O' or marker == 'X'):
        marker = input('X or O ? ').upper()
    turn = randint(0,1)
    if turn == 1:
        return ('X','O')
    else:
        return ('O','X')

def space_check(board,position):
    return board[position] == position

def player_input():
    position = ''
    while not (position in [1,2,3,4,5,6,7,8,9]):
        position = int(input('What is your next move? (1-9) '))
    return position

def place_marker(board,marker,position):
    board[position] = marker

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def full_board_check(board):
    for i in board:
        if space_check(board,i):
            return False
    return True
def replay():
    play_again = input("play again? Y or N ")
    return play_again == 'Y'


while True:
    print('Welcome to Tic Tac Toe')

    board = [0,1,2,3,4,5,6,7,8,9]

    display_board(board)
    player1,player2 = assign_marker()

    while True:
        #player 1's actions
        print(f"{player1}'s turn")
        position = player_input()
        space_check(board,position)
        place_marker(board,player1,position)
        display_board(board)
        if win_check(board,player1):
            print("player 1 win")
            break
        if full_board_check(board):
            print('draw')
            break

        #player 2's actions
        print(f"{player2}'s turn")
        position = player_input()
        space_check(board,position)
        place_marker(board,player2,position)
        display_board(board)
        if win_check(board,player1):
            print("player 2 win")
            break
        if full_board_check(board):
            print('draw')
            break
        
    if replay():
        continue
    else:
        break
