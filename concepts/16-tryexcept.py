try:
    number1 = int(input("Enter number1: "))
    number2 = int(input("Enter number2: "))
    
    output = number1/number2
    print(output)
except ZeroDivisionError:
    print("ZeroDivisionError")
except ValueError:
    print("ValueError")
else:
    print("Works good")
finally:
    print("End of try/except")