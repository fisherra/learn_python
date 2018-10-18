# functions can return something

def add(a, b):
    print(f"Adding {a} and {b}")
    return a + b

def subtract(a, b):
    print(f"Subtract {a} and {b}")
    return a - b

def multiply(a, b):
    print(f"Multiply {a} and {b}")
    return a * b

def divide(a,b):
    print(f"Divide {a} and {b}")
    return a / b

print("Let's do some math with just functions!")
c = add(5,2)
d = subtract(5,2)
e = multiply(5,2)
f = divide(5,2)

print(f"addition is {c}, subtraction is {d}, multiplication is {e}, division is {f}")






