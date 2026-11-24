import os
import random

class Player:
    def __init__(self, name, position, projected_points):
        self.name = name
        self.position = position
        self.projected_points = projected_points

player_pool = [
    Player("Joel Embiid", "C", 56),
    Player("Nikola Jokic", "C", 60),
    Player("Giannis Antetokounmpo", "PF", 56),
    Player("Luka Doncic", "PG", 55),
    Player("LeBron James", "SF", 52),
    Player("Shai Gilgeous-Alexander", "PG", 50),
    Player("Kevin Durant", "PF", 48),
    Player("Stephen Curry", "PG", 47),
    Player("Anthony Davis", "C", 50),
    Player("Devin Booker", "SG", 48),
    Player("Jayson Tatum", "SF", 53),
    Player("Ja Morant", "PG", 45),
    Player("Donovan Mitchell", "SG", 44),
    Player("Jimmy Butler", "SF", 46),
    Player("Kawhi Leonard", "SF", 46),
    Player("Jalen Brunson", "PG", 43),
    Player("Tyrese Haliburton", "PG", 47),
    Player("Anthony Edwards", "SG", 46),
    Player("Kyrie Irving", "SG", 47),
    Player("Domantas Sabonis", "C", 46),
    Player("Paul George", "SG", 41),
    Player("Jaylen Brown", "SG", 41),
    Player("Damian Lillard", "PG", 48),
    Player("Victor Wembanyama", "C", 41),
    Player("Zion Williamson", "PF", 50),
    Player("De’Aaron Fox", "PG", 43),
    Player("Trae Young", "PG", 45),
    Player("LaMelo Ball", "PG", 47),
    Player("Tyrese Maxey", "SG", 38),
    Player("Bam Adebayo", "C", 42),
    Player("Karl-Anthony Towns", "PF", 42),
    Player("Kristaps Porzingis", "PF", 42),
    Player("Jamal Murray", "PG", 39),
    Player("Chet Holmgren", "C", 35),
    Player("Evan Mobley", "PF", 36),
    Player("Paolo Banchero", "PF", 41),
    Player("DeMar DeRozan", "PF", 42),
    Player("Pascal Siakam", "PF", 43),
    Player("Brandon Ingram", "SF", 42),
    Player("Jaren Jackson Jr.", "PF", 43),
    Player("Dejounte Murray", "SG", 43),
    Player("James Harden", "PG", 45),
    Player("Bradley Beal", "SG", 34),
    Player("Alperen Sengun", "C", 37),
    Player("Khris Middleton", "SF", 37),
    Player("Lauri Markkanen", "SF", 44),
    Player("Julius Randle", "PF", 40),
    Player("Jrue Holiday", "PG", 37),
    Player("Derrick White", "SG", 29),
    Player("Jarrett Allen", "C", 37),
    Player("Scottie Barnes", "SF", 37),
    Player("Cade Cunningham", "PG", 39),
    Player("Jalen Green", "SG", 34),
    Player("Rudy Gobert", "C", 32),
    Player("C.J. McCollum", "PG", 38),
    Player("Desmond Bane", "SG", 38),
    Player("Fred VanVleet", "PG", 37),
    Player("Jalen Williams", "SF", 35),
    Player("Deandre Ayton", "C", 32),
    Player("Tyler Herro", "SG", 35),
    Player("Darius Garland", "PG", 40),
    Player("Mikal Bridges", "SG", 43),
    Player("Franz Wagner", "SF", 33),
    Player("Michael Porter Jr.", "SF", 32),
    Player("Collin Sexton", "PG", 31),
    Player("Aaron Gordon", "PF", 30),
    Player("Draymond Green", "PF", 31),
    Player("Zach LaVine", "SF", 39),
    Player("Nicolas Claxton", "C", 32),
    Player("D’Angelo Russell", "PG", 36),
    Player("Anfernee Simons", "SG", 32),
    Player("Kyle Kuzma", "SF", 40),
    Player("R.J. Barrett", "SF", 26),
    Player("Jonas Valanciunas", "C", 32),
    Player("Jalen Duren", "C", 26),
    Player("OG Anunoby", "SG", 33),
    Player("Jusuf Nurkic", "C", 33),
    Player("Myles Turner", "C", 37),
    Player("Chris Paul", "PG", 35),
    Player("Nikola Vucevic", "C", 40),
    Player("Austin Reaves", "SG", 35),
    Player("Jalen Suggs", "SG", 23),
    Player("Tobias Harris", "SF", 31),
    Player("Jonathan Kuminga", "PF", 22),
    Player("Coby White", "SG", 22),
    Player("Mark Williams", "C", 32),
    Player("Jakob Poeltl", "C", 34),
    Player("Cam Thomas", "SG", 21),
    Player("Mitchell Robinson", "C", 28),
    Player("Bobby Portis", "C", 31),
    Player("Devin Vassell", "SG", 37),
    Player("Jerami Grant", "PF", 32),
    Player("Klay Thompson", "SG", 32),
    Player("Brandon Miller", "SF", 28),
    Player("Amen Thompson", "SG", 26),
    Player("Keegan Murray", "PF", 33),
    Player("Jabari Smith Jr.", "PF", 28),
    Player("Walker Kessler", "C", 35),
    Player("Robert Williams III", "C", 31),
    Player("Clint Capela", "C", 33)
]

print("Welcome to the NBA Fantasy Draft! The objective is to make the greatest team possible by drafting from the current NBA pool.The draft will follow a snake draft format. Each team will be asked to pick a player from the draft pool. You can only select a player who plays the same position after you select your five players who play different positions. ")

while True:
    try:
        num_teams = int(input("How many teams would you like to have (minimum 2, maximum 8)? "))
        if 2 <= num_teams <= 8:
            break
        else:
            print("Please enter a number between 2 and 8.")
    except ValueError:
        print("Please enter a valid number.")

team_names = []
for i in range(1, num_teams + 1):
    team_name = input(f"Enter the name of Team {i}: ")
    team_names.append(team_name)

print("Teams in the Draft:", team_names)

team_players = {team_name: [] for team_name in team_names}

def draft_players(num_teams, team_names, player_pool):
    draft_order = []
    for i in range(1, num_teams + 1):
        if i % 2 == 1:  # Odd round: draft from top to bottom
            draft_order.extend(range(1, num_teams + 1))
        else:
            draft_order.extend(range(num_teams, 0, -1))
    for round_num in range(1, 5):
        os.system('cls')
        print(f"\nRound {round_num}:")
        for team_index in draft_order:
            team_name = team_names[team_index - 1]
            print(f"\n{team_name}'s turn to pick.")
            print("Draft Pool:")
            for player in player_pool:
                print(f"{player.name} | Position: {player.position} | Projected Points: {player.projected_points}")
            while True:
                selected_player_name = input("Enter the name of the player you want to draft or enter 'display' to display the players you drafted: ")
                if selected_player_name.lower() == 'display':
                    print("Your Drafted Players:\n")
                    for player in team_players[team_name]:
                        print(f"{player.name} | Position: {player.position} | Projected Points: {player.projected_points}")
                    continue
                selected_player = next((player for player in player_pool if player.name.lower() == selected_player_name.lower()), None)
                if selected_player is None:
                    print("Invalid player name. Please enter a valid player name.")
                    continue
                if selected_player in team_players[team_name]:
                    print(f"{selected_player_name} has already been drafted by {team_name}. Choose another player.")
                    continue
                if selected_player.position in [player.position for player in team_players[team_name]] and len(team_players[team_name]) < 5:
                    print(f"Sorry, {team_name} already has a player in position {selected_player.position}. Choose another player.")
                else:
                    team_players[team_name].append(selected_player)
                    print(f"{selected_player_name} has been drafted to {team_name}.")
                    player_pool.remove(selected_player)
                    break
   
    print("\nDraft Results:")
    for team_name, players in team_players.items():
        print (f"{team_name}: {[player.name for player in players]}")

draft_players(num_teams, team_names, player_pool)

def simulation(team1, team2, team_players):
    team1_points = {player.name: random.randint(player.projected_points - 10, player.projected_points + 10) for player in team_players[team1]}
    team2_points = {player.name: random.randint(player.projected_points - 10, player.projected_points + 10) for player in team_players[team2]}
    os.system('cls')
    print(f"{team1} Points:")
    for player, points in team1_points.items():
        print(f"{player}: {points}")
    
    print(f"\n{team2} Points:")
    for player, points in team2_points.items():
        print(f"{player}: {points}")
    
    total_team1_points = sum(team1_points.values())
    total_team2_points = sum(team2_points.values())
    
    print(f"\nTotal Points:")
    print(f"\n{team1}: {total_team1_points}")
    print(f"\n{team2}: {total_team2_points}")
    
    if total_team1_points > total_team2_points:
        print(f"\n{team1} wins!")
    elif total_team1_points < total_team2_points:
        print(f"\n{team2} wins!")
    else:
        print("\nIt's a tie!")

play_again = True
while play_again:
    play = input("Press enter to simulate a game between two teams or enter 'break' to end the program: ")
    if play.lower == 'break':
        break
    team1 = input("Enter the name of the first team: ")
    team2 = input("Enter the name of the second team: ")
    if team1 in team_names and team2 in team_names:
        simulation(team1, team2, team_players)
        while True:
            choice = input("Do you want to play again (y/n)?")
            if choice.lower() == "no" or "n":
                play_again = False
                break
            elif choice.lower() == "Yes" or "Y":
                break
            else:
                print("Please enter a valid input")
    else:
        print("Please enter valid team names.")
