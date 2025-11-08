import requests

r = input('Enter the name of a municipality: ')
cityname = False
while not cityname:
    request = f'https://api.openweathermap.org/data/2.5/weather?q={r}&APPID=3abf1b6e6194cd59053b48a53ecdce2a'
    try:
        
        response = requests.get(request)
        if response.status_code == 200:
            res_json = response.json()
            if  res_json['cod'] == 200:
                k_temp = res_json['main']['temp'] 
                c_temp = k_temp - 273.15
                cityname = True
                print(f'Weather condition: {res_json['weather'][0]['main']}\nCurrent temperature: {c_temp:.1f}°C')
                cityname = True

        else:
            print(f'{response.json()['message']}\nPlease enter the correct city name')
            r = input('Enter the name of a municipality: ')
                
        
        
            
        
    except requests.exceptions.RequestException as e:
        print("Request could not be completed")
        print(e.args)



