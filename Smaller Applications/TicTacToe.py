"""
Created on Sun Feb  2 18:07:28 2020

@author: Wyatt Haak
"""

#Global Variables

#Board
board = ["-", "-", "-", 
         "-", "-", "-", 
         "-", "-", "-", ]
#If game is still going
game_still_going = True

#Who won or tie?
winner = None

#Whos turn is it?
current_player = 'X'

#Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#Check Win
def check_win():
    
    global winner
    
    #Check rows
    row_winner = check_rows()
    #Check colums
    column_winner = check_columns()
    #Check diagonals
    diagonal_winner = check_diagonals()
    
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    
    return

def check_rows():
    
    global game_still_going
    
    row_1 = board[0] == board[1] == board[2] != '-'
    row_2 = board[3] == board[4] == board[5] != '-'
    row_3 = board[6] == board[7] == board[8] != '-'
    
    if row_1 or row_2 or row_3:
        game_still_going = False
        
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return

def check_columns():
    
    global game_still_going
    
    column_1 = board[0] == board[3] == board[6] != '-'
    column_2 = board[1] == board[4] == board[7] != '-'
    column_3 = board[2] == board[5] == board[8] != '-'
    
    if column_1 or column_2 or column_3:
        game_still_going = False
        
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return

def check_diagonals():
    global game_still_going
    
    diagonal_1 = board[0] == board[4] == board[8] != '-'
    diagonal_2 = board[6] == board[4] == board[2] != '-'
    
    
    if diagonal_1 or diagonal_2:
        game_still_going = False
        
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[6]
    return

#Check Tie
def check_tie():
    
    global game_still_going
    
    if '-' not in board:
        game_still_going = False
    return

#Flip player
def flip_player():
    
    global current_player
    
    if current_player == 'X':
        current_player = 'O'
    elif current_player == 'O':
        current_player = 'X'
    return

def check_if_game_over():
    check_win()
    check_tie()
    return
#Play a game of tic tac toe
def play_game():
    
    #Display initial board
    display_board()
    
    #While the game is still going
    while game_still_going:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
        
    if winner == 'X' or winner == 'O':
        print(winner + ' won')
    elif winner == None:
        print('Tie')
    
#Handle turn
def handle_turn(player):
    
    print(player + "'s turn.")
    userPosition = input('Choose a position from 1-9: ')
    valid = False
    while not valid:
        
        while userPosition not in ['1','2','3','4','5','6','7','8','9']:
            userPosition = input('Invalid input. Choose a position from 1-9: ')
    
        userPosition = int(userPosition) - 1
    
        if board[userPosition] == '-':
            valid = True
        else:
            print("You can't go there. Go again.")
        
    
    board[userPosition] = player
    
    display_board()

play_game()