import requests
import os
from dotenv import load_dotenv
load_dotenv()

API_KEY = os.getenv('API_KEY')
API_URL = 'https://api.football-data.org/v4/competitions/CL/matches'

def fetch_match_data():
    headers = {'X-Auth-Token': API_KEY}
    response = requests.get(API_URL, headers=headers)
    if response.status_code == 200:
        data = response.json()
        print("Data fetched successfully!")
        return data
    else:
        print("Failed to fetch data. Status code:", response.status_code)
        return None

if __name__ == "__main__":
    # For testing the module directly
    fetch_match_data()
