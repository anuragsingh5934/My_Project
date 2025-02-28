import requests
api_key = 'd4e0ec74d35c458694d541e9c21154eb'

print("\n\tWelcome to Weather Report App\n")
user_input = input("Please Enter Your City Name :\n")


weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)
info = dict(weather_data.json())


print(f"Here is a data we found about your {user_input.upper()} city\n\
    \nTemprature of {user_input.upper()} is {info["main"]["temp"]}° Fahrenheit.\n\
    Feels like {info['main']['feels_like']}° Fahrenheit.")


fahrenheit = info["main"]["temp"]
feel_fahrenheit = info['main']['feels_like']

celsious = int((fahrenheit - 32) * 5/9)
feel_cel = int((feel_fahrenheit - 32) * 5/9)


converter = input("\nWant to Convert in celsius ? (y/n) ")
if converter.lower() == "y":

    print(f"""Here is a data we found about your "{user_input.upper()}" city\n\
    \nTemprature of {user_input.upper()} is {celsious}° Celsious\n\
            Feels like {feel_cel}° Celsious""")

    if feel_cel <= 10:
        print(f"\nIts Cold, Wear Warm cloths.")

    elif feel_cel < 25:
        print(f"\nThe weather is pleasant today.")
    
    elif feel_cel < 35:
        print(f"\nWeather is warm use sunscreen when you step out")
    
    elif feel_cel < 45:
        print("\nToo hot outside, Use AC and Drink water.")
    
    elif feel_cel > 45:
        print("\nOut door Condition is wrost, dont step outside otherwise you will suffer.")
    print("\nThank You")

elif converter.lower() == "n":

    if feel_cel <= 10:
        print(f"Its Cold, Wear Warm cloths.")

    elif feel_cel < 25:
        print(f"The weather is pleasant today.")
    
    elif feel_cel < 35:
        print(f"Weather is warm use sunscreen when you step out")
    
    elif feel_cel < 45:
        print("Too hot outside, Use AC and Drink water.")
    
    elif feel_cel > 45:
        print("Out door Condition is wrost, dont step outside otherwise you will suffer.")
    print("Thank you!")
else:
    print("Please Enter correct value.")