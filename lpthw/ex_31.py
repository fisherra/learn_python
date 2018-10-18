# making decisions

print("""
You enter a dark room with two doors. 
Do you go through door number 1 or 2?
""") 

door = input("> ")

if door == "1":
    print("There's a giant bear here eating cheesecake. What do you do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("the bear eats your face. good job.")
    elif bear == "2":
        print("the bear eats your legs, good job.")
    else: 
        print(f"well doing {bear} is probably better.")
        print("bear runs away")

elif door == "2":
    print("You stare into the endless abyssa t Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clohtespins.")
    print("3. understanding revolvers yelling melodies?")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.") 
        print("Good Job!")
    else:
        print("The insanity rots your eyes into a pool of muck.") 
        print("Good Job!")

else:
    print("you stumble around and fall on a knife and die. Good job!")

