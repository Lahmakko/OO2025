from animal import Animal
from mammal import Mammal
from bird import Bird
from wolf import Wolf
from dog import Dog  

def run_encapsulation_tests():
    print("Running encapsulation tests...\n")
    
    # Test 1
    animal1 = Animal(4, "Cow")
    print(f"Original Name: {animal1.get_name()}")
    animal1.set_name("Bison")
    print(f"Updated Name: {animal1.get_name()}")
    
    # Test 2
    print(f"Original Number of Legs: {animal1.number_of_legs()}")
    animal1.set_legs(3)
    print(f"Updated Number of Legs: {animal1.number_of_legs()}")
    
    # Test 3
    try:
        print(animal1.get_name())
    except AttributeError as e:
        print(f"Error: {e}")

def run_mammal_tests():
    print("\nRunning Mammal tests...\n")
    
    # Test 1
    mammal1 = Mammal("Elephant")
    print(f"Mammal Name: {mammal1.get_name()}")
    
    # Test 2
    mammal1.make_sound()
    
    # Test 3
    mammal1.set_name("Tiger")
    print(f"Updated Mammal Name: {mammal1.get_name()}")

def run_bird_tests():
    print("\nRunning Bird tests...\n")
    
    # Test 1
    bird1 = Bird("Parrot")
    print(f"Bird Name: {bird1.get_name()}")
    
    # Test 2
    bird1.make_sound()
    
    # Test 3
    bird1.set_name("Eagle")
    print(f"Updated Bird Name: {bird1.get_name()}")

def run_wolf_tests():
    print("\nRunning Wolf tests...\n")
    
    # Test 1
    wolf1 = Wolf("Alpha Pack", "Alpha Wolf")
    print(f"Wolf Name: {wolf1.get_name()}")
    print(f"Pack Name: {wolf1.get_pack_name()}")
    
    # Test 2
    wolf1.make_sound()
    wolf1.another_make_sound()
    
    # Test 3
    wolf1.set_pack_name("Beta Pack")
    print(f"Updated Pack Name: {wolf1.get_pack_name()}")

def run_dog_tests():
    print("\nRunning Dog tests...\n")
    
    # Test 1
    dog1 = Dog("Alpha Pack", "Buddy", "Golden Retriever")
    print(f"Dog Name: {dog1.get_name()}")  
    dog1.show_breed()  
    
    # Test 2
    dog1.make_sound()  
    
    # Test 3
    dog1.set_breed("Labrador")
    dog1.show_breed()  
    
    # Test 4
    dog1.fetch("ball")  
    
    # Test 5
    dog1.set_breed("Poodle")
    print(f"Updated Breed: {dog1.get_breed()}")  
    
    # Test 6
    dog2 = Dog("Pack 2", "Charlie", "Beagle")
    dog2.show_breed()  
    dog2.make_sound()  
    
    # Test 7
    print(f"Pack Name: {dog2.get_pack_name()}")  
    print(f"Dog Name: {dog2.get_name()}")  
    print(f"Breed: {dog2.get_breed()}")  
    
    # Test 8
    dog2.make_sound()  
    
    # Test 9
    wolf = Wolf("Alpha Pack", "Alpha Wolf")
    wolf.make_sound()  
    
    # Test 10
    dog1.make_sound()  
    
    # Test 11
    dog3 = Dog("Pack 3", "Max", "Bulldog")
    dog3.show_breed()  
    dog3.make_sound()  

def run_all_tests():
    run_encapsulation_tests()
    run_mammal_tests()
    run_bird_tests()
    run_wolf_tests()
    run_dog_tests() 

run_all_tests()
