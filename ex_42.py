# is-a, has-a, objects and classes

# x is a y, has a z 

# create class animal is an object and has attributes 'pass'
class animal(object):
    pass

# create class dog is an animal which is an object
# has initiated attributes 'self', and 'name'
class dog(animal):
    def __init__(self, name):
        self.name = name

# create class cat is an animal which is an object
# has initiated attributes 'self', and 'name' = name var
class cat(animal):
    def __init__(self, name):
        self.name = name

class person(object):
    def __init__(self, name):
        self.name = name
        # also create empty slot for a pet 
        self.pet = None
    

class employee(person):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary



# using fish
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass


# rover is a dog
rover = dog("Ronald")
print(rover.name)


# satan is a ccat
satan = cat("Santa")
print(satan.name)

# mary is a person
Mary = person("Mary-the-person")
print(Mary.name)

# marry is a person, therefor has self.pet attribute
# we set self.pet attribute to be satan, which is we 
# previously set to be of class cat, and cat is an animal
# which has a name, which we put in the self
Mary.pet = satan


frank = employee("Frank", 120000)

frank.pet = rover

flipper = Fish()

Chris = Salmon()

Harry = Halibut()