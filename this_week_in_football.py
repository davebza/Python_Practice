import random
from operator import itemgetter

#Class definitions:

class Team:
    #define the initialization:
    #each team will be given a name from a list of names
    #and passed two random numbers describing attack and defense skill
    #they will also have variable slots for season performance, which will be updated during the games
    def __init__(self, name, attack, defense):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.home_wins = 0
        self.home_losses = 0
        self.away_wins = 0
        self.away_losses = 0
        self.home_draws = 0
        self.away_draws = 0
        self.games_played = 0

# Function definitions:

def match(team1, team2):
    #make a goals list, and then populate it with the returns of the play_half function
    goals = []
    first = play_half(team1, team2)
    second = play_half(team1, team2)
    #each teams goals are added to the list:
    goals_team1 = first[0] + second[0]
    goals_team2 = first[1] + second[1]
    goals.append(goals_team1)
    goals.append(goals_team2)

    #Output the fixture and the result:
    print("{0} (at home) plays {1}.".format(team1.name, team2.name))
    team1.games_played += 1
    team2.games_played += 1
    print("{0}: {1}".format(team1.name, goals[0]))
    print("{0}: {1}".format(team2.name, goals[1]))
    if goals[0] > goals[1]:
        team1.home_wins += 1
        team2.away_losses += 1
        print(team1.name + " wins!")
    elif goals[0] < goals[1]:
        team1.home_losses += 1
        team2.away_wins += 1
        print(team1.name + " loses.")
    else:
        team1.home_draws += 1
        team2.away_draws += 1
        print("Game drawn.")

def play_half(team1, team2):
    # this function simulates a half of a football game.
    #team attack and defence are used, but there is some room for random performance:
    team1_attack_performance = team1.attack * random.randint(1, 10)
    team1_defense_performance = team1.defense * random.randint(1, 10)
    team2_attack_performance = team2.attack * random.randint(1, 10)
    team2_defense_performance = team2.defense * random.randint(1, 10)

    #init a list for the goals of that half. this will be returned:
    half_goals = []

    #below is the scoring algorithm. It's very naive, and at the moment only 2 goals can be scored by each team per half:
    if team1_attack_performance / team2_defense_performance > 1:
        team1_goals = 1
    else:
        team1_goals = 0
    if team2_attack_performance / team1_defense_performance > 1:
        team2_goals = 1
    else:
        team2_goals = 0
    half_goals.append(team1_goals)
    half_goals.append(team2_goals)
    return half_goals


def season_performance(team):
    #This function generates the points for the team based on their performance in the league thus far
    total_points = (team.away_wins * 3) + (team.home_wins * 2) + team.home_draws + team.away_draws

    return total_points

#----------------------------------*** Main Program ***-----------------------------------------------#
team_list = ["Liverpool", "Spurs", "Manchester United", "West Ham", "Arsenal", "Sunderland", "Newcastle",
             "West Bromwich Albion", "Manchester City", "Leeds", "Brighton"]

# randomize the list to make each season's matches play out differently
random.shuffle(team_list)
# calculate the length of the season: 1 home and 1 away match per team. This could be extended with a top X teams knockout phase, and a final
season_length = (len(team_list) - 1) * 2

# Start the season:
week_number = 1
# Initalise a list of all the teams in the season:
team_stable = []
# Initialise lists of the results:
results_table = []
weekly_results = []
i = 1

# Create the teams by calling the Class: Team method, giving each team a number i.e. team1{Man U, Attack, Defence etc} and then append them to the team stable:
for team in team_list:
    team_init = "team" + str(i)
    team_init = Team(team, random.randint(1, 100), random.randint(1, 100))
    team_stable.append(team_init)
    i += 1

# start the matches for each week
while week_number <= season_length:

    print("Week {}:".format(week_number))
    i = 0

    while i <= len(team_stable) - 2:
        home_team = team_stable[i]
        away_team = team_stable[i + 1]
        match(home_team, away_team)
        i += 2
    print("Standings at the end of week {}:".format(week_number))


    #This code below moves the first item in the team stable to the end. That makes each week different!
    mover = team_stable.pop(0)
    team_stable.append(mover)

    # Begin the report generation:
    for team in team_stable:
        #calculate the season performance for the team
        season_end = season_performance(team)
        #intialize a list for the team's data to be collated into
        current_list = []
        #append the data from:
        current_list.append(team.name)
        current_list.append(team.home_wins)
        current_list.append(team.home_losses)
        current_list.append(team.home_draws)
        current_list.append(team.away_wins)
        current_list.append(team.away_losses)
        current_list.append(team.away_draws)
        current_list.append(season_end)
        current_list.append(team.games_played)
        # now insert htis list into the results_table list
        results_table.append(current_list)
    # Sort the results table once all the week's data is put in:
    results_table = sorted(results_table, key=itemgetter(7, 4, 1, 2, 5, 3, 6))
    # reverse the sorted table, as itemgetter does ascending sorts
    results_table = results_table[::-1]

    #outputting the data:
    for row in results_table:
        # Generate a string value of the list data:
        output_row = []
        for item in row:
            item = str(item)
            output_row.append(item)
        output_string = " ".join(output_row)
        print(output_string)
    #Append this string into the weekly results list:
    weekly_results.append(results_table)
    results_table = []

    # Make the weekly reports
    the_reported_week = 1
    if week_number == season_length:
        for week in weekly_results:
            print("Week {} results:".format(the_reported_week))
            #this print statement below prints out the values you have been using to do your matplotlib graphs:
            #print(week)
            for item in week:
                print(item)
            the_reported_week += 1
        break
    else:
        week_number += 1
