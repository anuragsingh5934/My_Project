# car workshop

def car_details(owner_name,car_name,buy_year,cc,color,known_prob='',modificaton=''):
    
    double = int(cc) * 2
    dou = int(cc) * 1.5
    '''car details and service log'''

    if modificaton == 'y':
        level_of_mod = input('level of modification you want (1-3) - ' )
        if level_of_mod == '3':
            ask_oem = input("Want OEM modification (y/n) - ")
            if ask_oem == 'y':
                import OEM_car_mods
                OEM_car_mods.oem_car_modification(in_cc)
            skip_ = input("You have to pay 60000 coins (tap enter)\n")
            print(f"We are Processing Your {car_name.upper()} car for modification of level 3.\nIn which we install extream level kits.\n")
            print(f"Engine size will be upgraded form {cc}cc to {double}cc. Which boost you driving thrill.\n")
            print(f"we change your {color.upper()} to racing Red blue yellow strip.\n")
            payment_ask = input(f"MR {owner_name.upper()}. Want to pay? (y/n)")
            if payment_ask =='y':
        
                payment_gatway()
            
        elif level_of_mod == '2':
            enter = input("You have to pay 3000 coins (tap enter)\n")
            print(f"We are Processing Your {car_name.upper()} car for modification of level 2.\nIn which we install medium level kits.\n")
            print(f"Engine size will be same and we add turbo boost and you get performence of {dou}cc form {cc}cc. Which boost you driving thrill.\n")
            print(f"we change your {color.upper()} to racing Red blue.\n")
            payment_ask = input(f"MR {owner_name.upper()}. Want to pay? (y/n)")
            if payment_ask =='y':
                
                payment_gatway()

        elif level_of_mod == '1':
            enter = input("You have to pay 1000 coins (tap enter)\n")
            print(f"We are Processing Your {car_name.upper()} car for modification of level 2.\nIn which we install low level kits.\n")
            print(f"Engine size will be same.\n")
            payment_ask = input(f"MR {owner_name.upper()}. Want to pay? (y/n)")
            if payment_ask =='y':
                
                payment_gatway()
        else:
            print("enter a valid keyword")
    else:
        import user_details_dict as usr

        user_data_dict1 = usr.usr_info_dict(owner_name = in_car_owner, car_name = in_car_name, buy_year = in_year ,cc = in_cc ,color = in_car_color)
        print("\n\t\tHERE IS A DETAILS OF USER\n")
        for key, value in user_data_dict1.items():
            print(f"{key.capitalize()} is {value.upper()}.")


from pyment import *
print("\n\t\tWELCOME\n\t\tFILL ALL AREA")
in_car_name = input("Enter Your car name - ")
import car_verification as auth
auth.car_verifi(in_car_name)
in_car_owner = input('car owner name - ')
in_year = input("car year - ")
in_cc =input("car cc - ")
in_car_color = input("car color - ")
in_car_prob = input("car problem - ")
in_modification = input("want any modification (y/n) - ")

carapp = car_details(in_car_owner,in_car_name,in_year,in_cc,in_car_color,in_car_prob,in_modification)
