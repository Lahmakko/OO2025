import json

# Function to read data from a JSON file
def read_data(file_name):
    with open(file_name, "r") as file:
        return json.load(file)

# Function to print a player's stats in the required format
def print_player_stats(player):
    goals = player["goals"]
    assists = player["assists"]
    points = goals + assists
    print(f"{player['name']: <25}{player['team']: <3}{goals: >2} + {assists: >2} = {points: >3}")

# Function to search for a player by name
def search_player(data, name):
    player = next((p for p in data if p["name"].lower() == name.lower()), None)
    if player:
        print_player_stats(player)
    else:
        print(f"Player {name} not found.")

# Function to list team abbreviations in alphabetical order
def list_teams(data):
    teams = sorted(set(player["team"] for player in data))
    print(" ".join(teams))

# Function to list country abbreviations in alphabetical order
def list_countries(data):
    countries = sorted(set(player["nationality"] for player in data))
    print(" ".join(countries))

# Function to list players in a specific team
def players_in_team(data, team):
    players_in_team = [player for player in data if player["team"].lower() == team.lower()]
    for player in players_in_team:
        print_player_stats(player)

# Function to list players from a specific country
def players_from_country(data, country):
    players_from_country = [player for player in data if player["nationality"].lower() == country.lower()]
    for player in players_from_country:
        print_player_stats(player)

# Function to find the player with the most points
def most_points(data):
    most_points_player = max(data, key=lambda player: player["goals"] + player["assists"])
    print_player_stats(most_points_player)

# Function to find the player with the most goals
def most_goals(data):
    most_goals_player = max(data, key=lambda player: player["goals"])
    print_player_stats(most_goals_player)

# Main function to drive the interactive menu
def main():
    file_name = input("Enter the file name (e.g., partial.json): ")
    data = read_data(file_name)

    while True:
        print("\nCommands:")
        print("0 - Quit")
        print("1 - Search for player")
        print("2 - List teams")
        print("3 - List countries")
        print("4 - Players in team")
        print("5 - Players from country")
        print("6 - Most points")
        print("7 - Most goals")

        command = input("Enter command: ")

        if command == "0":
            print("Exiting...")
            break
        elif command == "1":
            name = input("Enter player's name: ")
            search_player(data, name)
        elif command == "2":
            list_teams(data)
        elif command == "3":
            list_countries(data)
        elif command == "4":
            team = input("Enter team abbreviation: ")
            players_in_team(data, team)
        elif command == "5":
            country = input("Enter country abbreviation: ")
            players_from_country(data, country)
        elif command == "6":
            most_points(data)
        elif command == "7":
            most_goals(data)
        else:
            print("Invalid command.")

# Run the program
if __name__ == "__main__":
    main()
