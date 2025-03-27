from animal import Animal

class Mammal(Animal):

    def __init__(self, name="Mammal"):
        super().__init__(4, name)  # Pass number_of_legs and name to the Animal class

    def make_sound(self): 
        print("*mammal breathing*")
