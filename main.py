import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("enter the city name : \n")

url = f" https://api.openweathermap.org/data/2.5/weather?q={city}&appid=27076b876ea6a6ea93820806673bdbc7"

m = requests.get(url)
# print(m.text)

weather = json.loads(m.text)
r = weather["main"]["temp"]
temp = round(r - 273.15)
speak.speak(f"the temperture of {city} is {temp} degree celsius")

