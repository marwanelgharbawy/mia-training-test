def add(x, y):
    return x + y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return None

x = 10
y = 0

print("Sum is:", add(x, y))
print("Quotient is:", divide(x, y))