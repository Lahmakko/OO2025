# world.py
class World:
    """
    Represents a grid-based world where players can move, interact with items,
    and perform actions like picking up items from the grid.

    Attributes:
        grid (list of list): A 2D grid representing the world where each cell can contain items or be empty.
        players (list): A list of players currently present in the world.
    """

    def __init__(self, width, height):
        """
        Initializes a new world with a given grid size.
        
        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.

        Preconditions:
            width > 0
            height > 0
        """
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        self.players = []

    def add_player(self, player, x, y):
        """
        Adds a player to the world at a specified position on the grid.
        
        Args:
            player (Player): The player object to add.
            x (int): The x-coordinate (column) on the grid.
            y (int): The y-coordinate (row) on the grid.

        Preconditions:
            0 <= x < self.width
            0 <= y < self.height
            player is an instance of the Player class
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            player.set_position(x, y)
            self.players.append(player)
        else:
            print(f"Invalid position: ({x}, {y})")

    def move_player(self, player, direction):
        """
        Moves a player in the specified direction on the grid (up, down, left, right).
        
        Args:
            player (Player): The player to move.
            direction (str): The direction to move the player ('up', 'down', 'left', 'right').

        Preconditions:
            player is an instance of the Player class
            direction is one of 'up', 'down', 'left', 'right'
        """
        x, y = player.get_position()
        
        if direction == 'up' and y > 0:
            player.set_position(x, y - 1)
        elif direction == 'down' and y < self.height - 1:
            player.set_position(x, y + 1)
        elif direction == 'left' and x > 0:
            player.set_position(x - 1, y)
        elif direction == 'right' and x < self.width - 1:
            player.set_position(x + 1, y)
        else:
            print(f"Cannot move {direction} from ({x}, {y})")

    def place_item(self, item, x, y):
        """
        Places an item in a specific grid cell.
        
        Args:
            item (Item): The item to place.
            x (int): The x-coordinate (column) on the grid.
            y (int): The y-coordinate (row) on the grid.

        Preconditions:
            0 <= x < self.width
            0 <= y < self.height
            item is an instance of the Item class
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = item
        else:
            print(f"Invalid position: ({x}, {y})")

    def remove_item(self, x, y):
        """
        Removes the item from a specified grid cell.
        
        Args:
            x (int): The x-coordinate (column) of the grid cell.
            y (int): The y-coordinate (row) of the grid cell.

        Preconditions:
            0 <= x < self.width
            0 <= y < self.height
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            self.grid[y][x] = None
        else:
            print(f"Invalid position: ({x}, {y})")

    def get_item_at(self, x, y):
        """
        Returns the item at a specific grid cell.
        
        Args:
            x (int): The x-coordinate (column) of the grid cell.
            y (int): The y-coordinate (row) of the grid cell.

        Returns:
            Item or None: The item at the grid position or None if no item is present.

        Preconditions:
            0 <= x < self.width
            0 <= y < self.height
        """
        if 0 <= x < self.width and 0 <= y < self.height:
            return self.grid[y][x]
        return None
