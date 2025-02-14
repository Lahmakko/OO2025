# main.py
from player import Player
from item import Item
from grid import Grid

def main():
    # Create a grid with dimensions 5x5
    world_grid = Grid(5, 5)

    # Create some items
    sword = Item("Sword", 10)
    shield = Item("Shield", 15)
    health_potion = Item("Health Potion", 5)

    # Place items on the grid
    world_grid.place_item(1, 1, sword)
    world_grid.place_item(3, 3, shield)
    world_grid.place_item(2, 2, health_potion)

    # Create a player
    player = Player("Player1", 0, 0)

    # Display the grid
    print("World Grid:")
    print(world_grid)

    # Test movement and item pickup
    player.move(1, 1, world_grid)  # Move to (1, 1)
    player.pick_up_item(world_grid)  # Pick up the sword

    player.move(2, 2, world_grid)  # Move to (2, 2)
    player.pick_up_item(world_grid)  # Pick up the health potion

    # Display the final state of the player and grid
    print("\nFinal State:")
    print(player)
    print("\nWorld Grid:")
    print(world_grid)

if __name__ == "__main__":
    main()
