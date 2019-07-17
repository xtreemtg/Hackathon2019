from flask import Flask, request, send_from_directory
import weather
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

@app.route('/weather/<city>')
def get_weather(city):
    data = weather.get_weather(city)
    x = str((data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
    return x

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
