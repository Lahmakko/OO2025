import random

def get_user_choice():
    """Kysyy käyttäjän valinnan ja palauttaa sen."""
    print("\nValitse:")
    print("1 - Kivi")
    print("2 - Paperi")
    print("3 - Sakset")
    while True:
        try:
            choice = int(input("Anna valintasi (1, 2, tai 3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Virheellinen valinta. Valitse 1, 2, tai 3.")
        except ValueError:
            print("Virheellinen syöte. Anna numero 1, 2 tai 3.")

def get_computer_choice():
    """Arpoo tietokoneen valinnan (1 - Kivi, 2 - Paperi, 3 - Sakset)."""
    return random.randint(1, 3)

def determine_winner(user_choice, computer_choice):
    """Päättele voittaja käyttäjän ja tietokoneen valintojen perusteella."""
    if user_choice == computer_choice:
        return "tie"  # Tasapeli
    elif (user_choice == 1 and computer_choice == 3) or \
         (user_choice == 2 and computer_choice == 1) or \
         (user_choice == 3 and computer_choice == 2):
        return "user"  # Käyttäjä voittaa
    else:
        return "computer"  # Tietokone voittaa

def choice_to_text(choice):
    """Muuttaa numerovalinnan tekstiksi."""
    if choice == 1:
        return "Kivi"
    elif choice == 2:
        return "Paperi"
    elif choice == 3:
        return "Sakset"

def print_score(user_score, computer_score):
    """Tulostaa nykyisen pistetilanteen."""
    print(f"\nTilanne: Sinä {user_score} - Tietokone {computer_score}")

def play_game():
    """Pelin pääohjelma."""
    user_score = 0
    computer_score = 0

    print("Tervetuloa Kivi-Paperi-Sakset peliin!")
    print("Ensimmäinen, joka saa 3 voittoa, voittaa pelin.\n")

    while user_score < 3 and computer_score < 3:
        # Käyttäjän ja tietokoneen valinnat
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        # Tulostetaan valinnat
        print(f"\nSinä valitsit: {choice_to_text(user_choice)}")
        print(f"Tietokone valitsi: {choice_to_text(computer_choice)}")

        # Selvitetään kierroksen voittaja
        winner = determine_winner(user_choice, computer_choice)

        if winner == "tie":
            print("Tasapeli! Ei pisteitä.")
        elif winner == "user":
            print("Voitit kierroksen!")
            user_score += 1
        else:
            print("Tietokone voitti kierroksen!")
            computer_score += 1

        # Tulostetaan nykyinen pistetilanne
        print_score(user_score, computer_score)

    # Päätetään peli ja ilmoitetaan voittaja
    if user_score == 3:
        print("\nOnneksi olkoon! Voitit pelin!")
    else:
        print("\nHävisit pelin! Tietokone voitti tällä kertaa.")

# Suoritetaan peli
if __name__ == "__main__":
    play_game()
