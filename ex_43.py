# Angkor What

from sys import exit
from random import randint
from textwrap import dedent

# base class of scene, a thing that all scenes do 
class scene(object):
    def enter(self): 
        print("You've entered a blank scene.")
        print("Please subclass this scene and configure enter()")
        exit(1)

# create the game engine, which is an object
# engine has self, and scene_map, scene_map = variable scene_map
class engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
    
# play(self) is defined with current_scene = opening scene function
# play(self) is defined with last scene = next_scene('finished') function
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
    
# while the current scene isn't equal to finished the next scene is the enter function
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)
        
        current_scene.enter()



# create class death, which is a scene, with attributes enter(death)
class death(scene):
    def enter(self):
        print("\nShiva has decided that your time upon the earth is over.")
        print(dedent("""
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
            """))

        exit(0)



class outside(scene):
    def enter(self):
        print(dedent("""
        You're exploring the deep and lush jungles of Cambodia. 
        After some time, you stumble upon an ancient Angkor temple.
        The temple looks dangerous and forboding...
        As if it's warning you not to enter. 

        Suddenly you hear rustling in the nearby trees. An impending
        sense of doom overcomes you. 

        Do you run into the temple to take shelter from the unknown?
        """))

        action = input("> ")

        if "Y" in action or "y" in action:
            print(dedent("""
            You quickly enter the temple.
            Suddenly a door slams shut behind you. 
            It looks like you're stuck in here..."""))
        
            return 'corridor'
   
        elif "N" in action or "n" in action:
            print(dedent("""You decide not to enter the temple and stand your ground. 
                    The ancient and all powerful Garuda flies up and eats your face."""
                ))

            return 'death'

        else:
            print("You must quickly choose! Do you enter the temple, yes or no!?")

            return 'outside'

        

class corridor(scene):
    def enter(self):
        print(dedent("""

        There is now a long corridor ahead of you. 
        Choose an Option:
        
        1. Check the corridor for booby traps.
        2. Pray to Brahma that he guides your way.
        3. Run down the corridor as fast as you can.
        
        """))
        
        brahma = False
        corridor = True

        while corridor == True:

            choice = input("> ")

            if choice == "1":
                print("\nChecking for booby traps...")
                print("You're bitten by a cobra!") 

                return 'death'

            elif choice == "2" and not brahma:
                print("\nYou pray to Brahma, nothing seems to change...\n")
                print("Now what?\n")

                brahma = True


            elif choice == "2" and brahma:
                print("You've spent too long praying and die of starvation!")

                return 'death'

            elif choice == "3" and brahma == False:
                print("You fall into a pit of spikes!")

                return 'death'

            elif choice == "3" and brahma == True:
                print("\nYou sprint down the corridor...")
                print("You've made it to the other side.\n")
                corridor = False

                return 'ganesha'

            else:
                print("You must choose 1, 2, or 3!")


class ganesha(scene):
    def enter(self):
        print(dedent("""
            The corridor opens up into a dimly lit room.
            A statue of Ganesha stands in the middle.
            What do you do?
            """))

        rub_belly = input("> ")



        if "rub" in rub_belly or "belly" in rub_belly or "good" in rub_belly or "luck" in rub_belly:
            print(dedent("""
            
            You've decided to rub his belly for good luck.
            After rubbing his belly, a hidden door opens!
            You go throw the hidden doorway.
                """))

            return 'naga'

        else:
            print("\nHanuman throws a rock at your head!")

            return 'death'


class naga(scene):
    def enter(self):

        print(dedent("""
        You meet the great and mighty Naga!

        Naga asks you... 
        
        "What weighs more, a pound of lead, or a pound of gold?"
        
        """))

        naga = input("> ")

        if "same" in naga or "Same" in naga:
            print(dedent("""
            Naga nods in approval.
            You jump on Naga's back!
            Naga takes you to the treasure room!
            in the treasure room you find...
            .
            .
            .
            .


            Enlightenment.

            """))

            exit(1)


        else:
            print("\nNaga eats you in one bite!")

            return 'death'

# map
class map(object):

    scenes = {
         'outside': outside(),
         'death': death(),
         'corridor': corridor(),
         'ganesha': ganesha(),
         'naga': naga()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = map.scenes.get(scene_name)

        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = map('outside')
a_game = engine(a_map)
a_game.play()