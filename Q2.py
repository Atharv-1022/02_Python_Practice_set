# Create a program that checks if a person is eligible to vote (age >= 18)
age=int(input("Enter your age:"))

if(age>18):
    print("You are eligible for voting")
elif(age==18):
    print("Come next year")
else:
    print("You are not eligible  for voting")
    