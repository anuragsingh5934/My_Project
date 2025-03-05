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

city_input =   'sultanpur' #input("Please Enter Your City Name :\n")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={city_input}&units=imperial&APPID={api_key}"
)
info = weather_data.json()
#print(info)

f_temp = 0
f_feel = 0
#print(info)
for key,value in info.items():
    if 'main' in key:
        #print("main")
        f_feel = info['main']['feels_like']
        f_temp = info["main"]["temp"]
        break
else:
    print(f"Something went wrong\n\
    {key} {value}\n\
    {f_temp} {f_feel}")



import pint
temprature_conversion = pint.UnitRegistry()
fah_temp = temprature_conversion.Quantity(f_temp, temprature_conversion.degF)
fah_feel = temprature_conversion.Quantity(f_feel, temprature_conversion.degF)
c_temp_raw = str(fah_temp.to(temprature_conversion.degC)) 
c_feel_raw = str(fah_feel.to(temprature_conversion.degC))
c_temp = int(c_temp_raw[:2])
c_feel = int(c_feel_raw[:2])

f_display(f_temp,f_feel,city_input)

ask_Celsius = input("\nWant to Convert in celsius ? (y/n) ")

if ask_Celsius.lower() == 'y':
    f_display(c_temp,c_feel,city_input,'Celsious')
elif ask_Celsius.lower() == 'n':
    print("Thank You For using application")
else:
    print("invalid keyword. Please use y/n for proceed")