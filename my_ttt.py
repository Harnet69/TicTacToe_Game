import itertools


# winnings condition
def win_cond(current_game):
    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0:
            return True
        else:
            return False

    # horizontal
    for row in game:
        print(row)
        if all_same(row):
            print(f"Player {row[0]} is the winner horizontally!")
            return True

    # vertical
    for col in range(len(game[0])):
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check):
            print(f"Player {check[0]} is the winner vertically!")
            return True

    # / diagonal
    diags = []
    for idx, reverse_idx in enumerate(reversed(range(len(game)))):
        diags.append(game[idx][reverse_idx])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (/)")
        return True

    # \ diagonal
    diags = []
    for ix in range(len(game)):
        diags.append(game[ix][ix])

    if all_same(diags):
        print(f"Player {diags[0]} has won Diagonally (\\)")
        return True

    return False


def game_board(game_map, player=0, row=0, column=0, just_display=False):

    try:
        if game_map[row][column] != 0:
            print("This space is occupied, try another!")
            return False

        print("   "+"  ".join([str(i) for i in range(len(game_map))]))
        if not just_display:
            game_map[row][column] = player
        for count, row in enumerate(game_map):
            print(count, row)
        return game_map
    except IndexError:
        print("Hey!\nYou probably forgot in programming a counter starts from zero!\nTry again!")
        return False
    except Exception as e:
        print(str(e))
        return False


# scallable table
def scallable_tables_generator(game_size=3):
    game = []
    for i in range(game_size):
        row = []
        for i in range(game_size):
            row.append(0)
        game.append(row)

    return game


play = True
players = [1, 2]
while play:
    print('\033[H\033[J')
    print("WELCOME TO TicTacToe GAME FOR NOOBS IN PROGRAMMING!\n")
    game = scallable_tables_generator()
    game_won = False
    player_cycle = itertools.cycle([1, 2])
    game_board(game, just_display=True)
    while not game_won:
        current_player = next(player_cycle)
        played = False
        while not played:
            print(f"\nPlayer: {current_player}")
            column_choice = int(input("Choose the column: "))
            row_choice = int(input("Choose the row: "))
            print('\033[H\033[J')
            played = game_board(game, player=current_player, row=row_choice, column=column_choice)

        if win_cond(game):
            game_won = True
            again = input("Hey! Your your programmer skills have groved up!\nWant to improve it even more? (y/n) ")
            if again.lower() == "y":
                print("Nice to see you again!")
            elif again.lower() == "n":
                print("Bye, than...")
                play = False
            else:
                print("Unapropriate input, but... bye!")
                play = False
