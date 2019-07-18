from flask import Flask, request, send_from_directory
import weather
<<<<<<< HEAD

app = Flask(__name__)
=======
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app, resources={r"localhost:8080/weather/*": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
>>>>>>> ba9cd076a53da5826f342d339e27866e20899036



@app.route('/weather/<city>', methods=['GET','POST'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def get_weather(city):
    data = weather.get_weather(city)
    data.headers.add('Access-Control-Allow-Origin', '*')
    x = str((data['main']['temp'], data['main']['humidity'], data['weather'][0]['description']))
    return x


@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    return response


if __name__ == "__main__":
    app.run(debug=True, host='localhost', port=8080)
