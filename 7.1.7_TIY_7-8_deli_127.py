sandwiches_orders = ['tuna','straberry','cocacola','veg','non-veg']
finished_sandwiches = []
order_active = False

user = input("Do you want to eat ?\n - ")

if user == 'yes':
    print("Oh ! seems like you are hungry ! (tap enter)")
    verifying = input(f"Tap enter to see menu {input()}")
    order_active = True
    print("-----Here is a menu for You-----")

    # for sand in sandwiches_orders:
    #     print(f"\t{sand}")
if user == 'no':
    print(f"\n\tGet 2 pizza at rs 99.")
    attracted_user = input("\n\tWant to order ? ")
    if attracted_user == 'yes':
        print("\nThank you for Changing your Mind.")
        order_active = True
    elif attracted_user == 'no':
        print("Thank you")
        order_active = False
    else:
        print("Thank you sir")
# else:
#     order_active = False
#     print("Please use Valid keyword ( yes or no )")

while order_active:
    for sand in sandwiches_orders:
        print(f"{sand}")
    user_order = input("\nHey now tell me, What you want to eat ?\n---")
    print(f"\t\tWe are processing your {user_order}...\n")
    finished_sandwiches += user_order
    sandwiches_orders.remove(user_order)
    repeat_order = input("Want to order more ? (yes / no) : ")
    if repeat_order.lower() == 'no':
        print("Thank you for using service.\nHere is the food you have ordered:")
        for finished in finished_sandwiches:
            print(f"{finished} ready now !")
            break
    else:
        pass