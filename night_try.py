import itertools


# generate a sclable battlefild
def board_generator(game_size=3):
    game_board = []
    for i in range(game_size):  # takes a fields size as argument and return battlefield as list of lists 
        row = []
        for i in range(game_size):
            row.append(0)
        game_board.append(row)
    return game_board


# display a battlefild
def board_display(game_board, initial_bord=False):
    print('\033[H\033[J')
    print("WELCOME TO TicTacToe GAME FOR NOOBS IN PROGRAMMING!\n")
    print("   "+"  ".join([str(i) for i in range(len(game_board))]))
    for column, row in enumerate(game_board):  # display a battlefield in realtime 
        print(column, row)


# processing of user inputs
def users_input(player_cycle, playing_bord):
    current_player = next(player_cycle)
    print(f"\nPlayer: {current_player}")
    convertable = False
    while not convertable:
        try:
            user_col = int(input("Choose the column: "))
            user_row = int(input("Choose the row: "))
            if user_input_validator(playing_bord, user_col, user_row):
                convertable = True
        except ValueError:
            print("It's not a number")
    users_turn = [current_player, user_row, user_col]
    return users_turn


# display a battlefield after users move
def bord_performer(game_board, users_turn):
    current_player = users_turn[0]
    user_col = users_turn[1]
    user_row = users_turn[2]
    game_board[user_col][user_row] = current_player
    board_display(game_board)


# user inputs validator
def user_input_validator(game_board, user_col, user_row):
    if user_col > len(game_board)-1 or user_row > len(game_board)-1:  # TODO out of range didn't work
        print("Hey!\nYou probably forgot, in programming a counter starts from zero!\nTry again!")
        return False
    if game_board[user_row][user_col] != 0:  # if a spot isn't empty
        print("\nThis spot is occupied, try another!")
        return False

    return True


# winning condition checker (horizontal winning work on wide board)
def win_cond_performer(game_board):
    operated_table = []
    col_iterator = 0
    row_iterator = 0
    while col_iterator < len(game_board):
        while row_iterator <= len(game_board)-3:
            operated_table.append(game_board[col_iterator][row_iterator:row_iterator+3])
            row_iterator += 1
        row_iterator = 0
        col_iterator += 1
    if win_cond(operated_table):
        return True


# winnings condition
def win_cond(game_board):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal winning
    for row in game_board:
        if all_same(row):
            print(f"\nPlayer {row[0]} is the winner horizontally!\n")
            return True

    # vertical winning
    for col in range(len(game_board[0])):
        check = []
        for row in game_board:
            check.append(row[col])
        if all_same(check):
            print(f"\nPlayer {check[0]} wins vertically |\n")
            return True

    # / diagonal winning  TODO Why out of range exception occurs
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game_board)))):
        try:
            diags.append(game_board[idx][reverse_idx])
        except IndexError:
            pass
    if all_same(diags):
        print(f"\nPlayer {diags[0]} wins diagonally /\n")
        return True

    # \ diagonal winning TODO Why out of range exception occurs
    diags = []
    for ix in range(len(game_board)):
        try:
            diags.append(game_board[ix][ix])
        except IndexError:
                pass
    if all_same(diags):
        print(f"\nPlayer {diags[0]} wins diagonally \\ \n")
        return True

    # dead heat
    for row in game_board:
        if 0 in row:
            return False
    print(f"\nPlayer1 and Player2 have a DRAW!\n")
    return True


# point of entry
def main():
    playing_bord = board_generator(5)
    board_display(playing_bord)
    player_cycle = itertools.cycle([1, 2])  # iterator for players witch repeats indefinitely
    win_condition = False
    while not win_condition:
        bord_performer(playing_bord, users_input(player_cycle, playing_bord))
        win_condition = win_cond_performer(playing_bord)
    if win_condition:
        again = input("Hey! Your programmer skills have grown up!\n\nWant to improve it even more? (y/n) ")
        if again.lower() == "y":
            print("Nice to see you again!")
            main()
        elif again.lower() == "n":
            print("Bye, than...")
        else:
            print("Unapropriate input, but nevertheless... bye!")


if __name__ == "__main__":
    main()
