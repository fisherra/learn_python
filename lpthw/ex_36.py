# make a game of choices 

from sys import exit

def angkor():
    print(f"\nYou're deep in the jungles of Cambodia.")
    print("You come across an ancient Angkor temple.")
    print(f"Do you go inside the temple?\n")

    choice = input("> ")

    if "Y" in choice or "y" in choice:
        print(f"\nYou enter the temple.")
        corridor()
    elif "N" in choice or "n" in choice:
        print("\nYou decide not to enter the temple.")
        print("The Garuda flies up and eats your face.")
        dead()
    else:
        print(f"\nYou must choose yes or no!\n")
        angkor()


def corridor(): 
    print("There is a long corridor ahead of you.")
    print("Choose an option:\n")
    print("1. Check the corridor for booby traps.")
    print("2. Pray to Brahma that he guides your way.")
    print("3. Run down the corridor as fast as you can.\n")
    brahma = False
    corridor = True

    while corridor == True:
        choice = input("> ")

        if choice == "1":
            print("\nChecking for booby traps...")
            print("You're bitten by a cobra!") 
            dead()
        elif choice == "2" and not brahma:
            print("\nYou pray to Brahma, nothing seems to change...")
            print("Now what?\n")
            brahma = True
        elif choice == "2" and brahma:
            print("You've spent too long praying and die of starvation!")
            dead()
        elif choice == "3" and brahma == False:
            print("You fall into a pit of spikes!")
            dead()
        elif choice == "3" and brahma == True:
            print("\nYou sprint down the corridor...")
            print("You've made it to the other side.\n")
            corridor = False
            ganesha()
        else:
            print("You must choose 1, 2, or 3!")

def ganesha():
    print("The corridor opens up into a dimly lit room.")
    print("A statue of Ganesha stands in the middle.")
    print("What do you do?\n")

    rub_belly = input("> ")

    if "rub" in rub_belly or "belly" in rub_belly or "good" in rub_belly or "luck" in rub_belly:
        print("\nYou've decided to rub his belly for good luck")
        print("After rubbing his belly, a hidden door opens!")
        print("You go throw the hidden doorway.\n")
        naga()
    else:
        print("\nHanuman Throws a rock at your head!")
        dead()

def naga(): 
    print("\nYou meet the great and mighty Naga!")
    print("\nNaga asks you -\n")
    print("'What weighs more, a pound of lead, or a pound of gold?'\n")

    naga = input("> ")

    if "same" in naga or "Same" in naga:
        print("\nNaga nods in approval.")
        print("You jump on Naga's back!")
        print("Naga takes you to the treasure room!\n")
        print("in the treasure room you find...")
        print(".\n.\n.\n.\n.\n")
        print("Enlightenment.\n")
        exit(0)
    else:
        print("\nNaga eats you in one bite!")
        dead()

def dead():
    print("\nShiva has decided that your time upon the earth is over.")
    print("""
 @@@@@                                        @@@@@
@@@@@@@                                      @@@@@@@
@@@@@@@           @@@@@@@@@@@@@@@            @@@@@@@
 @@@@@@@@       @@@@@@@@@@@@@@@@@@@        @@@@@@@@
     @@@@@     @@@@@@@@@@@@@@@@@@@@@     @@@@@
       @@@@@  @@@@@@@@@@@@@@@@@@@@@@@  @@@@@
         @@  @@@@@@@@@@@@@@@@@@@@@@@@@  @@
            @@@@@@@    @@@@@@    @@@@@@
            @@@@@@      @@@@      @@@@@
            @@@@@@      @@@@      @@@@@
             @@@@@@    @@@@@@    @@@@@
              @@@@@@@@@@@  @@@@@@@@@@
               @@@@@@@@@@  @@@@@@@@@
           @@   @@@@@@@@@@@@@@@@@   @@
           @@@@  @@@@ @ @ @ @ @@@@  @@@@
          @@@@@   @@@ @ @ @ @ @@@   @@@@@
        @@@@@      @@@@@@@@@@@@@      @@@@@
      @@@@          @@@@@@@@@@@          @@@@
   @@@@@              @@@@@@@              @@@@@
  @@@@@@@                                 @@@@@@@
   @@@@@                                   @@@@@
""")
    exit(0)


angkor()