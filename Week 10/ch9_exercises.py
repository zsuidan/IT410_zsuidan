#Problem 9-1
#Creates a class named shirt that stores size and color attributes with a method to obtain the shirt attributes
print("Problem 9-1:")

class Shirt():
    """A simple class for representing a shirt"""
    def __init__(self, size, color):
        """Initialize size and color attributes"""
        self.size = size
        self.color = color
    
    def getShirtInfo(self):
        """Prints out shirt attributes"""
        print("The size of the shirt is " + self.size)
        print("The color of the shirt is " + self.color)

my_shirt = Shirt("M", "Red")
print(my_shirt.size)
print(my_shirt.color)

my_shirt.getShirtInfo()

my_other_shirt = Shirt("L", "Blue")
print(my_other_shirt.size)
print(my_other_shirt.color)

my_other_shirt.getShirtInfo()

#Problem 9-2
#Modifies the shirt class to include quantity with a method for increasing or decreasing the quantity
print("\nProblem 9-2:")

class Shirt2():
    """A simple class for representing a shirt"""
    def __init__(self, size, color):
        """Initialize size, color, and quantity attributes with a default of 1 for quantity"""
        self.size = size
        self.color = color
        self.quantity = 1
    
    def decreaseQuant(self, quant):
        """Decreases the quantity by an inputted amount"""
        self.quantity -= quant

    def getShirtInfo(self):
        """Prints out shirt attributes"""
        print("The size of the shirt is " + self.size)
        print("The color of the shirt is " + self.color)

    def increaseQuant(self, quant):
        """Increases the quantity by an inputted amount"""
        self.quantity += quant

new_shirt = Shirt2("S", "White")

new_shirt.increaseQuant(2)
print(new_shirt.quantity)

new_shirt.increaseQuant(4)
print(new_shirt.quantity)

new_shirt.increaseQuant(1)
print(new_shirt.quantity)

new_shirt.decreaseQuant(3)
print(new_shirt.quantity)

new_shirt.decreaseQuant(2)
print(new_shirt.quantity)

#Problem 9-3
#Adjusts the shirt class to be a general class for clothing which can be extended to other classes. Also creates a ShirtInherit class which inherits from the clothing class.
print("\nProblem 9-3:")

class Clothing():
    """A simple class for representing a piece of clothing"""
    def __init__(self, size, color):
        """Initialize size, color, and quantity attributes with a default of 1 for quantity"""
        self.size = size
        self.color = color
        self.quantity = 1
    
    def decreaseQuant(self, quant):
        """Decreases the quantity by an inputted amount"""
        self.quantity -= quant

    def getClothingInfo(self):
        """Prints out clothing attributes"""
        print("The size of the clothing is " + self.size)
        print("The color of the clothing is " + self.color)

    def increaseQuant(self, quant):
        """Increases the quantity by an inputted amount"""
        self.quantity += quant

class ShirtInherit(Clothing):
    """A simple class for representing a shirt"""
    def __init__(self, size, color, sleeve_type, printed_message):
        """Initializes size, color, and quantity attributes from the clothing parent class and initializes new attributes for sleeve type and printed message"""
        super().__init__(size, color)
        self.sleeve_type = sleeve_type
        self.printed_message = printed_message

    def printMessage(self):
        """Prints the current message on the shirt"""
        print(self.printed_message)

another_shirt = ShirtInherit("M", "Black", "Long", "Python is neat")

another_shirt.increaseQuant(4)
print(another_shirt.quantity)

another_shirt.printMessage()

#Problem 9-4
#Creates another class named pants which inherits from the clothing class
print("\nProblem 9-4:")

class Pants(Clothing):
    """A simple class for representing pants"""
    def __init__(self, size, color, fabric_type, style):
        """Initializes size, color, and quantity attributes from the clothing parent class and initializes new attributes for fabric type and style"""
        super().__init__(size, color)
        self.fabric_type = fabric_type
        self.style = style
