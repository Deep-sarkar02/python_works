# weather prediction app using pyhton and api
# imprt the required librarys:
import json
import requests
import win32com.client
speaker = win32com.client.Dispatch("SAPI.spVoice")
# user input city name
city = input("Enter the name of the city:-")
# passing city name to the url to fetch the data:-
url = f"https://api.weatherapi.com/v1/current.json?key=713f21ca34f04c57bab190049240703&q={city}"
# get data using the request.get method
data=requests.get(url)
# using json module form a dictionary of the data fetched:
data_dict=json.loads(data.text)
# store the required details want to print and display
temp_c = (data_dict["current"]["temp_c"])
date_time=(data_dict["current"]["last_updated"])
feels_like=(data_dict["current"]["feelslike_c"])
# display the output
p_d=(f"Temprature of {city} at {date_time} hours is {temp_c} degrees and its feels like {feels_like} degrees")
print(p_d)

# python text to speech
speaker.Speak(p_d)

