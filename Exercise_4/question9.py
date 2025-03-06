class WeatherStation:
    def __init__(self, name: str):
        # private attribute for the name of the station
        self.__name = name
        # private list to store observations
        self.__observations = []

    # method to add an observation
    def add_observation(self, observation: str):
        self.__observations.append(observation)

    # method to get the latest observation
    def latest_observation(self):
        # return the latest observation or empty string if no observations
        if self.__observations:
            return self.__observations[-1]
        return ""

    # method to return the number of observations
    def number_of_observations(self):
        return len(self.__observations)

    # method to represent the object as a string
    def __str__(self):
        return f"{self.__name}, {self.number_of_observations()} observations"

# test code
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())  # should print "Sunny"
station.add_observation("Thunderstorm")
print(station.latest_observation())  # should print "Thunderstorm"
print(station.number_of_observations())  # should print 3
print(station)  # should print "Houston, 3 observations"
