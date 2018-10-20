# chapter 11 - dictionaries

# created by {}, key-value pair can be any type
eng_2_spn = {}
print(eng_2_spn)
eng_2_spn['one'] = 'uno'
print(eng_2_spn)

eng_2_spn = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
print(eng_2_spn)

print('-' * 10)

# use dictionary and 'know' to make fib seq faster


# define dictionary as 'know' the first two values
known = {0:0, 1:1}

# fib sequence
def fibonacci(n):
    if n in known:  # check if we already computed the answer and stored it
        return known[n] # return the already computed answer
    res = fibonacci(n-1) + fibonacci(n-2) # if not, find the new answer
    known[n] = res # store the new answer 
    return res # return the new answer

print(fibonacci(50))

