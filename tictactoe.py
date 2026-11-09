def game_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)


def check_winner(board, player):

    for i in range(3):

        if all(board[i][j] == player for j in range(3)):
            return True

        if all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2-i] == player for i in range(3)):
        return True

    return False


def play_game():

    board = [[" " for i in range(3)] for j in range(3)]

    player = "X"

    while True:

        game_board(board)

        print("Player", player)

        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Enter valid numbers.")
            continue

        if row not in range(3) or col not in range(3):
            print("Invalid position.")
            continue

        if board[row][col] != " ":
            print("Position already occupied.")
            continue

        board[row][col] = player

        if check_winner(board, player):
            game_board(board)
            print(player, "WINS!")
            break

        if all(board[i][j] != " " for i in range(3) for j in range(3)):
            game_board(board)
            print("DRAW!")
            break

        player = "O" if player == "X" else "X"


play_game()