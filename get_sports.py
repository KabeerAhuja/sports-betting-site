import requests

# Your Odds API key
API_KEY = 'e1fa961b77802f0da6e79382bba070a7' 

# The Odds API endpoint for sports
SPORTS_API_URL = "https://api.the-odds-api.com/v4/sports"

def get_sports_in_season():
    """
    Fetch and return only the sports currently in season.
    """
    try:
        # Make a GET request to the Odds API to retrieve the list of sports
        response = requests.get(SPORTS_API_URL, params={"apiKey": API_KEY})
        response.raise_for_status()  # Raise an error for HTTP issues

        # Parse the response JSON
        sports_data = response.json()

        # Filter for sports currently in season
        sports_in_season = [sport['key'] for sport in sports_data if sport.get('active')]

        return sports_in_season

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching sports data: {e}")
        return []

# Run the function
if __name__ == "__main__":
    sports_in_season = get_sports_in_season()
    
    print("Sports Currently in Season:")
    for sport in sports_in_season:
        print(f" - {sport}")
