# Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.
print("1]Addistion\n2]Subtraction\n3]Multiplicastion\n4]Division\n5]remove remonder")
num=int(input("Select your operstion to perfome:"))
num1=int(input("Enter your first digit:"))
num2=int(input("Enter your Second digit:"))

match num:
    case 1:
        print(num1,"+",num2,"=",num1+num2)
    case 2:
        print(num1,"-",num2,"=",num1-num2)
    case 3:
        print(num1,"X",num2,"=",num1*num2)
    case 4:
        print(num1,"/",num2,"=",num1/num2)
    case 5:
        print(num1,"%",num2,"=",num1%num2)
    case _:
        print("Chosse from the given opstion")

