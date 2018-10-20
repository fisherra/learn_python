# chapter 10 - lists 

# lists work just like they do in R
my_list = [1, 'hello', True, [1,2]]
print(my_list[3])

# lists are mutable
my_list[3] = "new 3"
print(my_list[3])

# lists can be concatenated, multiplied, and sliced
print('-' * 10)

my_list_2 = my_list + my_list
print(my_list_2)

my_list_2x = my_list_2 * 2
print(my_list_2x)

print(my_list_2x[0:4])

print('-' * 10)

# list methods

# append module adds arguement
my_list.append('im appended')
print(my_list)

# extend module adds other list as arguement
ex_list = ['list', 'is', 'good']
my_list.extend(ex_list)
print(my_list)

# total += 1 means total = total + 1

# pop
print("-" * 10)
t = ['a', 'b', 'c']
x  = t.pop(1)
print(t)
print(x)
print(t[0], x, t[1])

print('-' * 10)

# remove module
t = ['a', 'b', 'c']
t.remove('b')
print(t)

print('-' * 10)

# delete t
del t

# lists and strings
stringy = "Im a good string yea"
listy = list(stringy)
print(listy)


splity = stringy.split()
print(splity)

stringy_2 = "Im-a-good-string-yea"
delim = '-'
splity_2 = stringy_2.split('-')
print(splity_2)

joiny = delim.join(splity_2)
print(joiny)