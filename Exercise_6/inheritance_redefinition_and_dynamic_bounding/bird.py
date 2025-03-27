from animal import Animal

class Bird(Animal):

    def __init__(self, name="Bird"):
        super().__init__(2, name)  # Pass number_of_legs and name to the Animal class

    def make_sound(self):
        print("*clear bird singing*")
