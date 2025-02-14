class Item:
    def __init__(self, name, value):
        """Initializes an item in the StoneAge world.
        
        Args:
            name (str): The name of the item.
            value (int): The monetary value of the item.
        """
        self.name = name
        self.value = value

    def __str__(self):
        return f"{self.name} (Value: {self.value})"
