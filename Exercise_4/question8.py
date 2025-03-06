class Recording:
    def __init__(self, length: int):
        # private variable for the length of the recording
        self.__length = length

    # getter method for the length
    @property
    def length(self):
        return self.__length

    # setter method for the length
    @length.setter
    def length(self, new_length: int):
        self.__length = new_length

# test code
the_wall = Recording(43)
print(the_wall.length)  # should print 43

the_wall.length = 44
print(the_wall.length)  # should print 44
