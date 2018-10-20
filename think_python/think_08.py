# chapter 8 - strings 

# strings are a sequence of characters
string = 'yes, this is dog'
letter = string[0]

print(string)
print('-' * 10 )

def letter_by_line(string):
    n = 0 
    while n < len(string):
        letter = string[n]
        print(letter)
        n = n + 1

letter_by_line('yes, this is dog')

print('-' * 10)

# traversal - running through a string, chr by chr

# printing slices
s = 'Monty Python'
print(s[0:5])
print(s[6:12])
# but you can just omit the first or second half
print(s[:5])
print(s[6:])
print('-' * 10)

# strings are immutable, you can't change an existing string
greetings = "Hello World!"
# greetings[0] = "j"  <--- this won't fly 

# but this will
new_greetings = "J" + greetings[1:]

print(greetings)
print(new_greetings)

print('-' * 10)

# searching
def find(word, letter):
    index = 0 
    while index < len(word):
        if word[index] == letter:
            return index
        else:
            index = index + 1
    return -1

miss_index = find("mississippi", "p")
print(miss_index)

print('-' * 10)

# counters

# count the i's in mississippi
def i_count(word):
    index = 0
    count = 0
    while(index < len(word)):
        if word[index] == 'i':
            count = count + 1
        index = index + 1
    return count

print(i_count('mississippi'))

print('-' * 10)

# method

word = 'banana'
print(word.upper())

# methods are like functions but with different notation.
# target.method(arguement)

print(word.isdecimal())
print(word.find('na'))

print('-' * 10)

# the in op

print('n' in 'banana')
print('seed' in 'banana')

# simple!

print('-' * 10)

# comparisons on strings work alphabetically

if 'apple' > 'banana':
    print('apple greater than banana')

if 'apple' < 'banana':
    print('apple less than banana')

if 'banana' == 'banana':
    print('banana is banana')

# 'lesser' words are earlier in the alphabet. a = 1. 

