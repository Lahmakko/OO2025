class Grid:
    def __init__(self, width, height):
        """Initializes the world grid where players and items are placed.
        
        Args:
            width (int): The number of columns in the grid.
            height (int): The number of rows in the grid.
        """
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]  # Empty grid

    def place_item(self, x, y, item):
        """Places an item on the grid at the specified coordinates.
        
        Args:
            x (int): The x-coordinate (column).
            y (int): The y-coordinate (row).
            item (Item): The item to place on the grid.
        """
        self.grid[y][x] = item

    def remove_item(self, x, y):
        """Removes an item from the grid at the specified coordinates.
        
        Args:
            x (int): The x-coordinate (column).
            y (int): The y-coordinate (row).
        """
        self.grid[y][x] = None

    def __str__(self):
        """Returns a string representation of the grid."""
        grid_str = ""
        for row in self.grid:
            grid_str += " | ".join([str(cell) if cell else "Empty" for cell in row]) + "\n"
        return grid_str
