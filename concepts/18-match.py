day = int(input("Enter number from 1 to 7 to fetch the day: "))

"""
match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")
    case _:
        print("Wrong value. Please enter correct value.")
"""

match day:
    case 1 | 2 | 3 | 4 | 5:
        print("I love weekdays")
    case 6 | 7:
        print("I love weekends")