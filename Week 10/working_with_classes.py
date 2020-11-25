class Dog():
    """A simple class for representing a dog"""

    def __init__(self, name, age):
        """Initialize name and age variables/attributes"""
        self.name = name
        self.age = age
    
    def clean(self):
        """Represents the act of cleaning the dog"""
        print(self.name + " is clean!")

    def placeDogInCarrier(self):
        """This represents placing the dog in a car carrier"""
        print(self.name + " is in the car carrier!")

    def takeToVet(self):
        """Contains all of the tasks needed to get the dog to the vet"""
        self.placeDogInCarrier()
        self.__visitVet()

    #Private methods cannot be called outside of the class
    def __visitVet(self):
        """Represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")

my_dog = Dog("Scout", 3)
print("My dog's name is: " + my_dog.name)
my_dog.takeToVet()
