import requests
api_key = 'd4e0ec74d35c458694d541e9c21154eb'

print("\n\tWelcome to Weather Report App\n")
user_input = input("Please Enter Your City Name :\n")


weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
info = dict(weather_data.json())

# temp_real =int({info["main"]["temp"]})
print(f"Here is a data we found about your {user_input.upper()} city\n\
      Temprature of {user_input.upper()} is {info["main"]["temp"]}\n\
        feels like {info['main']['feels_like']}")

converter = input("Want to Convert in celsius ? (y/n) ")
if converter.lower() == "y":
    fahrenheit = info["main"]["temp"]
    
    celsious = (fahrenheit - 32) * 5/9
    
    print(f"Here is a data we found about your {user_input.upper()} city\n\
    Temprature of {user_input.upper()} is {int(celsious)}\n\
    Feels like {info['main']['feels_like']}")