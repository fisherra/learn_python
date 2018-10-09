#  reading and writing files 

# memorize these commands 

# close - closes the file 
# read - reads the file
# truncate - empties the file
# write('stuff') - writes 'stuff' to the file
# seek(0) - move the read / write location to the beginning of the file 


# create a simple text editor

# from terminal line, import argumenets variable
from sys import argv

# arguements variable is unpacked as script name, file name
script, filename = argv

# print statements warning you of truncation
print(f"W'ere going to erase {filename}")
print("If you don't want that, ,hit CTRL-C.")
print("If you do want that, hit RETURN.")

# request truncation authorization
input("? ")

print("Opening the file...")

# the target becomes the contents of filename
target = open(filename, "w")

# empty file
print("Truncating the file. Goodbye!")
target.truncate()

# ask for 3 new lines of file input
print("Now I'm going to ask you for three new lines.")
line1 = input("Line 1: ")
line2 = input("Line 2: ")
line3 = input("Line 3: ")

# tell user you'll create that
print("I'm going to write these to the file.")

# write lines, include line breaks
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

# close file
print("And finally, we close it.")
target.close()



