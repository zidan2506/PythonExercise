import requests

request = "https://api.chucknorris.io/jokes/random"
try:
    response =  requests.get(request)
    if response.status_code == 200:
        json_res = response.json()
        print(f"Joke of the day: {json_res['value']}")

except requests.exceptions.RequestException as e:
    print("Request could not be completed")
    print(e.args)
