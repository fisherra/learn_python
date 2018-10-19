# chapter 3 - functions

print('-' * 10)

# int function
print(int('32'))
# print(int('hello')) doesn't work

# float function
print(float('2.99999'))
print(float(3))

# string function
print(type(str(666)))
print('-' * 10)

# math module
import math
print(math)

# module objects contain variables, functions, etc
# to access them you must specify the module and the 
# name of the tool, in dot notation. for example: 
print(math.log10(100))
print("heres pi")
print(math.pi)
print("here's the sin of pi")
print(math.sin(math.pi))
print("math.pi is only accurate to 15 digits")
print('-' * 10)

# creating new functions
def song_lyrics():
    print("yeahhhh, wooowow, yeahhhh, yeahhh,")
    print("yeah yeah yeah, no, yeahhhh")
    
song_lyrics()

# functions in functions
def repeat_lyrics():
    song_lyrics()
    song_lyrics()

repeat_lyrics()

print('-' * 10 )
 
 # parameters and arguements

 # variables inside functions are local

def cat_twice(part_1, part_2):
    cat = part_1 + part_2
    print(cat)
    print(cat)

cat_twice("alpha ", "beta")

# but I can't print(cat), it only exists in the function

def cat_twice(part_1, part_2):
    global cat # make cat variable global intead of local
    cat = part_1 + part_2
    print(cat)
    print(cat)

cat_twice("alpha ", "beta")

print("and for the global test:")
print(cat)
print('-' * 10)

# fruitfull functions and void functions

# fruitful functions return values
math.cos(1)
# but the value is lost forever unless you save it
cos_1 = math.cos(1)
print(cos_1)

# void functions perform an action but have no return
print("hey there!")
hey_there = print("hey there!")
print(hey_there)

