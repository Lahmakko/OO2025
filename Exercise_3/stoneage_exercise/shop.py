# shop.py
import random

class Item:
    def __init__(self, name, value):
        """Initializes an item with a name and value.
        
        Args:
            name (str): The name of the item.
            value (int): The monetary value of the item.
        """
        self.name = name
        self.value = value

class Shop:
    def __init__(self, items_for_sale):
        """Initializes the shop with a list of items for sale.
        
        Args:
            items_for_sale (list): A list of Item objects available for purchase.
        """
        self.items_for_sale = items_for_sale

    def buy_item(self, character, item):
        """Handles the logic of a character purchasing an item from the shop.
        
        Args:
            character (Character): The character buying the item.
            item (Item): The item to be bought.
        """
        if character.money >= item.value:
            character.money -= item.value
            character.add_item_to_backpack(item)
            print(f"{character.name} bought a {item.name}")
        else:
            print(f"{character.name} doesn't have enough money to buy {item.name}.")

    def sell_item(self, character, item):
        """Handles the logic of a character selling an item to the shop.
        
        Args:
            character (Character): The character selling the item.
            item (Item): The item to be sold.
        """
        if item in character.backpack:
            character.remove_item_from_backpack(item)
            character.money += item.value
            print(f"{character.name} sold a {item.name}")
        else:
            print(f"{character.name} doesn't have {item.name} in their backpack.")

    def gamble(self, character, gamble_item, target_item):
        """Handles the gambling feature where the character exchanges an item for a chance to get a target item.
        
        Args:
            character (Character): The character participating in the gamble.
            gamble_item (Item): The item the character is wagering.
            target_item (Item): The item the character hopes to win.
        """
        if gamble_item in character.backpack:
            if random.choice([True, False]):  # 50% success chance
                character.remove_item_from_backpack(gamble_item)
                character.add_item_to_backpack(target_item)
                print(f"{character.name} successfully gambled {gamble_item.name} for {target_item.name}.")
            else:
                print(f"{character.name}'s gamble failed.")
        else:
            print(f"{character.name} doesn't have {gamble_item.name} in their backpack.")

class Character:
    def __init__(self, name, strength, agility, money):
        """Initializes a character with their attributes and an empty backpack.
        
        Args:
            name (str): The name of the character.
            strength (int): The strength attribute of the character.
            agility (int): The agility attribute of the character.
            money (int): The amount of money the character has.
        """
        self.name = name
        self.strength = strength
        self.agility = agility
        self.money = money
        self.backpack = []

    def add_item_to_backpack(self, item):
        """Adds an item to the character's backpack.
        
        Args:
            item (Item): The item to add to the backpack.
        """
        self.backpack.append(item)

    def remove_item_from_backpack(self, item):
        """Removes an item from the character's backpack.
        
        Args:
            item (Item): The item to remove from the backpack.
        """
        if item in self.backpack:
            self.backpack.remove(item)
        else:
            print(f"{item.name} is not in the backpack!")

class Shopkeeper:
    def __init__(self, name, strength, agility, money, shop):
        """Initializes the shopkeeper with their attributes and the shop they manage.
        
        Args:
            name (str): The name of the shopkeeper.
            strength (int): The strength attribute of the shopkeeper.
            agility (int): The agility attribute of the shopkeeper.
            money (int): The money the shopkeeper has.
            shop (Shop): The shop that the shopkeeper manages.
        """
        self.name = name
        self.strength = strength
        self.agility = agility
        self.money = money
        self.shop = shop

    def assist_purchase(self, character, item):
        """Assists a character in purchasing an item from the shop.
        
        Args:
            character (Character): The character making the purchase.
            item (Item): The item to purchase.
        """
        self.shop.buy_item(character, item)

    def assist_sell(self, character, item):
        """Assists a character in selling an item to the shop.
        
        Args:
            character (Character): The character selling the item.
            item (Item): The item to sell.
        """
        self.shop.sell_item(character, item)

    def assist_gamble(self, character, gamble_item, target_item):
        """Assists a character in gambling an item for another item from the shop.
        
        Args:
            character (Character): The character participating in the gamble.
            gamble_item (Item): The item the character is gambling.
            target_item (Item): The item the character hopes to receive if they win.
        """
        self.shop.gamble(character, gamble_item, target_item)
