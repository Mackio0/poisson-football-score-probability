import matplotlib
matplotlib.use('TkAgg')
# I had the error of visualizations not showing up, so i changed the backend to Tkinter
import matplotlib.pyplot as plt
from data_fetcher import fetch_match_data
from data_processing import process_data, compute_team_stats
from poisson_model import calculate_score_probabilities, outcome_probabilities
from visualizations import plot_goal_distribution, plot_score_matrix_heatmap

def main():
    # Step 1: Fetch match data from the API
    data = fetch_match_data()
    if data is None:
        print("No data fetched. Exiting.")
        return

    # Step 2: Process the raw JSON into a DataFrame
    df = process_data(data)
    if df.empty:
        print("The DataFrame is empty. Exiting.")
        return

    # Step 3: Compute team statistics
    team_stats = compute_team_stats(df)
    
    
    # Convert team_stats keys into a list and print with index numbers
    teams = list(team_stats.keys())
    print("Team Stats:")
    for idx, team in enumerate(teams):
        stats = team_stats[team]
        print(f"{idx}: {team}: Avg Scored: {stats.get('avg_scored', 0):.2f}, Avg Conceded: {stats.get('avg_conceded', 0):.2f}")
    
    # Prompt the user to select teams by their index number
    try:
        home_index = int(input("Select the index for the HOME team: "))
        away_index = int(input("Select the index for the AWAY team: "))
    except ValueError:
        print("Invalid input! Please enter a valid integer.")
        return

    # Validate the indices
    if home_index < 0 or home_index >= len(teams) or away_index < 0 or away_index >= len(teams):
        print("Invalid index selection!")
        return

    home_team = teams[home_index]
    away_team = teams[away_index]
    home_lambda = team_stats[home_team]['avg_scored']
    away_lambda = team_stats[away_team]['avg_scored']
    
    print(f"\nSelected teams for modeling:")
    print(f"Home - {home_team} (λ={home_lambda:.2f})")
    print(f"Away - {away_team} (λ={away_lambda:.2f})")

    # Step 4: Calculate score probabilities using the Poisson model
    max_goals = 5
    score_matrix = calculate_score_probabilities(home_lambda, away_lambda, max_goals=max_goals)
    home_win, draw, away_win = outcome_probabilities(score_matrix)
    print("\nMatch Outcome Probabilities:")
    print("Home Win: {:.2%}".format(home_win))
    print("Draw: {:.2%}".format(draw))
    print("Away Win: {:.2%}".format(away_win))


    # Step 5: Visualizations
    plot_goal_distribution(home_lambda, away_lambda, max_goals=max_goals)
    plot_score_matrix_heatmap(score_matrix, max_goals=max_goals)

if __name__ == "__main__":
    main()
