import requests

r = input('Enter the name of a municipality: ')
request = 'http://api.weatherapi.com/v1/current.json?key=2ce58d6386004c7d872210654250611&q=' + r
try:
    response = requests.get(request)
    if response.status_code == 200:
        res_json = response.json()
        k_temp = (res_json['current']['temp_f'] - 32)*(5/9)+273.1
        c_temp = k_temp - 273.15

        print(f'Weather condition: {res_json['current']['condition']['text']}\nCurrent temperature: {c_temp:.1f}°C')

except requests.exceptions.RequestException as e:
    print("Request could not be completed")
    print(e.args)