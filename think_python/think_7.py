# chapter 7 - iteration 

# updating variables
x = 0 
print(x)
x = x+1 
print(x)
print('-' * 10)

# while loop 
def countdown(n):
    while n > 0:
        print(n)
        n = n-1
    print('Blastoff!')

countdown(15)
print('-' * 10)

# breaks are useful because you can say
# 'stop when this happens'
# instead of keep going until this happens
# while look break example

def done():
    while True:
        line = input("> ")
        if line == 'done':
            print('done!')
            break
        else:
             print(line)

done()

# rather than testing equality, it's sometimes
# safer to use abs(a-b) < epsilon where epsilon
# signifies some value like 0.00000001 that's close enough. 

# if abs(y-x) < epsilon:
#         break



# algorithms are mechancial processes for solving a category of problem. 
# don't require intellegence, just follow the steps, find the solution

