empty_box = " "

board = [empty_box for i in range(9)]

""" ou
for i in range(9):
    board.append(" ")
print(board)
"""
player =  "X"

def board_render():
    print(" ---+---+--- ")
    for i in range(9):
        print("|", board[i], end=" ")
        if i % 3 == 2:
            print("|")
            print(" ---+---+--- ")

while True:
    player_choice = 0
    board_render()

    while player_choice < 1 or player_choice > 9 or board[player_choice - 1] != empty_box:
      player_choice = int(input("Enter a box between 1 and 9 : "))

    board[player_choice - 1] = player

    if empty_box != board[0] == board[1] == board[2] \
    or empty_box != board[3] == board[4] == board[5] \
    or empty_box != board[6] == board[7] == board[8] \
    or empty_box != board[0] == board[3] == board[6] \
    or empty_box != board[1] == board[4] == board[7] \
    or empty_box != board[2] == board[5] == board[8] \
    or empty_box != board[0] == board[4] == board[8] \
    or empty_box != board[2] == board[4] == board[6] :
        print("Player", player, "is the winner !")
        board_render()
        restart = input("Do you want to play again ? (y/n)")
        if restart == "y" or restart == "Y":
            board = [empty_box for i in range(9)]
            player = "X"
            continue
        else:
            break

    if empty_box not in board:
        print("It's a draw!")
        board_render()
        restart = input("Do you want to play again ? (y/n)")
        if restart == "y" or restart == "Y":
            board = [empty_box for i in range(9)]
            player = "X"
            continue
        else:
            break

    player = "O" if player == "X" else "X"

    """
    if player == "X":
       player = "O"
    else:
        player = "X"
    """