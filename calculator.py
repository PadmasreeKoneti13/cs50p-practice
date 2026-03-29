print("Welcome To The Calculator Program")
print("1.Addition","2.Subtraction","3.Multiplication","4.Division",sep="\n")
option = int(input("Enter your option:"))
if option == 1:
    print("You have selected addition.")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"The addition of {num1} and {num2} is {num1+num2}")
elif option == 2:
    print("You have selected subtraction.")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"The subtraction of {num1} and {num2} is {num1-num2}")
elif option == 3:
    print("You have selected multiplication.")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"The multiplication of {num1} and {num2} is {num1*num2}")
elif option == 4:
    print("You have selected division.")
    num1 = int(input("Enter first number:"))
    num2 = int(input("Enter second number:"))
    print(f"The division of {num1} and {num2} is {num1/num2}")
else:
    print("You have not entered a valid option")