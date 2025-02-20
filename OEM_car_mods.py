from engine_wheel_modification import *

def oem_car_modification(size):
    '''Wheel modification function'''
    oem_fun = True

    print(f"\n\t\tWELCOME TO OEM MODIFICATION.\n\nProvide Infomation for Modification")
    print(f"Your engine size {size}cc.")
    usr_name = input("Your name\n ")
    if usr_name != '':
        oem_fun = True
    else:
        oem_fun =False

    while oem_fun:
        print(f"\n\n\tHello Mr {usr_name.upper()}")
        strt = input(f"Where to start for modification\n\n---LIST---\nWHEEL\nENGINE\nBODY\n ")
        if strt.upper() == "WHEEL":
            wheel_modi()
        elif strt.upper() == 'ENGINE':
            engine_modification()

oem_car_modification(1200)