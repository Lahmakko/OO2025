class Present:
    def __init__(self, name: str, weight: int):
        # Initializes the present with a name and weight
        self.name = name
        self.weight = weight
    
    def __str__(self):
        # Customized string representation for the present
        return f"{self.name} ({self.weight} g)"
    
book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
print("The name of the present:", book.name)
print("The weight of the present:", book.weight)
print("Present:", book)

class Box:
    def __init__(self):
        # Initializes the box with an empty list of presents and a total weight of 0
        self.presents = []
    
    def add_present(self, present):
        # Adds the given present to the box
        self.presents.append(present)
    
    def total_weight(self):
        # Returns the combined weight of all presents in the box
        return sum(present.weight for present in self.presents)
    

book = Present("Ta-Nehisi Coates: The Water Dancer", 200)
box = Box()
box.add_present(book)
print(box.total_weight())  # Output: 200

cd = Present("Pink Floyd: Dark Side of the Moon", 50)
box.add_present(cd)
print(box.total_weight())  # Output: 250
