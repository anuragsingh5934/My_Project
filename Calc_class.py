class Calculator():
    '''this class'''
    def __init__(self,nmbr1,nmbr2):
        self.num1 = nmbr1
        self.num2 = nmbr2

    def add(self):
        return self.num1+self.num2

    def sub(self):
        return self.num1-self.num2

    def multi(self):
        return self.num1*self.num2

    def div(self):
        return self.num1/self.num2

    def avg(self):
        return (self.num1+self.num2)/2

print("Please select Opration:\n\
      1.Addition\n\
      2.Substration\n\
      3.Multiply\n\
      4.Division\n\
      5.Avrage " )

user_select = int(input("Select number from 1 - 5 :  "))
if user_select > 5:
    print(f"We dont accept {user_select}.\n\
          This is not in our list.\n\
          Please try again (1-5).")
in_num1 = int(input("Enter first Number : "))
in_num2 = int(input("Enter second number : "))

clc = Calculator(in_num1,in_num2)
if user_select == 1:
    print(f"The sum of {in_num1} and {in_num2} is {clc.add()}")
elif user_select == 2:
    print(f"If you substract {in_num2} form {in_num1} then you get {clc.sub}")
elif user_select == 3:
    print(f"If you multiply these two numbers '{in_num1} and {in_num2}'. the result is {clc.multi()} ")
elif user_select == 4:
    print(f"If you divide these number then you well get {clc.div()}")
elif user_select == 5:
    print(f'You want Average of {in_num1} and {in_num2}. the answer is {clc.avg}')
elif user_select == str:
    print(f"""Sorry ! , Please Enter Valid Key\n\
         We failed to understand "{user_select}".""")