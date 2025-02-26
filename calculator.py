def add(num1,num2):
    return num1+num2

def sub(num1,num2):
    return num1-num2

def multi(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2

def avg(num1,num2):
    return (num1+num2)/2

print("Please select Opration:\n\
      1.Addition\n\
      2.Substration\n\
      3.Multiply\n\
      4.Division\n\
      5.Avrage " )

user_select = int(input("Select number from 1 - 5 :  "))
in_num1 = int(input("Enter first Number : "))
in_num2 = int(input("Enter second number : "))

if user_select == 1:
    added = add(in_num1,in_num2)
    print(f"Your answer is {added}")
elif user_select == 2:
    print(f"Substraction of {in_num1} and {in_num2} is - {sub(in_num1,in_num2)}")
elif user_select == 3:
    print(f"Multiplication of {in_num1} and {in_num2} is - {multi(in_num1,in_num2)}")
elif user_select == 4:
    print("Division of", in_num1 ,"and", in_num2, "is - ", div(in_num1,in_num2))
elif user_select == 5:
    print(f"The Average of {in_num1} and {in_num2} is - {avg(in_num1,in_num2)}")