class Car:
    def __init__(self, make: str, top_speed: int):
        self.make = make
        self.top_speed = top_speed

    def __str__(self):
        return f"Car (brand: {self.make}, top speed: {self.top_speed})"

# I added the fastest_car function here
def fastest_car(cars: list) -> str:
    # I used the max() function to find the car with the highest top_speed
    return max(cars, key=lambda car: car.top_speed).make  # I return the make of the fastest car

if __name__ == "__main__":  
    car1 = Car("Saab", 195)
    car2 = Car("Lada", 110)
    car3 = Car("Ferrari", 280) 
    car4 = Car("Trabant", 85)

    cars = [car1, car2, car3, car4]
    print(fastest_car(cars))  
