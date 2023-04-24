import requests
import smtplib


MY_EMAIL = "ritiksuniljain@gmail.com"
PASSWORD = "fjiqjihbqojanzbq"
RECEVIVER_EMAIL = "ritikjain7350@gmail.com"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
# api_key = "6c9a1479c0c60e5bd702eb58f696ccbd"
api_key = "69f04e4613056b159c2761a9d9e664d2"

weather_params = {
    "lat" : 18.5196,
    "lon" : 73.8553,
    "appid" : api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()


will_rain = False

for i in range(13):
    if weather_data['hourly'][i]['weather'][0]['id'] < 700:
        will_rain = True
        break
#         for _ in range enum(list)

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= MY_EMAIL, password= PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,
                            to_addrs= RECEVIVER_EMAIL,
                            msg=f"Subject:Rain Alert\n\nRemember To Take An UMBRELLA Today !!!")
        connection.close()