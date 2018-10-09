# more functions

def cheese_and_crackers(cheese_count, boxes_of_crackers):
        print(f"You have {cheese_count} cheeses!")
        print(f"You have {boxes_of_crackers} boxes of crackers!")
        print("That's enough for a party!")
        print(f"\n")



# we can give the functions numbers directly
cheese_and_crackers(20,30)

# or we can just use variables from our script
amount_of_cheese = 10 
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)

# we can even do math inside a function
cheese_and_crackers(10 + 5, 25 / 5)

# and we can combine the two 
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 200)

