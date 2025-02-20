def engine_modification(current_size):
   
    print("WELCOME TO ENGINE MODIFICATION AREA")
   
    engine_loop = True

    while engine_loop:
        # current_size = int(input("Your size of engine - "))


        if current_size == 1200:
            cc_1200_user = input("This engine size is not very power full. Want to add Turbo booster or upgrade or quit? (t/u/q) : ")
            if cc_1200_user.lower() == 't':
                print("ok we are setting Turbo charger in your Car...")
                break
            if cc_1200_user.lower() == 'u':
                user_engine_upgrade_input = input(" How much CC you want- 1500, 2200 , more (1500/2200/more) ")
                if user_engine_upgrade_input == 1500:
                    print("We are upgrading your engine to 1500 cc")
                    break
            if cc_1200_user.lower() == 'q':
                break


        if current_size == 1500:
            cc_1500_user = input("This engine size is not very power full. Want to add Turbo booster or upgrade or quit? (t/u/q) : ")
            if cc_1500_user.lower() == 't':
                print("ok we are setting Turbo charger in your Car...")
            if cc_1500_user.lower() == 'u':
                user_engine_upgrade_input = input(" How much CC you want- 2200 , more (2200/more) ")
                if user_engine_upgrade_input == 2200:
                    print("We are upgrading your engine to 2200 cc")
            if cc_1500_user.lower() == 'q':
                break


        if current_size >= 1800:
            print("enough powerful for You. want to upgrade?")
            cc_1800_abv_user = input("(y,n,q)")
            if cc_1800_abv_user == 'q':
                break

def wheel_modi():
    print(f"Welcome to WHEEL WORKSHOP..")
    avl_wheel = [
  "Alloy Wheels",  
  "Steel Wheels",  
  "Forged Wheels",  
  "Carbon Fiber Wheels",  
  "Split-Rim Wheels",  
  "Spinner Wheels",  
  "Deep-Dish Wheels",  
  "Off-Road Wheels",  
  "Chrome Wheels",  
  "Custom Painted or Powder-Coated Wheels"
    ]
    for wheel in avl_wheel:
        print(f"\nHere is the list of wheel available")
        print(wheel)
    select_wheel = input("\nWrite name of wheel You Want - ")
    print(f"\nCongratulation we are adding {select_wheel.upper()} wheels in your vehicle.")