board = [
    ["1", "2", "3"],
    ["4", "X", "6"],
    ["7", "8", "9"]
]

player_move = int(input('Choose a number location to play: '))
if player_move <= 2:
    board[[0][player_move - 1]] = '0'

print(board)