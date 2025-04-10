class Person:
    def __init__(self, name):
        self.name = name
        self.numbers = []
        self.address = None

    def add_number(self, number):
        self.numbers.append(number)

    def add_address(self, address):
        self.address = address

    def get_entry(self):
        numbers = ', '.join(self.numbers) if self.numbers else 'No numbers'
        address = self.address if self.address else 'No address'
        return f"{self.name}\nNumbers: {numbers}\nAddress: {address}"

class PhoneBook:
    def __init__(self):
        self.__persons = {}

    def add_number(self, name, number):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_number(number)

    def add_address(self, name, address):
        if name not in self.__persons:
            self.__persons[name] = Person(name)
        self.__persons[name].add_address(address)

    def get_entry(self, name):
        if name in self.__persons:
            return self.__persons[name].get_entry()
        else:
            return f"No entry found for {name}"

# Example usage:
if __name__ == "__main__":
    phonebook = PhoneBook()
    phonebook.add_number("Eric", "040-123456")
    phonebook.add_address("Eric", "Mannerheimintie 10, Helsinki")
    phonebook.add_number("Emily", "050-654321")
    phonebook.add_address("Emily", "Viherlaaksontie 7, Espoo")
    print(phonebook.get_entry("Eric"))
    print(phonebook.get_entry("Emily"))
    print(phonebook.get_entry("John"))
