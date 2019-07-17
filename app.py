from flask import Flask, request, jsonify

import weather

app = Flask(__name__)



@app.route('/weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    data = weather.get_weather(city)
    return data


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
