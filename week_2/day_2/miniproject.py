def display_board(board):
    print(f"{board[0][0]} | {board[0][1]} | {board[0][2]}" )
    print("---------")
    print(f"{board[1][0]} | {board[1][1]} | {board[1][2]}")
    print("---------")      
    print(f"{board[2][0]} | {board[2][1]} | {board[2][2]}")
    print("\n")

def player_input(player, board):
    row=int(input(f"{player}, enter a row between 0 and 2:"))
    column=int(input(f"{player}, enter a column between 0 and 2:"))
    if row not in range(3) and column not in range(3):
        print("Invalid input. Please try again.")
        return player_input(player, board)
    elif board[row][column] != " ":
        print("This cell is already occupied. Please try again.")
        return player_input(player, board)
    else: return row, column


def check_win(board, player):
    for row in range(3):
        if board[row][1]== board[row][2] == board[row][0] == player:
            return True
    for column in range(3):
        if board[0][column] == board[1][column] == board[2][column] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

def check_tie(board):
    for row in board:
        if " " in row:
            return False
    for column in board:
        if " " in column:
            return False
    return True


current_player= "X"
print("player 1 is and player 2 is 0")
board=[[" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]]

while True:
    display_board(board)
    row, column = player_input(current_player, board)
    board[row][column] = current_player

    if check_win(board, current_player):
        display_board(board)
        print(f"Congratulations {current_player}, you win!")
        break

    if check_tie(board):
        display_board(board)
        print("It's a tie!")
        break

    current_player = "O" if current_player == "X" else "X"



