import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy.stats import poisson

def plot_goal_distribution(home_lambda, away_lambda, max_goals=5, save_file=False):
    """
    Plot the Poisson distribution for the number of goals for both teams.
    If save_file is True, the plot is saved as 'goal_distribution.png'; 
    otherwise, it is displayed interactively.
    """
    goal_counts = np.arange(0, max_goals + 1)
    home_probs = poisson.pmf(goal_counts, home_lambda)
    away_probs = poisson.pmf(goal_counts, away_lambda)

    plt.figure(figsize=(8, 6))
    # Offset bars so they don’t overlap
    plt.bar(goal_counts - 0.15, home_probs, width=0.3, alpha=0.7, label='Home Team')
    plt.bar(goal_counts + 0.15, away_probs, width=0.3, alpha=0.7, label='Away Team')
    plt.xlabel('Number of Goals')
    plt.ylabel('Probability')
    plt.title('Poisson Distribution of Goals')
    plt.legend()
    
    if save_file:
        plt.savefig("goal_distribution.png")
        plt.close()
    else:
        plt.show()

def plot_score_matrix_heatmap(score_matrix, max_goals=5, save_file=False):
    """
    Plot a heatmap of the score probability matrix.
    If save_file is True, the plot is saved as 'score_matrix_heatmap.png';
    otherwise, it is displayed interactively.
    """
    # Create a 2D array from the score_matrix dictionary
    heatmap_data = np.zeros((max_goals + 1, max_goals + 1))
    for h in range(0, max_goals + 1):
        for a in range(0, max_goals + 1):
            heatmap_data[h, a] = score_matrix.get((h, a), 0)
    
    plt.figure(figsize=(8, 6))
    sns.heatmap(heatmap_data, annot=True, fmt=".3f", cmap="YlGnBu", 
                xticklabels=range(0, max_goals + 1), yticklabels=range(0, max_goals + 1))
    plt.xlabel('Away Goals')
    plt.ylabel('Home Goals')
    plt.title('Score Probability Matrix')
    
    if save_file:
        plt.savefig("score_matrix_heatmap.png")
        plt.close()
    else:
        plt.show()

if __name__ == "__main__":
    # Example usage with sample lambda values.
    home_lambda = 1.7
    away_lambda = 1.2
    # Set save_file=True if you want to save the figures instead of displaying them
    plot_goal_distribution(home_lambda, away_lambda, max_goals=5, save_file=True)
    
    from poisson_model import calculate_score_probabilities
    score_matrix = calculate_score_probabilities(home_lambda, away_lambda, max_goals=5)
    plot_score_matrix_heatmap(score_matrix, max_goals=5, save_file=True)
