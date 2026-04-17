import requests
from twilio.rest import Client
import os
params = {
    "appid": "7bba75b3218b1cc2b55bcfcd03b1207c",
    # "q": "Brooklyn,NY,US",
    "units": "imperial",
    "lon":-73.990997,
    "lat": 40.692532,
    "cnt": 6  # This is 18 hours every on is 3 hours

}

response = requests.get(url="https://api.openweathermap.org/data/2.5/forecast", params=params)

data = response.json()

def is_it_going_to_rain():
    """this will tell return True of False if it is going to rain in the next 18 hours """
    all_id =[ raining_id["weather"][0]["id"] for raining_id in data["list"]]
    for rain_id in all_id:
        if rain_id > 700:
            return True
        else:
            return False
def send_whatsapp(message):
    """This will send a message from my Twilo WhatsApp number
    Note :you need to have from twilio.rest import Client installed in order this to work"""
    aut_token = os.environ.get("TWILIO_AUTH_TOKEN")
    account_sid = os.environ.get("AMOUNT_SID")

    client = Client(account_sid, aut_token)

    message = client.messages.create(
        body=message,
        from_="whatsapp:+14155238886",
        to="whatsapp:+19292490738",
    )
    print(f"Message Status: {message.status}")
    print(f"Message SID: {message.sid}")



if is_it_going_to_rain():
    send_whatsapp("It's going to rain in the next 18 hours! 🌧️ Don't forget to take an umbrella to Yeshiva today. Have a great day!")
elif not is_it_going_to_rain() :
    send_whatsapp("Have a great day! The skies look clear today. ☀️")

