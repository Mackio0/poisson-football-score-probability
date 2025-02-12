import numpy as np
from scipy.stats import poisson

def calculate_score_probabilities(home_lambda, away_lambda, max_goals=5):
    """
    Calculate the score probability matrix using the Poisson distribution.
    
    Parameters:
      - home_lambda: Expected goals for the home team.
      - away_lambda: Expected goals for the away team.
      - max_goals: Maximum number of goals to consider for each team.
    
    Returns:
      A dictionary where keys are (home_goals, away_goals) tuples and values are probabilities.
    """
    score_matrix = {}
    for home_goals in range(0, max_goals + 1):
        for away_goals in range(0, max_goals + 1):
            prob_home = poisson.pmf(home_goals, home_lambda)
            prob_away = poisson.pmf(away_goals, away_lambda)
            score_matrix[(home_goals, away_goals)] = prob_home * prob_away
    return score_matrix

def outcome_probabilities(score_matrix):
    """
    Calculate overall match outcome probabilities (home win, draw, away win)
    from the score probability matrix.
    
    Returns:
      A tuple: (home_win_probability, draw_probability, away_win_probability)
    """
    home_win = sum(prob for (h, a), prob in score_matrix.items() if h > a)
    draw = sum(prob for (h, a), prob in score_matrix.items() if h == a)
    away_win = sum(prob for (h, a), prob in score_matrix.items() if h < a)
    return home_win, draw, away_win

if __name__ == "__main__":
    # Example usage with sample lambda values
    home_lambda = 1.7
    away_lambda = 1.2
    score_matrix = calculate_score_probabilities(home_lambda, away_lambda, max_goals=5)
    home_win, draw, away_win = outcome_probabilities(score_matrix)
    print("Home win probability: {:.2%}".format(home_win))
    print("Draw probability: {:.2%}".format(draw))
    print("Away win probability: {:.2%}".format(away_win))
