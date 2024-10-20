def print_board(board):
    for row in board:
        print(" ".join(row))


def check_pairs(board):
    pairs = []
    for i in range(3):
        for j in range(9):
            if i < 2 and board[i][j] == board[i + 1][j]:
                pairs.append((i, j))
            if j < 8 and board[i][j] == board[i][j + 1]:
                pairs.append((i, j))
            if i < 2 and board[i][j] + board[i + 1][j] == 10:
                pairs.append((i, j))
            if j < 8 and board[i][j] + board[i][j + 1] == 10:
                pairs.append((i, j))
    return pairs


def update_board(board, pairs):
    for pair in pairs:
        i, j = pair
        board[i][j] = " "
        if i < 2 and board[i + 1][j] != " ":
            board[i + 1][j] = " "
        if j < 8 and board[i][j + 1] != " ":
            board[i][j + 1] = " "


def check_end_game(board):
    for row in board:
        if any(cell != " " for cell in row):
            return False
    return True


board = [["1", "2", "3", "4", "5", "6", "7", "8", "9"],
         ["1", "2", "3", "4", "5", "6", "7", "8", "9"],
         ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
         ]

while not check_end_game(board):
    print_board(board)
    pairs = check_pairs(board)
    if not pairs:
        print("Game over! You win!")
        break
    else:
        print("Pairs found at:")
        for pair in pairs:
            print(pair)

    i = int(input("Enter row number: "))
    j = int(input("Enter column number: "))

    if (i, j) not in pairs:
        print("Invalid move! Pair not found at this position.")
        continue

    update_board(board, m[(i, j)])

print_board(board)