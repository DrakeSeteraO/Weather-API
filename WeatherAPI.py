import requests

API_Key = None
Zipcode = None

url = "http://api.weatherapi.com/v1/current.json?key=" + API_Key +"&q=" + Zipcode + "&aqi=no"

response = requests.get(url)
json = response.json()
temperature = json["current"]["temp_f"]
print(temperature)