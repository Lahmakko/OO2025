from carriage import Carriage
from train import Train

def main():
    """Runs a demo to test Carriage and Train functionality."""

    # Create carriages
    carriage1 = Carriage("C1", 10)
    carriage2 = Carriage("C2", 8)
    
    # Create a train with two carriages
    train = Train("T100", "City A", "City B", carriage1, carriage2)

    # Display train info
    print("\n--- Train Information ---")
    print(train.get_train_info())

    # Reserve seats
    print("\n--- Reserving Seats ---")
    train.reserve_seat()
    train.reserve_seat()

    # Display seat availability
    print("\n--- Seat Availability ---")
    train.display_seat_availability()

    # Add a new carriage
    print("\n--- Adding a New Carriage ---")
    carriage3 = Carriage("C3", 12)
    train.add_carriage(carriage3)
    train.display_seat_availability()

    # Remove a carriage (only once)
    print("\n--- Removing a Carriage (C2) ---")
    train.remove_carriage(carriage2)
    train.display_seat_availability()

    # Display final train info (one time only)
    print("\n--- Final Train Information ---")
    print(train.get_train_info())

if __name__ == "__main__":
    main()
