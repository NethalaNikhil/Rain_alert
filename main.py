import requests
from twilio.rest import Client

account_sid = 'ACca64ec53998ee8739da558f5e40b9071'
auth_token = 'ab738c791f3e57b2f591774ced60b4d6'

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/forecast?lat=16.591040&lon=81.520782&cnt=3&appid=21158568bf14e948960257ed3151772c")
j_response = response.json()
# condition = j_response["list"][1]["weather"][0]["id"]
# print(condition)
will_run = False
for i in range(3):
    if j_response["list"][i]["weather"][0]["id"] < 700:
        will_run = True
if will_run:
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="It's going to rain today. remember to bring an Umbrella...",
        from_="+14842763122",
        to="+919505758106"
    )

    print(message.status)
