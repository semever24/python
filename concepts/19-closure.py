def outer_function(x):
    def inner_function(y):
        return x  *  y    # x is remembered
    return inner_function

double = outer_function(2)
triple = outer_function(3)

print(double(5))
print(triple(5))