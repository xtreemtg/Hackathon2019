from flask import Flask
import weather

app = Flask(__name__)


@app.route('/weather/<city>')
def get_weather(city):
    data = weather.get_weather(city)
    return str((data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)
