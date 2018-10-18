# more practice

# skipped encoding exercise

print("Let's practice everything, again!")
print('You\'d need to know \'bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\t The lovely world 
with logic so firmly planted
cannot discern \nthe needs of love
nor comprehen passion from intuition 
and requires an explaination
\n\t\twhere there is none. 
"""

print("-----------")
print(poem)
print("-----------")


five = 10-2+3-6

print(f"This shoud be {five}")

def secret_formula(started):
    jelly_bean = started * 500
    jar = jelly_bean / 1000
    crates = jar / 100
    return jelly_bean, jar, crates

start_point = 10000
beans, jars, crates = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

start_point = start_point / 10 

print("we can also do it this way")

formula = secret_formula(start_point)

# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))s
