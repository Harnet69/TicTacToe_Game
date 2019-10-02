import pprint

# Player class
class Player:
    def __init__(self, name, mark):
        self.name = name
        self.mark = mark

    # Invoked when player makes a move
    def move(self):
        move = input("Please Enter Move: ")
        i = int(move[0])
        j = int(move[1])
        if i > size-1 or j > size-1 or board[i][j] == "X" or board[i][j] == "O" or board[i][j] == "Z":
            print("Invalid Move")
            self.move()
        else:
            board[i][j] = self.mark
            displayBoard()
            check(i,j)

        if gameover:
            print("{} has won the game".format(self.name))
            print("Thanks for playing!!!")
            quit()

# Global variables
board = []
gameover = False

# Draws the board
def displayBoard():
    pprint.pprint(board)

# Check if previous move resulted in a win
def check(i,j):
    global gameover
    if size == 5:
        # Check win on vertical line
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j]:
            gameover = True
        # Check win on horizontal line
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4]:
            gameover = True
        # Check win on diagonal left to right
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]:
            gameover = True
        # Check win on diagonal right to left
        if i + j == (size - 1) and board[0][4] == board[1][3] == board[2][2] == board[3][1] == board[4][0]:
            gameover = True
    elif size == 6:
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == board[5][j]:
            gameover = True
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5]:
            gameover = True
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]== board[5][5]:
            gameover = True
        if i + j == (size - 1) and board[0][5] == board[1][4] == board[2][3] == board[3][2] == board[4][1] == board[5][0]:
            gameover = True
    elif size == 7:
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == board[5][j] == board[6][j]:
            gameover = True
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5] == board[i][6]:
            gameover = True
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]== board[5][5] == board[6][6]:
            gameover = True
        if i + j == (size - 1) and board[0][6] == board[1][5] == board[2][4] == board[3][3] == board[4][2] == board[5][1] == board[6][0]:
            gameover = True
    elif size == 8:
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == board[5][j] == board[6][j] == board[7][j]:
            gameover = True
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5] == board[i][6] == board[i][7]:
            gameover = True
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]== board[5][5] == board[6][6] == board[7][7]:
            gameover = True
        if i + j == (size - 1) and board[0][7] == board[1][6] == board[2][5] == board[3][4] == board[4][3] == board[5][2] == board[6][1] == board[7][0]:
            gameover = True
    elif size == 9:
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == board[5][j] == board[6][j] == board[7][j] == board[8][j]:
            gameover = True
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5] == board[i][6] == board[i][7] == board[i][8]:
            gameover = True
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]== board[5][5] == board[6][6] == board[7][7] == board[8][8]:
            gameover = True
        if i + j == (size - 1) and board[0][8] == board[1][7] == board[2][6] == board[3][5] == board[4][4] == board[5][3] == board[6][2] == board[7][1] == board[8][0]:
            gameover = True
    elif size == 10:
        if board[0][j] == board[1][j] == board[2][j] == board[3][j] == board[4][j] == board[5][j] == board[6][j] == board[7][j] == board[8][j] == board[9][j]:
            gameover = True
        if board[i][0] == board[i][1] == board[i][2] == board[i][3] == board[i][4] == board[i][5] == board[i][6] == board[i][7] == board[i][8] == board[i][9]:
            gameover = True
        if i == j and board[0][0] == board[1][1] == board[2][2] == board[3][3] == board[4][4]== board[5][5] == board[6][6] == board[7][7] == board[8][8] == board[9][9]:
            gameover = True
        if i + j == (size - 1) and board[0][9] == board[1][8] == board[2][7] == board[3][6] == board[4][5] == board[5][4] == board[6][3] == board[7][2] == board[8][1] == board[9][0]:
            gameover = True

# User specifies size of grid, must be between 5 & 10
size = int(input("Please Enter Grid Size: "))

if size > 10:
    print("Too Big, grid size should be between 5 & 10")
elif size < 5:
    print("Too Small, grid size should be between 5 & 10")
else:
    print("Game Starting! Select move by specifing a two digit number where the first digit represents " +
          "the row and the second represents the column. \nFor example the top left column is 00")
    board = [[" "] * size for i in range(size)]
    displayBoard()

# 3 Players prompted in turn for their move, will continue untill a player wins
while not gameover:
    first = Player("First Player", "X")
    first.move()

    second = Player("Second Player", "O")
    second.move()

    third = Player("Third Player", "Z")
    third.move()
    