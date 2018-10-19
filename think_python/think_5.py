# conditional and recursion


# the modulus op
print(5 % 3) # returns 2 
# 5 goes into 3 once, with a REMAINDER of 2 

# Booleans return T/F

# comparison ops
print('-' * 10)
print(5 == 5)
print('A' == 'A')
print('A' == 'B')

print('-' * 10)
print(5 != 6)
print(5 > 6)
print( 5 < 6)
print(5 <= 5)
print(5 >= 6)

# logical ops
print('-' * 10)
print(5 == 6 or 6 == 6)
print(5 == 6 and 6 == 6)
print(not 5 == 6)

# conditional execution
print('-' * 10)
x = 5
y = 6

if x < y:
    print("x is less than y")

def even_checker(arg_1):
    if arg_1%2 == 0:
        print('num is even')
    else:
        print('num not even')

even_checker(0)
even_checker(1)
even_checker(2)
print('-' * 10)

# functions referencing themselves 
def countdown(n):
    if n <= 0:
        print("blast off!")
    else:
        print(n)
        countdown(n-1)

countdown(10)
print('-' * 10)

# another recursive function
def print_n(s, n):
    if n == 0: 
        return
    else:
        print(s)
        print_n(s, n-1)

print_n("hi there\n", 6)
print('-' * 10)
