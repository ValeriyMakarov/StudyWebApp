import requests as requests
from flask import Flask, request, render_template

app = Flask(__name__)

# Главная страница с формой для ввода города
@app.route('/')
def home():
    return render_template('index.html')

# Обработка формы и получение данных о погоде
@app.route('/weather', methods=['POST'])
def weather():
    city = request.form['city']
    geo_url = f'https://geocoding-api.open-meteo.com/v1/search?name={city}&count=10&language=en&format=json'

    response = requests.get(geo_url)
    data = response.json()
    print(data['results'][0])
    data = data['results'][0]
    weather_url = f'https://api.open-meteo.com/v1/forecast?latitude=' \
                  f'{data["latitude"]}&longitude={data["longitude"]}&hourly=temperature_2m'
    response = requests.get(weather_url)
    data = response.json()
    print(data)
    # if not data:
    #     print(data)
    #     return render_template('index.html', error='City not found')
    # else:
    #     print('\n\n\n'+str(data[0])+'\n\n\n\n')
    #     data = data[0]
    #     geo_data = {
    #         "city": data['name'],
    #         "lat": data['lat'],
    #         "lon": data['lon'],
    #         "country": data['country'],
    #         "state": data['state']
    #     }
    #     api_key = '5ef4f0e87d344ee399e54c5e27afd7f0'
    #     base_url = 'https://api.openweathermap.org/data/3.0/onecall?'
    #     # complete_url = f"http://api.openweathermap.org/data/2.5/find?q=Petersburg&type=like&appid={api_key}"
    #     complete_url = f"{base_url}lat={51.5073219}&lon={-0.1276474}&appid={api_key}"
    #
    #     response = requests.get(complete_url)
    #     data = response.json()
    #     print(data)
    #     weather_data = {
    #         'city': geo_data['city'],
    #         'timezone': data['timezone'],
    #         'current': data['current']
    #     }
        # return render_template('result.html', weather=weather_data)
    return 'f'

if __name__ == '__main__':
    app.run(debug=True)
