empty_box = " "

board = [empty_box for i in range(9)]

""" ou
for i in range(9):
    board.append(" ")
print(board)
"""
gamer =  "X"

while True:
    gamer_choice = 0

    while gamer_choice < 1 or gamer_choice > 9 or board[gamer_choice - 1] != empty_box:
      gamer_choice = int(input("Enter a box between 1 and 9 : "))

    board[gamer_choice - 1] = gamer

    for i in range(9):
        print(board[i], end=" ")
        if i % 3 == 2:
            print("")

    if empty_box != board[0] == board[1] == board[2] \
    or empty_box != board[3] == board[4] == board[5] \
    or empty_box != board[6] == board[7] == board[8] \
    or empty_box != board[0] == board[3] == board[6] \
    or empty_box != board[1] == board[4] == board[7] \
    or empty_box != board[2] == board[5] == board[8] \
    or empty_box != board[0] == board[4] == board[8] \
    or empty_box != board[2] == board[4] == board[6] :
        print("Gamer", gamer, "is the winner !")
        break

    gamer = "O" if gamer == "X" else "X"

    """
    if gamer == "X":
       gamer = "O"
    else:
        gamer = "X"
    """