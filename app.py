from flask import Flask, request, send_from_directory
import weather

app = Flask(__name__)

@app.route('/weather/<city>')
def get_weather(city):
    data = weather.get_weather(city)
    x = str((data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
    return x


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
