# player.py
class Player:
    """
    Represents a player in the StoneAge world.
    
    Attributes:
        name (str): The name of the player.
        x (int): The x-coordinate (column) of the player's position.
        y (int): The y-coordinate (row) of the player's position.
        inventory (list): A list of items the player has picked up.
    """
    
    def __init__(self, name, x, y):
        """Initializes a player with a name and starting position.
        
        Args:
            name (str): The name of the player.
            x (int): The x-coordinate (column) of the player's starting position.
            y (int): The y-coordinate (row) of the player's starting position.
        """
        self.name = name
        self.x = x
        self.y = y
        self.inventory = []

    def move(self, x, y, world):
        """Moves the player to a new position on the grid.
        
        Args:
            x (int): The new x-coordinate (column) to move to.
            y (int): The new y-coordinate (row) to move to.
            world (World): The world where the player is moving.
        
        Preconditions:
            0 <= x < world.width
            0 <= y < world.height
        """
        if 0 <= x < world.width and 0 <= y < world.height:
            self.x = x
            self.y = y
        else:
            print(f"Invalid position: ({x}, {y})")

    def pick_up_item(self, world):
        """Picks up the item at the current position on the grid, if any.
        
        Args:
            world (World): The world where the player is interacting with items.
        """
        item = world.get_item_at(self.x, self.y)
        if item:
            self.inventory.append(item)
            world.remove_item(self.x, self.y)
            print(f"{self.name} picked up {item.name}.")
        else:
            print("No item to pick up here.")

    def __str__(self):
        """Returns a string representation of the player's state."""
        return f"{self.name} (Position: {self.x}, {self.y}, Inventory: {[item.name for item in self.inventory]})"
