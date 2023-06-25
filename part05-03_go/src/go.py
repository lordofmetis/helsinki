# Write your solution here
def who_won(game_board: list):
    player1 = []
    player2 = []

    for row in game_board:
        for square in row:
            if square == 2:
                player2.append(square)
            elif square == 1:
                player1.append(square)
    if len(player1) == len(player2):
        return 0
    elif len(player1) > len(player2):
        return 1
    else:
        return 2

if __name__ == "__main__":
    who_won([[1, 2, 1], [0, 0, 1], [2, 1, 0]])