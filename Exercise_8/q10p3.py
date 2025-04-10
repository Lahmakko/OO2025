import json

# Function to load data from the JSON file
def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Function to search for a player by name
def search_player(players, name):
    for player in players:
        if player['name'].lower() == name.lower():
            return player
    return None

# Function to list all team abbreviations in alphabetical order
def list_teams(players):
    teams = sorted(set(player['team'] for player in players))
    return teams

# Function to list all country abbreviations in alphabetical order
def list_countries(players):
    countries = sorted(set(player['nationality'] for player in players))
    return countries

# Function to list players in a specific team
def players_in_team(players, team):
    return [player for player in players if player['team'] == team]

# Function to list players from a specific country
def players_from_country(players, country):
    return [player for player in players if player['nationality'] == country]

# Function to sort players by points (goals + assists)
def sort_by_points(players, n):
    players_sorted = sorted(players, key=lambda x: (x['goals'] + x['assists'], x['goals']), reverse=True)
    return players_sorted[:n]

# Function to sort players by goals
def sort_by_goals(players, n):
    players_sorted = sorted(players, key=lambda x: (x['goals'], -x['games']), reverse=True)
    return players_sorted[:n]

# Function to print player statistics in the required format
def print_player_stats(player):
    print(f"{player['name']: <20}{player['team']: <4} {player['goals']: >2} + {player['assists']: >2} = {player['goals'] + player['assists']: >3}")

# Main function to drive the program
def main():
    # Load the data from the file
    filename = input("Enter the file name (e.g., partial.json): ")
    players = load_data(filename)
    
    while True:
        # Show available commands
        print("\nCommands:")
        print("0 - Quit")
        print("1 - Search for player")
        print("2 - List teams")
        print("3 - List countries")
        print("4 - Players in team")
        print("5 - Players from country")
        print("6 - Most points")
        print("7 - Most goals")

        # Get the user's command
        command = input("Enter command: ")

        if command == '0':
            break
        elif command == '1':  # Search for player
            name = input("Enter the player's name: ")
            player = search_player(players, name)
            if player:
                print_player_stats(player)
            else:
                print(f"Player {name} not found.")
        elif command == '2':  # List teams
            teams = list_teams(players)
            print("Teams:", " ".join(teams))
        elif command == '3':  # List countries
            countries = list_countries(players)
            print("Countries:", " ".join(countries))
        elif command == '4':  # Players in team
            team = input("Enter team abbreviation: ")
            team_players = players_in_team(players, team)
            for player in team_players:
                print_player_stats(player)
        elif command == '5':  # Players from country
            country = input("Enter country abbreviation: ")
            country_players = players_from_country(players, country)
            for player in country_players:
                print_player_stats(player)
        elif command == '6':  # Most points
            how_many = int(input("How many: "))
            top_players = sort_by_points(players, how_many)
            for player in top_players:
                print_player_stats(player)
        elif command == '7':  # Most goals
            how_many = int(input("How many: "))
            top_players = sort_by_goals(players, how_many)
            for player in top_players:
                print_player_stats(player)
        else:
            print("Invalid command")

# Entry point of the program
if __name__ == '__main__':
    main()
