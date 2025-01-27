weight = int(input("What is your weight: "))
kg_lbs = input(f"{weight} in (k)Kg or (l)Lbs: ")

if kg_lbs.lower() == 'k':
    lbs = weight * 2.20462262185
    print(f"Your weight is {round(lbs)}lbs")
elif kg_lbs.lower() == 'l':
    kg = weight / 2.20462262185
    print(f"Your weight is {round(kg)}kg.")
else:
    print("Not valid info")
    print("Thank you for visiting.")