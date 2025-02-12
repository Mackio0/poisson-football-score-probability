import pandas as pd

def process_data(data):
    """
    Convert raw JSON data to a Pandas DataFrame.
    Expects the JSON data to contain a key 'matches' with a list of match dictionaries.
    """
    if data is None or 'matches' not in data:
        print("No match data found!")
        return pd.DataFrame()
    
    matches = data['matches']
    df = pd.DataFrame(matches)
    return df

def compute_team_stats(df):
    team_stats = {}
    for index, row in df.iterrows():
        home_team = row['homeTeam']['name']
        away_team = row['awayTeam']['name']
        
        # Access score values from fullTime and ensure they're numbers (default to 0 if None)
        score = row.get('score', {}).get('fullTime', {})
        home_goals = score.get('home') or 0  # if None, defaults to 0
        away_goals = score.get('away') or 0  # if None, defaults to 0
        
        # Update stats for the home team
        if home_team not in team_stats:
            team_stats[home_team] = {'scored': 0, 'conceded': 0, 'matches': 0}
        team_stats[home_team]['scored'] += home_goals
        team_stats[home_team]['conceded'] += away_goals
        team_stats[home_team]['matches'] += 1
        
        # Update stats for the away team
        if away_team not in team_stats:
            team_stats[away_team] = {'scored': 0, 'conceded': 0, 'matches': 0}
        team_stats[away_team]['scored'] += away_goals
        team_stats[away_team]['conceded'] += home_goals
        team_stats[away_team]['matches'] += 1

    # Compute averages for each team
    for team, stats in team_stats.items():
        if stats['matches'] > 0:
            stats['avg_scored'] = stats['scored'] / stats['matches']
            stats['avg_conceded'] = stats['conceded'] / stats['matches']
        else:
            stats['avg_scored'] = 0
            stats['avg_conceded'] = 0

    return team_stats
