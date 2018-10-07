# more more print

# create string called formatter with 4 spaces for input
formatter = "{} {} {} {}"

# print formatter with 1,2,3,4 in those inputs using .format
print(formatter.format(1,2,3,4))
# replace with strings
print(formatter.format("one", "two", "three","four"))
# replace with T/F
print(formatter.format(True, False, False, True))
# replace formatter with formatter so you see 16 x {}
print(formatter.format(formatter, formatter, formatter, formatter))
# go back to strings
print(formatter.format(
    "This is a story",
    "about a boy",
    "who liked apples",
    "but not oranges"
))