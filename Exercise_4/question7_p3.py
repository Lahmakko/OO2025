class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height
    
    def __str__(self):
        return f"{self.name} ({self.height} cm)"

class Room:
    def __init__(self):
        self.persons = []
    
    def add(self, person: Person):
        """add a person to the room"""
        self.persons.append(person)
    
    def is_empty(self):
        """return True if the room is empty, else False"""
        return len(self.persons) == 0
    
    def print_contents(self):
        """print the contents of the room"""
        if self.is_empty():
            print("The room is empty.")
            return
        
        total_height = sum(person.height for person in self.persons)
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm.")
        
        for person in self.persons:
            print(person)
    
    def shortest(self):
        """return the shortest person in the room or None if the room is empty"""
        if self.is_empty():
            return None
        return min(self.persons, key=lambda person: person.height)
    
    def remove_shortest(self):
        """remove the shortest person from the room and return the reference to the person"""
        if self.is_empty():
            return None
        
        shortest_person = self.shortest()
        self.persons.remove(shortest_person)
        return shortest_person
# testing the implementation
room = Room()
room.add(Person("Lea", 183))
room.add(Person("Kenya", 172))
room.add(Person("Ally", 166))
room.add(Person("Nina", 162))
room.add(Person("Dorothy", 175))

# print the current room state
print("Is the room empty?", room.is_empty())
room.print_contents()

# remove the shortest person and print the result
removed = room.remove_shortest()
print(f"Removed from room: {removed.name}")
print()

# print the new room state after removing the shortest person
room.print_contents()
