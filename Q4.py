# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case

day=int(input("Select a number from 1-7:"))

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wnesday")
    case 4:
        print("Thersday")
    case 5:
        print("Friday")
    case 6:
        print("Satrday")
    case 7:
        print("Sunday")
    case _:
        print("Invalid input")