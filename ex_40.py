# modules, classes, and objects

# three ways to get things from things

# dictionaries 
my_stuff = {'entry': 'this is entry 1', 'two': 'yellow'}

# modules (calling another script my_stuff.py)
import my_stuff
# a function
my_stuff.apple()
# a variable
print(my_stuff.tangerine)


# class style define class my_stuff as an object
class my_stuff(object):
    def __init__(self):
        self.tangerine = "I'm a classy tangerine"
    def apple(self):
        print("I am a classy apple")

# call it like a function to make more
thing = my_stuff()

thing.apple()
print(thing.tangerine)


# classes are like blue prints to new modules 


# to be honest I have no idea how this works
class song(object):
    def __init__(self, lyrics):
        self.lyrics = lyrics
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)

happy_bday = song(["Happy Birthday to you",
                   "Happy Birthday to you",
                   "Happy Birthday dear person",
                   "Happy Birthday to you"])

bulls_on_parade = song(["They rally around the family",
                        "With pockets full of shells"])


happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

