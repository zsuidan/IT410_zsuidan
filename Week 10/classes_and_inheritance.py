class Pet():
    """A simple class for representing a pet"""

    def __init__(self, name, age):
        """Initialize name and age variables/attributes"""
        self.name = name
        self.age = age
    
    def clean(self):
        """Represents the act of cleaning the pet"""
        print(self.name + " is clean!")


class Dog(Pet):
    """A simple class for representing a dog"""

    def __init__(self, name, age, breed):
        """Initialize name and age variables/attributes for the dog"""
        #Calls the constructor from the parent class and adds an additional attribute for breed
        super().__init__(name, age)
        self.breed = breed

    def placeDogInCarrier(self):
        """This represents placing the dog in a car carrier"""
        print(self.name + " is in the car carrier!")

    def takeToVet(self):
        """Contains all of the tasks needed to get the dog to the vet"""
        self.placeDogInCarrier()
        self.__visitVet()

    def __visitVet(self):
        """Represents the act of taking the dog to the vet"""
        print(self.name + " is on their way to the vet!")

class Cat(Pet):
    """A simple class for representing a cat"""
    def __init__(self, name, age):
        """Initialize name and age variables/attributes for the cat"""
        super().__init__(name, age)  

my_dog = Dog("Scout", 3, "German Shepherd")
print("My dog's name is: " + my_dog.name)

#Clean method is inherited from the parent class, so it still works
my_dog.clean()
print("My Dog's breed is: " + my_dog.breed)

my_cat = Cat("Fluffy", 3)
print("My cat's name is: " + my_cat.name)