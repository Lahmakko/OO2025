import random

#luon tyhjät listat numeroille ja merkkijonoille
numbers = []
strings = []

#kysyn käyttäjältä 10 numeroa
print("Anna 10 numeroo:")
for i in range(10):
    number = int(input(f"Anna numero {i+1}: "))
    numbers.append(number)

#kysyn käyttäjältä 10 merkkijonoa
print("\nAnna 10 merkkijonoa:")
for i in range(10):
    string = input(f"Anna merkkijono {i+1}: ")
    strings.append(string)

#tulostan listat
print("\nNumeroiden lista:")
print(numbers)
print("\nMerkkijonojen lista:")
print(strings)

#täytän numeroiden listan satunnaisilla numeroilla
print("\nTäytän numeroiden listan satunnaisilla numeroilla...")
for i in range(10):
    numbers[i] = random.randint(1, 100)

#tulostan päivitetyn numeroiden listan
print("\nPäivitetty numeroiden lista (satunnaiset numerot):")
print(numbers)
