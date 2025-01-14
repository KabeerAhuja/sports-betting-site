from flask import Flask, jsonify, request
import requests

# Flask app
app = Flask(__name__)
app.secret_key = "sports-betting-news-secret-key"

# The Odds API details
API_KEY = 'your_api_key_here'  # Replace with your API key
SPORTS_API_URL = "https://api.the-odds-api.com/v4/sports"

# Initial popularity (reversed predefined popularity)
POPULARITY_RANKING = {
    "americanfootball_nfl": 1,
    "basketball_nba": 2,
    "baseball_mlb": 3,
    "soccer_epl": 4,
    "hockey_nhl": 5,
    "tennis_atp": 6,
    "mma_ufc": 7
}

# Reverse the numbers for default order
for sport in POPULARITY_RANKING:
    POPULARITY_RANKING[sport] = len(POPULARITY_RANKING) - POPULARITY_RANKING[sport] + 1

# Popularity counts (to track clicks)
popularity_counts = {sport: POPULARITY_RANKING[sport] for sport in POPULARITY_RANKING}

# Cached sports data
cached_sports = None

def fetch_sports_data():
    """
    Fetch sports data from the Odds API and cache it.
    """
    global cached_sports
    if cached_sports is None:
        try:
            response = requests.get(SPORTS_API_URL, params={"apiKey": API_KEY})
            response.raise_for_status()
            cached_sports = response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching sports data: {e}")
            cached_sports = []
    return cached_sports

@app.route('/menu', methods=['GET'])
def get_sports_menu():
    """
    Get sports in season, sorted by popularity.
    """
    global popularity_counts

    # Fetch sports data
    sports_data = fetch_sports_data()

    # Filter sports in season
    sports_in_season = [sport['key'] for sport in sports_data if sport.get('active')]

    # Sort sports by popularity
    sorted_sports = sorted(
        sports_in_season,
        key=lambda sport: popularity_counts.get(sport, float('inf')),
        reverse=True
    )

    return jsonify(sorted_sports)

@app.route('/increase_popularity', methods=['POST'])
def increase_popularity():
    """
    Increase the popularity of a selected sport.
    """
    global popularity_counts
    sport = request.json.get('sport')

    if sport in popularity_counts:
        popularity_counts[sport] += 1
        return jsonify({"success": True, "message": f"Popularity for {sport} increased."})
    else:
        return jsonify({"success": False, "message": "Sport not found."}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
