price = 30
txt = f"The product price is {price}"
print(txt)

name = "SK"
location = "Bangalore"
txt = f"my name is {name} and I am from {location}"
print(txt)

price = 57
txt = f"The product price is {price:.2f}"
print(txt)

txt = f"The product price is {12*10}"
print(txt)

price = 110
tax = 0.55
final_price = f"Final product price is {price + (price*tax)} dollars"
print(final_price)

price = 48
txt = f"Product price is {'Expensive' if price>50 else 'Cheap'}"
print(txt)

fruit = "apple"
txt = f"Fruit name is {fruit.upper()}"
print(txt)

def myconverter(x):
    return x * 0.3048
txt = f"The plane is flying at a {myconverter(35000)} meter altitude"
print(txt)