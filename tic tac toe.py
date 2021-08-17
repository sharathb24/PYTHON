# this is just to make the code look beautiful
print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

# displaying a virtual representation 
board = ['-', '-', '-',
         '-', '-', '-',
         '-', '-', '-']

# creating global vars

# set game_going 
game_going = True

# winner is none
winner = None

# current player is x
current_player = 'x'


# creating the final board representation of the game
def print_board():
    print('\n')
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print('\n')


# the function that holds the main part of the game
def play_game():

    # printing the board
    print_board()

    # until game is going keep on looping
    while game_going:

        # calling handle_turn function
        handle_turn(current_player)

        # calling game_done function
        check_game_done()

        # calling flip player function
        flip_player()

        # if there is a winner then print it
        if winner == 'x' or winner == 'o':
            print(winner + ' is the winner\n')
            break


# the function that checks the input given by the user
def handle_turn(current_player):

    # take in the users input
    print(current_player, 'turn')
    position = input('Enter a position between 1 and 9: ')

    # check if the position is taken in the board
    valid = False
    while not valid:

        # if positon is not in 1 to 9 then ask again
        while position not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
            print_board()
            position = input('Invalid input! Enter a position between 1 and 9: ')

        position = int(position) - 1

        # check if position is already taken
        if board[position] == '-':
            valid = True
        else:
            print('The position is already taken!')

    # assign the var to the position
    board[position] = current_player
    print_board()


# check if the game is over
def check_game_done():
    check_for_winner()

# checks for the winner
def check_for_winner():

    # accesing global var
    global winner

    # interlinking the connections
    row_winner = check_rows()
    column_winner = check_columns()
    diagonal_winner = check_diagonals()

    # if winner then set in to winner
    if row_winner:
        winner = check_rows()
    elif column_winner:
        winner = check_columns()
    elif diagonal_winner:
        winner = check_diagonals()
    else:
        winner = None

# the check rows function
def check_rows():

    # if a row has same value i.e x or o the wins
    row1 = board[0] == board[1] == board[2] != '-'
    row2 = board[3] == board[4] == board[5] != '-'
    row3 = board[6] == board[7] == board[8] != '-'

    # returning the value of winner
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
    else:
        return None

# the check cols function
def check_columns():

    # if a row has same value i.e x or o the wins
    col1 = board[0] == board[3] == board[6] != '-'
    col2 = board[1] == board[4] == board[7] != '-'
    col3 = board[2] == board[5] == board[8] != '-'
    
    # returning the value of winner
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    else:
        return None

# the check diags function
def check_diagonals():

    # if a row has same value i.e x or o the wins
    diag1 = board[0] == board[4] == board[8] != '-'
    diag2 = board[2] == board[4] == board[6] != '-'

    # returning the value of winner
    if diag1:
        return board[0]
    elif diag2:
        return board[2]
    else:
        return None


# toggle between the two players
def flip_player():

    global current_player

    if current_player == 'x':
        current_player = 'o'
    elif current_player == 'o':
        current_player = 'x'

    return

# finally calling the play game function
play_game()