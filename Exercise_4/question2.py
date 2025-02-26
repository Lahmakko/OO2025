class NumberStats:
    def __init__(self):
        # Using a list to store numbers instead of a single integer
        self.numbers = []

    def add_number(self, number: int):
        self.numbers.append(number)

    def count_numbers(self):
        return len(self.numbers)
    
    def get_sum(self):
        return sum(self.numbers)
    
    def average(self):
        if self.count_numbers() == 0:
            return 0
        return self.get_sum() / self.count_numbers()

if __name__ == "__main__":
    # Part 1 test prints:
    stats = NumberStats()
    stats.add_number(3)
    stats.add_number(5)
    stats.add_number(1)
    stats.add_number(2)
    print("Numbers added:", stats.count_numbers())
    
    # Part 2 test prints:
    print("Sum of numbers:", stats.get_sum())
    print("Mean of numbers:", stats.average())
    
    # Part 3 & 4: User input with even and odd number tracking
    all_stats = NumberStats()
    even_stats = NumberStats()
    odd_stats = NumberStats()
    
    print("Please type in integer numbers:")
    while True:
        number = int(input())
        if number == -1:
            break
        all_stats.add_number(number)
        if number % 2 == 0:
            even_stats.add_number(number)
        else:
            odd_stats.add_number(number)
    
    print("Sum of numbers:", all_stats.get_sum())
    print("Mean of numbers:", all_stats.average())
    print("Sum of even numbers:", even_stats.get_sum())
    print("Sum of odd numbers:", odd_stats.get_sum())
