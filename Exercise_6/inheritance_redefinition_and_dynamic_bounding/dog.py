from wolf import Wolf

class Dog(Wolf):
    def __init__(self, pack_name, name, breed):
        super().__init__(pack_name, name)
        assert isinstance(breed, str) and len(breed) > 0, "Breed must be a non-empty string"
        
        self.__breed = breed

    def get_breed(self):
        return self.__breed

    def set_breed(self, breed):
        assert isinstance(breed, str) and len(breed) > 0, "Breed must be a non-empty string"
        self.__breed = breed

    def show_breed(self):
        print(f"{self.get_name()} is a {self.__breed}.")

    def make_sound(self):
        print(f"{self.get_name()} barks loudly!")

    def fetch(self, item):
        print(f"{self.get_name()} fetched the {item}!")
