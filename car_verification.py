def car_verifi(car_name):

    car_names = [
        "Swift",  
        "Creta",  
        "Scorpio",  
        "Nexon",  
        "Baleno",  
        "Seltos",  
        "Innova Crysta",  
        "City",  
        "i20",  
        "Harrier",  
        "Ertiga",  
        "Kwid",  
        "EcoSport",  
        "Polo",  
        "Rapid",  
        "Hector",  
        "Magnite",  
        "Vitara Brezza",  
        "Fortuner",  
        "Thar"  
    ]
    if car_name in car_names:
        print("\n\t\tVerifying...\nWe do modify this model car")
    else:
        print(f"We Dont modify {car_name} car")