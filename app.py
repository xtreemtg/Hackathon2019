from flask import Flask, request, send_from_directory
import weather
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"localhost:8080/weather/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'



@app.route('/weather/<city>', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_weather(city):
    data = weather.get_weather(city)
    data.headers.add('Access-Control-Allow-Origin', '*')
    x = str((data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
    return x

if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
