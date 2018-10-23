# Object Oriented Warrior Battle!
 
import random
import math
 
# Warriors will have names, health, and attack and block maximums
# They will have the capabilities to attack and block random amounts

# create class warrior, set defaults
class Warrior:
    def __init__(self, name="warrior", health=0, attkMax=0, blockMax=0):
        self.name = name
        self.health = health
        self.attkMax = attkMax
        self.blockMax = blockMax
 
 # how to calculate attacks
    def attack(self):
        # Randomly calculate the attack amount
        # random() returns a value from 0.0 to 1.0
        attkAmt = self.attkMax * (random.random() + .5)
 
        return attkAmt

 # how to calculate blocks
    def block(self):
 
        # Randomly calculate how much of the attack was blocked
        blockAmt = self.blockMax * (random.random() + .5)
 
        return blockAmt
 
# The Battle class will have the capability to loop until 1 Warrior dies
# The Warriors will each get a turn to attack each turn
 
# battle object
class Battle:
 
    def startFight(self, warrior1, warrior2):
 
        # Continue looping until a Warrior dies switching back and
        # forth as the Warriors attack each other
        while True:
            if self.getAttackResult(warrior1, warrior2) == "Game Over":
                print("Game Over")
                break
 
            if self.getAttackResult(warrior2, warrior1) == "Game Over":
                print("Game Over")
                break
 
    # A function will receive each Warrior that will attack the other
    # Have the attack and block amounts be integers to make the results clean
    # Output the results of the fight as it goes
    # If a Warrior dies return that result to end the looping in the
    # above function
 
    # Make this method static because we don't need to use self
    @staticmethod
    def getAttackResult(warriorA, warriorB):
        warriorAAttkAmt = warriorA.attack()
 
        warriorBBlockAmt = warriorB.block()
 
        damage2WarriorB = math.ceil(warriorAAttkAmt - warriorBBlockAmt)
 
        warriorB.health = warriorB.health - damage2WarriorB
 
        print("{} attacks {} and deals {} damage".format(warriorA.name,
                                                         warriorB.name, damage2WarriorB))
 
        print("{} is down to {} health".format(warriorB.name,
                                               warriorB.health))
 
        if warriorB.health <= 0:
            print("{} has Died and {} is Victorious".format(warriorB.name,
                                                            warriorA.name))
 
            return "Game Over"
        else:
            return "Fight Again"
 
 # the arena!
def main():
 
    # Create 2 Warriors
    Odyssus = Warrior("Odyssus", 50, 20, 10)
    Titan = Warrior("Titan", 50, 20, 10)
 
    # Create Battle object
    battle = Battle()
 
    # Initiate Battle
    battle.startFight(Odyssus, Titan)
 
main()