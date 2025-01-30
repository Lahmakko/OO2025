# File: coin.py
# Source: Tony Gaddis: Starting out with Python, fourth edition
# Modified by: Sanna Mastra & Anne Jumppanen
# Description: Coin object and tossing with additional outcomes

import random

# Class definition

class Coin:
    def __init__(self):
        self.sideup = 'Heads'

    def toss_the_coin(self):
        # Define the possible outcomes with their respective weights
        outcomes = [
            ('Heads', 40),  # 40% chance
            ('Tails', 40),  # 40% chance
            ('Upright', 15),  # 15% chance
            ('Rabbit Hole', 4),  # 4% chance
            ('Wormhole', 1)  # 1% chance
        ]
        
        # Extract the outcomes and their weights
        options, weights = zip(*outcomes)
        
        # Select an outcome based on the weights
        self.sideup = random.choices(options, weights=weights, k=1)[0]

    def get_sideup(self):
        return self.sideup

# Main function definition

def main():
    my_coin = Coin()

    print("Initial:", my_coin.get_sideup())

    print("Tossing...")
    my_coin.toss_the_coin()

    result = my_coin.get_sideup()
    print("Result:", result)
    
    # Provide minimal status based on the result
    if result == 'Heads':
        print("Heads up!")
    elif result == 'Tails':
        print("Tails up!")
    elif result == 'Upright':
        print("Landed upright!")
    elif result == 'Rabbit Hole':
        print("Disappeared into a rabbit hole.")
    elif result == 'Wormhole':
        print("Lost in a wormhole!")

# Calling the main function
main()