import winning_comb


# generate an initial battles field
def table_display(battle_field):
    print('\033[H\033[J')
    print("TIC TAC TOE GAME")
    for i in battle_field:
        print(i[0], i[1], i[2])
    return battle_field


# users_movements
def user_movements(battle_field):
    dod = 0
    while dod < 3 :
        print("Player1(X) movement")
        raw = int(input("GIve a raw: "))
        column = int(input("GIve a column: "))
        print('\033[H\033[J')
        battle_field[raw-1][column-1] = "X"
        table_display(battle_field)
        dod += 1
    return battle_field


# check if DoD happened
def wins_checker(user_movements):
    if user_movements in winning_comb.winning_combinations:
        print("You WIN!!!")


def main():
    wins_checker(user_movements(table_display(winning_comb.battle_field)))


if __name__ == "__main__":
    main()