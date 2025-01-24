import random

#Määritetään funktio, joka palauttaa satunnaisen luvun 1 ja 6 välillä
def get_random_die_roll():
    return random.randint(1, 6)

#Kutsutaan funktiota ja tulosta tulos
roll_result = get_random_die_roll()
print(f"The rolled number is: {roll_result}")
