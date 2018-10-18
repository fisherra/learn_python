# functions and files 

# bash command to move ex_19.py output to new text file "python ex_19.py echo >> ex_20.txt"

from sys import argv
script, input_file = argv

# define print_all() function in script
def print_all(f):
    print(f.read())

# define rewind() function in script
def rewind(f):
    f.seek(0)

# define print_a_line function in script
def print_a_line(line, f):
    print(line, f.readline())


# test the functions
current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")
rewind(current_file)

print("Let's print three lines:")

line = 1
print_a_line(line, current_file)

line = line + 1
print_a_line(line, current_file)

line = line + 1 
print_a_line(line, current_file)



