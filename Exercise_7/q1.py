class MagicPotion:
    def __init__(self, name):
        self.name = name
        self.ingredients = []

    def add_ingredient(self, ingredient, amount):
        self.ingredients.append((ingredient, amount))

    def print_recipe(self):
        print(f"{self.name}:")
        for ingredient, amount in self.ingredients:
            print(f"{ingredient} {amount} grams")

class SecretMagicPotion(MagicPotion):
    def __init__(self, name, password):
        super().__init__(name)
        self.password = password

    def add_ingredient(self, ingredient, amount, password):
        if password != self.password:
            raise ValueError("Wrong password!")
        super().add_ingredient(ingredient, amount)

    def print_recipe(self, password):
        if password != self.password:
            raise ValueError("Wrong password!")
        super().print_recipe()

# Example usage:
if __name__ == "__main__":
    diminuendo = SecretMagicPotion("Diminuendo maximus", "hocuspocus")
    diminuendo.add_ingredient("Toadstool", 1.5, "hocuspocus")
    diminuendo.add_ingredient("Magic sand", 3.0, "hocuspocus")
    diminuendo.add_ingredient("Frogspawn", 4.0, "hocuspocus")
    diminuendo.print_recipe("hocuspocus")
    try:
        diminuendo.print_recipe("wrongpassword")
    except ValueError as e:
        print(e)
