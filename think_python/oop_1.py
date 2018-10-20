# dog

# Real world objects all have attributes and capabilities

# attributes of a dog - Name, Height, Weight
# capabilities of dog - Run, Bark, Eat

# define attributes (fields / variables) 
# define capabilities (methods / functions)

# dog object is created from a template, called a class


# create class of dog
class dog:
# define attributes name, height, weight, give them defaults
    def __init__(self, name = "", height = 0, weight = 0):
# create variables that we can assign easily
        self.name = name
        self.height = height
        self.weight = weight

# create methods run, eat, and bark
    def run(self):
        print("{} the dog runs!".format(self.name))
        
    def eat(self):
        print("{} the dog eats!".format(self.name))
        
    def bark(self):
        print("{} the dog barks!".format(self.name))




def main():

    spot = dog("spot", 12, 22)

    spot.bark()
    spot.run()
    spot.eat()

    maxwell = dog()
    maxwell.name = "maxwell"
    maxwell.bark()




main()