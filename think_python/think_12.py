# chapter 12 - tuples

# tuples are imumutable lists

t = ('a', 'b', 'c', 'd')
print(t)
print(type(t))

# must have following , for single entry or else not tuple
tu = ('a',)
ts = ('a')
print(type(tu))
print(type(ts))

print('-' * 10)
t = tuple('colombine')
print(t)
print(t[0])
print(t[5:])

# remember can't be modified in place

# tuples are very boring actually
