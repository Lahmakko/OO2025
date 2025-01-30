class RealProperty:
    def __init__(self, rooms: int, square_metres: int, price_per_sqm: int):
        self.rooms = rooms
        self.square_metres = square_metres
        self.price_per_sqm = price_per_sqm

    def bigger(self, compared_to) -> bool:
        """Returns True if the property is bigger than the compared property."""
        return self.square_metres > compared_to.square_metres

    def price_difference(self, compared_to) -> int:
        """Returns the absolute price difference between the properties."""
        self_price = self.square_metres * self.price_per_sqm
        compared_to_price = compared_to.square_metres * compared_to.price_per_sqm
        return abs(self_price - compared_to_price)

    def more_expensive(self, compared_to) -> bool:
        """Returns True if the property is more expensive than the compared property."""
        self_price = self.square_metres * self.price_per_sqm
        compared_to_price = compared_to.square_metres * compared_to.price_per_sqm
        return self_price > compared_to_price

central_studio = RealProperty(1, 16, 5500)
downtown_two_bedroom = RealProperty(2, 38, 4200)
suburbs_three_bedroom = RealProperty(3, 78, 2500)

# Part 1: Bigger comparison
print(central_studio.bigger(downtown_two_bedroom))  # False
print(suburbs_three_bedroom.bigger(downtown_two_bedroom))  # True

# Part 2: Price difference
print(central_studio.price_difference(downtown_two_bedroom))  # 71600
print(suburbs_three_bedroom.price_difference(downtown_two_bedroom))  # 35400

# Part 3: More expensive comparison
print(central_studio.more_expensive(downtown_two_bedroom))  # False
print(suburbs_three_bedroom.more_expensive(downtown_two_bedroom))  # True
