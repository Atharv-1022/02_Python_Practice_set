# Write a program that asks the user for a number and prints whether it is positive, negative, or zero.
num=int(input("Enter a number:"))

if(num>0):
    print("The",num,"is \"POSITIVE\"")
elif(num<0):
    print("The",num,"is \"NEGATIVE\"")
elif(num==0):
    print("The",num,"is \ZERO\"")
else:
    print("Invalid input")