# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd"
num=int(input("Enter a number:"))

if (num%2==0):
    print(num,"is \'EVEN\'")
elif(num%2!=0):
    print(num,"is \'ODD\'")
else:
    print("invalid value")
