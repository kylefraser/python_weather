from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/temperature', methods=['POST'])
def temperature():
    zipcode = request.form['zip']
    r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip='+zipcode+',us&appid=ff98cd3153f41d44ddff8b2e6762f63d')
    json_object = r.json()
    status = str(json_object["weather"][0]["main"])
    wind = float(json_object['wind']['speed'])
    temp_k = float(json_object['main']['temp'])
    temp_f = (temp_k - 273.15) * 1.8 + 32
    return render_template('temperature.html', status=status, temp=temp_f, wind=wind)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
