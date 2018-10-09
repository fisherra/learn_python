 # names variables, code, functions

 # all about functions

 # make functions using def 

 # print two args 
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# the *args was pointless
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this function just prints one arg
def print_one(arg):
    print(f"arg: {arg}")

# this function has no input
def print_none():
    print("I got nothin'")

# test the functions
print_two("Fisher", "Ankney")
print_two_again("Fisher", "Ankney")
print_one("Fisher")
print_none()

