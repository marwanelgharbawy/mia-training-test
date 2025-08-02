def add(x, y):
    return x + y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None
    
def square(x):
    return x * x
    
def subtract(x, y):
    return x - y

x = 10
y = 5

print("Sum is:", add(x, y))
print("Quotient is:", divide(x, y))
print("Difference is:", subtract(x, y))
print("Square is:", square(x))