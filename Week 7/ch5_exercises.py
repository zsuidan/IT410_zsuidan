#Problem 5-1
print("Problem 5-1:")
#Sets variables and performs various conditional tests
variable1 = 5
variable2 = "Zach"
variable3 = 1.7
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4]
list3 = ["1", "2", "3"]
#I expect this to be true
if variable1 > variable3:
    print("Variable 1 is greater than variable 3")

#I expect this to be true
if type(variable2) is str:
    print("My name is " + variable2)

#I expect this to be true
if len(list1) < len(list2):
    print("List 1 has less values in it than list 2")

#I expect this to be false
if variable1 in list1:
    print("Variable 1 is in list 1")

#I expect this to be false
if type(variable3) is int:
    print("Variable 3 is an integer")

#I expect this to be false
if list1 == list3:
    print("List 1 is the same as list 3")

#Problem 5-2
print("\nProblem 5-2:")
#Creates an integer variable and tests if it is odd
#This should evaluate to true
number = 7

if number % 2 == 1:
    print(str(number) + " is odd.")

#This should evaluate to false
other_number = 4

if other_number % 2 == 1:
    print(str(other_number) + " is odd.")

#Problem 5-3
print("\nProblem 5-3:")
#Modifies the program in the previous problem to add one if the number is even then print the new number 
number = 7

if number % 2 == 1:
    print(str(number) + " is odd.")
else: 
    number += 1
    print(str(number))

other_number = 4

if other_number % 2 == 1:
    print(str(other_number) + " is odd.")
else:
    other_number += 1
    print(str(other_number))

#Problem 5-4
print("\nProblem 5-4:")
#Creates a list of favorite fruits and uses an if-else chain to print out a message based on the number of fruits
fav_fruits = ["Raspberry", "Strawberry", "Grape"]

if len(fav_fruits) == 2:
    print("I like 2 fruits")
elif len(fav_fruits) == 3:
    print("I like three fruits")
elif len(fav_fruits) == 4:
    print("I like four fruits")
elif len(fav_fruits) >= 5:
    print("I like several fruits")
else: 
    print("I don't like fruits")

#Problem 5-5
print("\nProblem 5-5:")
#Creates a list of numbers between 1 and 55, creates 2 variables containing random numbers, and checks if those numbers are in the list
num_list = [1, 5, 8, 11, 13, 16, 18, 22, 23, 27, 35, 41, 50]

num1 = 11
num2 = 52

if num1 in num_list:
    print(str(num1) + " was found in the list.")
else:
    print(str(num1) + " was not found in the list.")

if num2 in num_list:
    print(str(num2) + " was found in the list.")
else:
    print(str(num2) + " was not found in the list.")

#Problem 5-6
print("\nProblem 5-6:")
#Creates a list of favorite stores and another list of stores that have sales, then loops through the list of favorite stores to see if they have sales and prints whether or not they do
fav_stores = ["Amazon", "Meijer", "DSW", "Walmart"]
running_sales = ["Amazon", "Walmart"]

for store in fav_stores:
    if store in running_sales:
        print(store + " is running a sale, take advantage of it!")
    else:
        print(store + " is not running a sale. :(")