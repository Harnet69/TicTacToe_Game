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


def bord_performer(game_board, users_turn):
    current_player = users_turn[0]
    user_col = users_turn[1]
    user_row = users_turn[2]
    game_board[user_col][user_row] = current_player
    board_display(game_board)


def user_input_validator(game_board, user_col, user_row):
    if user_col > len(game_board)-1 or user_row > len(game_board)-1:  # TODO out of range didn't work
        print("\nThis spot is not exists, give another coordinates!")
        return False
    if game_board[user_col][user_row] != 0:  # if a spot isn't empty
        print("\nThis spot is occupied, try another!")
        return False

    return True


# winnings condition
def win_cond(game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False


    # TODO dead heat


    # horizontal winning
    for row in game:
        print(row)
        if all_same(row):
            print(f"\nPlayer {row[0]} is the winner horizontally!\n")
            return True

    # vertical winning
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"\nPlayer {check[0]} wins vertically |\n")
            return True

    # / diagonal winning
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"\nPlayer {diags[0]} wins diagonally /\n")
        return True

    # \ diagonal winning
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"\nPlayer {diags[0]} wins diagonally \\ \n")
        return True

    return False


def main():
    playing_bord = board_generator(3)
    board_display(playing_bord)
    player_cycle = itertools.cycle([1, 2])  # iterator for players witch repeats indefinitely
    #print(board_display(board_generator(3)))
    win_condition = False
    while not win_condition:
        bord_performer(playing_bord, users_input(player_cycle, playing_bord))


if __name__ == "__main__":
    main()
