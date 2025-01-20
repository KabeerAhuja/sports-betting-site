from flask import Flask, render_template, jsonify, request
from get_sports import get_sports_in_season, get_all_sports

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('menu.html')

@app.route('/menu', methods=['GET'])
def fetch_sports_menu():
    sports_in_season = get_sports_in_season()
    return jsonify(sports_in_season)

@app.route('/increase_popularity', methods=['POST'])
def increase_popularity():
    data = request.get_json()
    sport = data.get('sport')
    if sport:
        # Simulate popularity update (replace this with database logic if needed)
        return jsonify({'success': True, 'message': f'Popularity for {sport} increased!'})
    else:
        return jsonify({'success': False, 'message': 'Sport not provided!'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
