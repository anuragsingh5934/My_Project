price = 10_00_000

has_good_credit = True
if has_good_credit:
    down_payment = int(price) * 0.1
    print(f"Your credit is good , so you have to pay ${down_payment}.")
else:
    down_pay = int(price) * 0.2
    print(f"You have to pay ${down_pay}")