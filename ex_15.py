# reading files 

# from the system inputs import arguements variable
from sys import argv

# the arguements inputted should be the script name and filename to read
script, filename = argv
# variable txt = open file name
txt = open(filename)

# print formatted statement using filename var
print(f"Here's your file {filename}:")
print(txt.read())
# print the result of text variable, then read it 

# ask user to type in the filename again
print("Type the filename again:")
file_again = input("> ")
# file again takes input given after prompt

text_again = open(file_again)
#text again variable opens the file_again input

# print the results of opening and reading the file again variable
print(text_again.read())





