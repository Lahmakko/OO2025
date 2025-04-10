class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        # Format player output in the specified format
        return f"{self.name:<20}{self.team:>4} {self.goals:2} + {self.assists:2} = {self.points():3}"

# Load the players data from JSON
import json

def load_players(file_name):
    with open(file_name, "r") as file:
        data = json.load(file)
    players = []
    for player_data in data:
        player = Player(
            name=player_data["name"],
            nationality=player_data["nationality"],
            assists=player_data["assists"],
            goals=player_data["goals"],
            penalties=player_data["penalties"],
            team=player_data["team"],
            games=player_data["games"]
        )
        players.append(player)
    return players
def list_players_in_team(players, team_abbr):
    # Filter players by team and sort by points
    team_players = [player for player in players if player.team == team_abbr]
    sorted_players = sorted(team_players, key=lambda player: player.points(), reverse=True)
    
    for player in sorted_players:
        print(player)

def list_players_from_country(players, country_abbr):
    # Filter players by nationality and sort by points
    country_players = [player for player in players if player.nationality == country_abbr]
    sorted_players = sorted(country_players, key=lambda player: player.points(), reverse=True)
    
    for player in sorted_players:
        print(player)

def main():
    # Ask for the file name and load players
    file_name = input("Enter the file name (e.g., partial.json): ")
    players = load_players(file_name)
    
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
            break
        elif command == "1":
            name = input("Enter player's name: ")
            player = next((p for p in players if p.name.lower() == name.lower()), None)
            if player:
                print(player)
            else:
                print("Player not found.")
        elif command == "2":
            teams = sorted(set(player.team for player in players))
            print("Teams:", " ".join(teams))
        elif command == "3":
            countries = sorted(set(player.nationality for player in players))
            print("Countries:", " ".join(countries))
        elif command == "4":
            team = input("Enter team abbreviation: ").upper()
            list_players_in_team(players, team)
        elif command == "5":
            country = input("Enter country abbreviation: ").upper()
            list_players_from_country(players, country)
        elif command == "6":
            # List player with most points
            best_player = max(players, key=lambda player: player.points())
            print(best_player)
        elif command == "7":
            # List player with most goals
            best_goals = max(players, key=lambda player: player.goals)
            print(best_goals)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
