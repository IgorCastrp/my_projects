board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]

while True:
    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

    player_move = int(input('Choose a number location to play: '))
    if player_move <= 3:
        board[0][player_move - 1] = '0'
    elif 2 < player_move <= 6:
        board[1][player_move - 4] = '0'
    else:
        board[2][player_move - 7] = '0'

