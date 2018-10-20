# chapter 6 - fruitfull functions

import math as mt

def what_is_e():
    e = mt.exp(1)
    return e

print(what_is_e())


def fibonacci (n):
    if n == 0:
        return 0
    elif  n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fib = fibonacci(10)
print(fib)

print('-' * 10)

# isinstance() returns true if object is selected data type
