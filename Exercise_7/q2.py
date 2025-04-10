import random

class Dice:
    def __init__(self):
        self.side = 1

    def roll(self):
        self.side = random.randint(1, 6)

    def get_side(self):
        return self.side

def play_game(dices):
    rolls = [dice.roll() or dice.get_side() for dice in dices]
    total = sum(rolls)
    print(f"Rolls: {rolls}, Total: {total}")
    return total

def main():
    num_dices = int(input("Enter the number of dices: "))
    dices = [Dice() for _ in range(num_dices)]
    num_players = int(input("Enter the number of players: "))
    players = {}
    for i in range(num_players):
        name = input(f"Enter name for player {i+1}: ")
        players[name] = dices[i % num_dices]
    while True:
        for name, dice in players.items():
            input(f"{name}'s turn. Press Enter to roll the dice...")
            dice.roll()
            print(f"{name} rolled a {dice.get_side()}")
        play_again = input("Play again? (y/n): ")
        if play_again.lower() != 'y':
            break

if __name__ == "__main__":
    main()
