def payment_gatway():
    payment_sys = True
    while payment_sys:
        print(f'Welcom to payment Gateway plateform.')
        card_name = input("enter your name as menstioned in your card - ")
        card_number = input("Enter Your card number - ")
        card_cvv = int(input("enter 3 digit ccv -"))
        if card_cvv >= 999:
            print("\nWrong CVV code")
        
        card_pin = input("\nenter your pin - ")
        print(f"\nYour card name is {card_name}.\nCard number is - {card_number}.\nCard CVV is {card_cvv}. ")
        verify_pin = input("\nverify your Pin again to payment - ")
        if verify_pin == card_pin:
            OTP = input(f"\nPin verification is done.\nEnter OTP - ")
            print("payment done")
            break
        else:
            break
    print("Payment done successfully")