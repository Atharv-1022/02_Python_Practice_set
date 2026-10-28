# Write a program that keeps asking the user to enter a password until they enter the correct one

P=12345

password=int(input("Enter the password:"))

while P!=password:
    password=int(input("Enter Right Password:"))

print("Welcome host")