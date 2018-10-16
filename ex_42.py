# is-a, has-a, objects and classes

# x is a y, has a z 

# assign class to animal, animal is a object
class Animal(object):
    pass

# assign class to dog, dog is an animal, has a name
class Dog(Animal):
# define __init__ self, name
    def __init__(self, name):
        self.name = name

# assign class to cat, cat is an animal, has a name
class Cat(Animal):
    def __init__(self, name):
        self.name = name

# assign class to person, person is an object, has a name and a pet
class Person(object):
    def __init__(self, name):
        self.name = name 
        # person has a pet of some sort 
        self.pet = None

# assign a clas to Employee, employee is a person, has a name and salary
class Emplyee(Person):
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
rover = Dog("rover")

# satan is a ccat
satan = Cat("satan")

# mary is a person
Mary = Person("Mary")

# marry is a person, therefor has self.pet attribute
# we set self.pet attribute to be satan, which is we 
# previously set to be of class cat, and cat is an animal
# which has a name, which we put in the self
Mary.pet = satan


frank = Emplyee("Frank", 120000)

frank.pet = rover

flipper = Fish()

Chris = Salmon()

Harry = Halibut()