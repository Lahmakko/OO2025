class Carriage:
    """
    Represents a train carriage with a set number of seats.
    """

    def __init__(self, new_identifier, number_of_seats):
        """Initializes the current object."""
        self.__id = new_identifier
        self.__max_number_of_seats = number_of_seats
        self.__seats = []
        self.reset_seats()

    def reserve(self, free_seat_number):
        """Precondition: is_free(free_seat_number) and is_legal(free_seat_number)"""
        self.__seats[free_seat_number] = 1

    def make_free(self, reserved_seat_number):
        """Precondition: not is_free(reserved_seat_number) and is_legal(reserved_seat_number)"""
        self.__seats[reserved_seat_number] = 0

    def count_reserved(self):
        """Returns the total number of reserved seats."""
        result = 0
        for seat in self.__seats[1:]:
            if seat != 0:
                result += 1
        return result

    def is_free(self, free_seat_number):
        """Checks if a seat is free."""
        return self.__seats[free_seat_number] == 0

    def is_legal(self, seat_number):
        """Checks if the given seat number is within valid range."""
        return 1 <= seat_number <= self.__max_number_of_seats

    def max_seats(self):
        """Returns the maximum number of seats in the carriage."""
        return self.__max_number_of_seats

    def is_full(self):
        """Checks if all seats are reserved."""
        return self.count_reserved() >= self.max_seats()

    def reset_seats(self):
        """Resets all seats in the carriage to free."""
        self.__seats = [0] * (self.__max_number_of_seats + 1)  # Seat numbering starts at 1

    def reserved_seats_as_list(self):
        """Returns a list of reserved seat numbers."""
        return [i for i in range(1, len(self.__seats)) if not self.is_free(i)]

    def __str__(self):
        """String representation of the carriage's seat status."""
        return f"{self.__id}: {self.__seats[1:]}"
