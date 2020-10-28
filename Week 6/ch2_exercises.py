#Problem 2-1
#Creates a variable with favorite restaurant, prints, then changes to favorite dish and prints again
favorite = "Highland House"
print(favorite)
favorite = "Ravioli"
print(favorite)

#Problem 2-2
#Creates two variables with the last place you purchased an item from and which item was purchased then prints a sentence with them
lastLocation = "Amazon"
lastItem = "python textbook"
print("The last time I went to " + lastLocation + ", I purchased a " + lastItem + ".")

#Problem 2-3
#Creates a variable with favorite car and prints in lower, upper, and title case
favCar = "Corvette"
print(favCar.lower())
print(favCar.upper())
print(favCar.title())

#Problem 2-4
#Creates a varible with a favorite quote and prints it, then prints again while removing the tab and new line
favQuote = "\tOne small step for man, one giant leap for mankind.\n"
print(favQuote)
print(favQuote.lstrip())
print(favQuote.strip())

#Problem 2-5
#Creates a variable with an answer to a sample math problem and prints it using type casting
mathAnswer = (2*10)/5
print("The result of my math problem is: " + str(mathAnswer))