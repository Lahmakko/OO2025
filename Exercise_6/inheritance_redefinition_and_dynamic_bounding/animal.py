class Animal:
    def __init__(self, number_of_legs, name):
        assert isinstance(number_of_legs, int) and number_of_legs > 0, "Number of legs must be a positive integer"
        assert isinstance(name, str) and len(name) > 0, "Name must be a non-empty string"
        
        self.__legs = number_of_legs
        self.__name = name

    def number_of_legs(self):
        return self.__legs

    def get_name(self):
        return self.__name

    def set_name(self, name):
        assert isinstance(name, str) and len(name) > 0, "Name must be a non-empty string"
        self.__name = name

    # Add this method to set the number of legs
    def set_legs(self, number_of_legs):
        assert isinstance(number_of_legs, int) and number_of_legs > 0, "Number of legs must be a positive integer"
        self.__legs = number_of_legs
