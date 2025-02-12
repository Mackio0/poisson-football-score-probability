# Football Poisson Model

This project uses a Poisson model to predict football match outcomes based on historical match data fetched from a football API.

 
## Project Structure

  
-  **data_fetcher.py**: Fetches match data from the API.

-  **data_processing.py**: Processes the raw data and computes team statistics.

-  **poisson_model.py**: Implements the Poisson model to compute score probabilities.

-  **visualizations.py**: Generates visualizations for the Poisson distributions and score probability matrix.

-  **main.py**: Main script that ties everything together.

-  **requirements.txt**: Lists all the dependencies.

  

## Setup

  
> **Note:** Beforehand, please get your api key from https://www.football-data.org/client/register and add it to your .env file.

1. Clone the repository.

2. Create and activate a virtual environment.

3. Install the dependencies:

```bash

pip install -r requirements.txt

```

4. Run the main script:

```bash

python3 main.py

```

5. Follow the prompts to select teams and visualize the Poisson distributions and score probability matrix.
