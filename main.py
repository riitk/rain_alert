import requests
import smtplib


MY_EMAIL = "SENDER_EMAIL"               #Add Sender's/Your's Email Address
PASSWORD = "SENDER_PASSWORD"            #Add Sender's/Your's Password
RECEVIVER_EMAIL = "RECEVIVER_EMAIL"

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "XXXXXX"                      #Your openweathermap's API KEY           

weather_params = {
    "lat" : 18.5196,                    #Latitude
    "lon" : 73.8553,                    #Longitude
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
