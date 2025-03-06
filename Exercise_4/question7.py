class Person:
    def __init__(self, name, height):
        self.name = name
        self.height = height
    
    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        # initialize an empty list to store persons
        self.persons = []
    
    def add(self, person):
        # adds the person to the room
        self.persons.append(person)
    
    def is_empty(self):
        # returns true if the room is empty else false
        return len(self.persons) == 0
    
    def print_contents(self):
        # print the contents of the room total number of persons and their combined height
        if self.persons:
            total_height = sum(person.height for person in self.persons)
            print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm.")
            for person in self.persons:
                print(person)
    
    def shortest(self):
        # returns the shortest person in the room or none if the room is empty
        if self.is_empty():
            return None
        return min(self.persons, key=lambda person: person.height)

# test code
room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))

# printing the contents of the room
print("Is the room empty?", room.is_empty())
print("Shortest:", room.shortest())  # this will print the shortest person's name
print()

# print the contents of the room
room.print_contents()
