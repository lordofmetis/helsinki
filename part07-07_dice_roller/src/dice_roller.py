# Write your solution here
from random import choice

def roll(die: str):

    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }

    if die in dice:
        return choice(dice[die])

def play(die1: str, die2: str, times: int):

    dice = {
        "A": [3, 3, 3, 3, 3, 6],
        "B": [2, 2, 2, 5, 5, 5],
        "C": [1, 4, 4, 4, 4, 4],
    }

    win = 0
    lose = 0
    ties = 0
    
    for _ in range(times):
        roll1 = choice(dice[die1])
        roll2 = choice(dice[die2])

        if roll1 > roll2:
            win += 1
        elif roll1 < roll2:
            lose += 1
        else:
            ties += 1
            
    return (win, lose, ties)

if __name__ == "__main__":
    result = play("A", "B", 100)
    print(result)