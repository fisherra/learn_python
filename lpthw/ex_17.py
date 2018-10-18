# python script to copy bash cp 

# import argv from command line inputs
from sys import argv

# from location in computer, import files present
from os.path import exists

# unpack argv
script, from_file, to_file = argv

# copy from file 1 to file 2
print(f"Copy from {from_file} to {to_file}.")

# we could do this in a signle line. how?
in_file = open(from_file)
indata = in_file.read()

# check length of input file
print(f"The input file is {len(indata)} bytes long")
# check if output file exists
print(f"Does the output file really exist? {exists(to_file)}")
# ask for permission to continue 
print("ready, hit RETURN to continue, CTRL-C to abort.") 

# user permission
input("> ") 

# new variable out_file is the opened to_file in write mode
out_file = open(to_file, "w")
# out file .write() becomes the in data 
out_file.write(indata)

# confirm and close
print("Alright, all done.")
out_file.close
in_file.close

