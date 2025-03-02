import requests
api_key = 'd4e0ec74d35c458694d541e9c21154eb'

def f_display(f_temp, f_feel, city, unit='Fahrenheit'):
    """ Display text """

    print(f"""\nHere is a data we found about your "{city.upper()}" city\n\
    \nTemprature of {city} is {f_temp}° {unit}\n\
        Feels like {f_feel}° {unit}. """) #Celsious Fahrenheit
    

    if unit == 'Celsious':
        if f_feel <= 10:
            print(f"\n'Its Cold, Wear Warm cloths.'")

        elif f_feel < 25:
            print(f"\n'The weather is pleasant today.'")
    
        elif f_feel < 35:
            print(f"\n'Weather is warm use sunscreen when you step out'")
    
        elif f_feel < 45:
            print("\n'Too hot outside, Use AC and Drink water.'")
    
        elif f_feel > 45:
            print("\n'Out door Condition is wrost, don't step outside otherwise you will suffer.'")
            
    print("\nThank You")

print("\n\tWelcome to Weather Report App\n")

city_input = input("Please Enter Your City Name :\n")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={api_key}"
)
info = dict(weather_data.json())

try:
    f_temp = info["main"]["temp"]
    f_feel = info['main']['feels_like']
except KeyError:
    print(f"Fail to fetch API , Please Try again later!")
    quit()  

c_temp = int((f_temp - 32) * 5/9)
c_feel = int((f_feel - 32) * 5/9)

### fail  to Implement ####
# import pint as p
# unit_reg = p.UnitRegistry()
# f_temp = int(info["main"]["temp"]) * unit_reg.degF
# c_temp = f_temp.to(unit_reg.degC)
# f_feel = int(info['main']['feels_like']) * unit_reg.degF
# c_feel = f_feel.to(unit_reg.degC)

f_display(f_temp,f_feel,city_input)

user_yes_celci = input("\nWant to Convert in celsius ? (y/n) ")
if user_yes_celci.lower() == 'y':
    f_display(c_temp,c_feel,city_input,'Celsious')
elif user_yes_celci.lower() == 'n':
    print("Thank You For using application")
else:
    print("invalid keyword. Please use y/n for proceed")
