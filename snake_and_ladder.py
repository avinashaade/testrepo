
import random

snakes = {16: 6, 47: 26, 49: 11, 56: 53, 62: 19, 64: 60, 87: 24, 93: 73, 95: 75, 98: 78}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 100}

def roll_dice():
    return random.randint(1, 6)

def update_position(position, dice_roll):
    position += dice_roll
    if position > 100:
        return position - dice_roll
    if position in snakes:
        print(f"Oops! Bitten by a snake. Down to {snakes[position]}.")
        position = snakes[position]
    elif position in ladders:
        print(f"Yay! Climbed a ladder to {ladders[position]}.")
        position = ladders[position]
    return position

def play_game():
    player_positions = [0, 0]
    player_names = ["Player 1", "Player 2"]
    turn = 0

    while True:
        input(f"{player_names[turn]}'s turn. Press Enter to roll the dice...")
        dice_roll = roll_dice()
        print(f"{player_names[turn]} rolled a {dice_roll}.")
        
        player_positions[turn] = update_position(player_positions[turn], dice_roll)
        print(f"{player_names[turn]} is now at position {player_positions[turn]}.")
        
        if player_positions[turn] == 100:
            print(f"Congratulations! {player_names[turn]} wins!")
            break
        
        turn = 1 - turn

if __name__ == "__main__":
    play_game()
