import tkinter as tk
from pip._vendor import requests
import time

def getWeather(screen):
    
    city = e1.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=7a0472896a9fbae4a2c627a4a5f34b13"
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp']-273.15)
    min_temp = int(json_data['main']['temp_min']-273.15)
    max_temp = int(json_data['main']['temp_max']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunrise']-216000))
    sunset = time.strftime("%I:%M:%S",time.gmtime(json_data['sys']['sunset']-216000))
    
    final_info = condition + "\n" + str(temp) + "°C"
    final_data = "\n" + "Max Temp : " + str(max_temp) + "\n" + "Min Temp : " + str(min_temp) + "\n" + "Pressure : " + str(pressure) + "\n" + "Humidity : " + str(humidity) + "\n" + "Wind Speed : " + str(wind) + "\n" + "Sunrise : " + sunrise + "\n" + "Sunset : " + sunset
                 
    label1.config(text=final_info)
    label2.config(text=final_data)
    
screen = tk.Tk()
screen.geometry("600x500")
screen.title("Weather App")

f=("poppins",15,"bold")
t=("poppins",35,"bold")

e1 = tk.Entry(screen, justify='center', font=f)
e1.pack(pady=30)
e1.focus()
e1.bind('<Return>',getWeather)

label1 = tk.Label(screen, font=t)
label1.pack()
label2 = tk.Label(screen, font=f)
label2.pack()

screen.mainloop()