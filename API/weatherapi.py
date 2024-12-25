from flask import Flask, jsonify, request, render_template
import requests


app = Flask(__name__)


API_KEY = "ae19afeb6770e1d1e79a2df7283e8d02"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')

    if not city:
        return jsonify({"error": "Please provide a city name!"}), 400


    url = f"{BASE_URL}?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"],
            "wind_speed": data["wind"]["speed"]
        }
        return jsonify(weather)
    else:
        return jsonify({"error": "City not found or API request failed"}), 404


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
