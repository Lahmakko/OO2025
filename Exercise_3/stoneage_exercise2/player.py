class Player:
    def __init__(self, name, x, y):
        """Initializes a player in the StoneAge world with a starting position.
        
        Args:
            name (str): The name of the player.
            x (int): The starting x-coordinate (column).
            y (int): The starting y-coordinate (row).
        """
        self.name = name
        self.x = x
        self.y = y
        self.backpack = []

    def move(self, dx, dy, grid):
        """Moves the player in the grid by the specified delta values.
        
        Args:
            dx (int): The change in the x-coordinate (horizontal movement).
            dy (int): The change in the y-coordinate (vertical movement).
            grid (Grid): The grid in which the player is moving.
            
        Preconditions:
            (0 <= x + dx < grid.width) and (0 <= y + dy < grid.height)
        """
        new_x = self.x + dx
        new_y = self.y + dy

        # Ensure the new position is within the grid bounds
        if 0 <= new_x < grid.width and 0 <= new_y < grid.height:
            self.x = new_x
            self.y = new_y
            print(f"{self.name} moved to position ({self.x}, {self.y})")
        else:
            print(f"{self.name} cannot move outside the grid!")

    def pick_up_item(self, grid):
        """Picks up an item from the grid at the player's current position.
        
        Args:
            grid (Grid): The grid where the player is picking up the item.
            
        Preconditions:
            The player's current position must contain an item.
        """
        item = grid.grid[self.y][self.x]
        if item:
            self.backpack.append(item)
            grid.remove_item(self.x, self.y)
            print(f"{self.name} picked up a {item.name}")
        else:
            print(f"No item at position ({self.x}, {self.y}) to pick up.")
    
    def __str__(self):
        """Returns a string representation of the player."""
        return f"Player: {self.name}, Position: ({self.x}, {self.y}), Backpack: {', '.join([item.name for item in self.backpack])}"
