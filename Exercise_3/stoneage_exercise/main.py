# Import the necessary classes from the shop module
from shop import Shop, Shopkeeper, Character, Item

def main():
    # Create some items
    sword = Item("Sword", 50)
    shield = Item("Shield", 30)
    health_potion = Item("Health Potion", 20)

    # Create a list of items the shop has for sale
    items_for_sale = [sword, shield, health_potion]

    # Create a shop with the available items
    shop = Shop(items_for_sale)

    # Create a player character with some money and an empty backpack
    player = Character("Player1", 10, 5, 100)  # Name, strength, agility, money

    # Add some items to the player's backpack for testing
    player.add_item_to_backpack(sword)
    player.add_item_to_backpack(shield)

    # Create a shopkeeper who manages the shop
    shopkeeper = Shopkeeper("Bob", 10, 5, 100, shop)

    print("Starting the shop interaction...")

    # Test buying an item
    print("\nAttempting to buy a Health Potion:")
    shopkeeper.assist_purchase(player, health_potion)

    # Test selling an item
    print("\nAttempting to sell a Sword:")
    shopkeeper.assist_sell(player, sword)

    # Test gambling an item for another item
    print("\nAttempting to gamble a Shield for a Health Potion:")
    shopkeeper.assist_gamble(player, shield, health_potion)

    # Show player's final backpack and money
    print(f"\nFinal Backpack: {[item.name for item in player.backpack]}")
    print(f"Final Money: {player.money}")

if __name__ == "__main__":
    main()
