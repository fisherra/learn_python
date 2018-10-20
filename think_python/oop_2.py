# square

class square:
    def __init__(self, height="0", width="0"):
        self.height = height
        self.width = width


# a getter allows reference to defined fields above to retrieve values
    @property 
    def height(self):
        print("Retrieving height input...")

        return self.__height
    
    @property
    def width(self):
        print("Retrieving width input...")

        return self.__width
    

    # setters protect the value from being input wrong
    @height.setter
    def height(self, value):
 
        # We protect the height from receiving a bad value
        if value.isdigit():
 
            # Put a __ before this private field
            self.__height = value
        else:
            print("Please only enter numbers for height")


    @width.setter
    def width(self, value):
        if value.isdigit():
            self.__width = value
        else:
            print("Please only enter numbers for width")
 
    
    def get_area(self):
        return int(self.__height) * int(self.__width)


def main():

    a_square = square()

    height = input("height > ")
    width = input("width > ")

    a_square.height = height
    a_square.width = width

    print("The height is ", a_square.height)
    print("The width is ", a_square.width)
 
    if height != width:
        print("\nThis is not a true square!")


    print("The area is ", a_square.get_area())


main()