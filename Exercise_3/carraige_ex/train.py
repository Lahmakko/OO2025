from carriage import Carriage

class Train:
    """
    Represents a train that consists of multiple carriages.
    Allows adding/removing carriages, reserving seats, and displaying seat availability.
    """

    def __init__(self, train_id, departure, destination, *carriages):
        """
        Initializes a Train object.
        
        :param train_id: Unique identifier for the train.
        :param departure: Departure location.
        :param destination: Destination location.
        :param carriages: At least one Carriage object.
        :raises ValueError: If no carriages are provided.
        """
        if not carriages:
            raise ValueError("A train must have at least one carriage.")
        
        self.__train_id = train_id
        self.__departure = departure
        self.__destination = destination
        self.__carriages = list(carriages)  # Preserve order of carriages

    def add_carriage(self, carriage):
        """
        Adds a carriage to the end of the train.
        
        :param carriage: A Carriage object to be added.
        """
        self.__carriages.append(carriage)

    def remove_carriage(self, carriage):
        """
        Removes a specific carriage from the train.
        
        :param carriage: The Carriage object to be removed.
        :raises ValueError: If the train has only one carriage.
        """
        if len(self.__carriages) == 1:
            raise ValueError("A train must have at least one carriage.")
        
        self.__carriages.remove(carriage)

    def reserve_seat(self):
        """
        Reserves a seat in the first available carriage.
        
        :return: The carriage where the seat was reserved.
        :raises ValueError: If no seats are available.
        """
        for carriage in self.__carriages:
            for seat_number in range(1, carriage.max_seats() + 1):
                if carriage.is_free(seat_number):
                    carriage.reserve(seat_number)
                    return carriage
        
        raise ValueError("No available seats in any carriage.")

    def display_seat_availability(self):
        """
        Displays all reserved and free seats in the train.
        """
        print(f"Train {self.__train_id} - Seat Availability")
        for i, carriage in enumerate(self.__carriages, start=1):
            print(f"Carriage {i}: {carriage}")

    def get_train_info(self):
        """
        Returns details about the train, including its carriages.
        """
        return {
            "Train ID": self.__train_id,
            "Departure": self.__departure,
            "Destination": self.__destination,
            "Number of Carriages": len(self.__carriages),
            "Carriages Info": [str(carriage) for carriage in self.__carriages]
        }

    def __str__(self):
        """
        String representation of the train.
        """
        return f"Train {self.__train_id} from {self.__departure} to {self.__destination} with {len(self.__carriages)} carriages."
