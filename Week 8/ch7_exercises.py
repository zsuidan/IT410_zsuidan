#Problem 7-1
#Prompts user to input their favorite restaurant and uses it in a print statement
print("Problem 7-1")

fav_restaurant = input("What is your favorite restaurant?: ")

print("Let me help you find the closest " + fav_restaurant)

#Problem 7-2
#Prompts user to input two numbers and multiplies them together, printing the result
print("\nProblem 7-2")

first_num = input("Enter a number: ")
second_num = input("Enter another number: ")

product = int(first_num) * int(second_num)

print(first_num + " times " + second_num + " equals " + str(product))

#Problem 7-3
#Prompts user to input items they are having for dinner using a while loop, these items are added to a list and the list is printed
print("\nProblem 7-3")

program_running = True

dinner_items = []

while program_running:
    dinner_item = input("What is one of the things you are having for dinner?: ")
    dinner_items.append(dinner_item)

    continue_adding = input("Do you want to add another item? (Y/N): ")
    if continue_adding.upper() == "N":
        break
    else:
        continue

print(dinner_items)

#Problem 7-4
#Asks user for a carnival ride they would like to go on, gives the price for the ride or tells them the ride wasn't found, then asks if they would like to go on another ride
print("\nProblem 7-4")

while program_running:
    which_ride = input("Which ride would you like to go on?: ")
    if which_ride.title() == "Ferris Wheel":
        print("Riding the Ferris Wheel will cost $2")
    elif which_ride.lower() == "tilt-a-whirl":
        print("Riding the tilt-a-whirl will cost $3")
    elif which_ride.lower() == "pirate ship":
        print("Riding the pirate ship will cost $3.50")
    else:
        print("Ride was not found.")

    more_rides = input("Would you like to go on another ride? (Y/N): ")
    if more_rides.upper() == "N":
        break
    else:
        continue

#Problem 7-5
#Creates a list of groceries with duplicates of an item, then uses a loop to remove the item with duplicates 
print("\nProblem 7-5")

grocery_list = ['milk', 'juice', 'apples', 'bread', 'cereal','apples', 'pasta', 'apples']

while ('apples' in grocery_list):
    grocery_list.remove('apples')

print(grocery_list)