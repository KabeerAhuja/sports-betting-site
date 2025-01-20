import requests

API_KEY = "2946c26b4a6a0c1edbb12873847b9d45"
BASE_URL = "https://api.sportsgameodds.com/"

def get_sports_in_season():
    """
    Fetches a list of sports currently in season from the Sportsgameodds API.
    """
    endpoint = f"{BASE_URL}sports"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }
    
    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response
        
        # Extract sports currently in season (modify this based on API structure)
        sports_in_season = [sport['name'] for sport in data.get('sports', []) if sport.get('in_season', False)]
        return sports_in_season

    except requests.exceptions.RequestException as e:
        print(f"Error fetching sports in season: {e}")
        return []

def get_all_sports():
    """
    Fetches a list of all sports from the Sportsgameodds API.
    """
    endpoint = f"{BASE_URL}sports"
    headers = {
        "Authorization": f"Bearer {API_KEY}"
    }

    try:
        response = requests.get(endpoint, headers=headers)
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse JSON response
        
        # Extract all sports (modify this based on API structure)
        all_sports = [sport['name'] for sport in data.get('sports', [])]
        return all_sports

    except requests.exceptions.RequestException as e:
        print(f"Error fetching all sports: {e}")
        return []
