# doing things to lists

# create a string
ten_things = "Apples Oranges Crows Telephon Light Sugar"

# print statement
print("there aren't 10 things in that list. let's fix it")

# split into variable stuff according to ' ' 
stuff = ten_things.split(' ')

# create new list variable
more_stuff = ['Day', 'Night', 'Song', 'Frisbee', 'Corn', 'Banana', 'Girl', 'Boy']

# while original list is less than 10 elements long, add from the end of this list
while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding", next_one)
    stuff.append(next_one)
    print("There we go: ", stuff)
    print(f"There are {len(stuff)} items now.")


# access these elements
print("Let's do some things with stuff.")
print(stuff[1])
print(stuff[-1]) # whoa! fancy print(stuff.pop())
print(' '.join(stuff)) # what? cool! print('#'.join(stuff[3:5])) # super stellar!