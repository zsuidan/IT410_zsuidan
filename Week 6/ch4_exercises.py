#Problem 4-1
print("Problem 4-1\n")
#Creates a list of favorite places to visit and uses a loop to print them out
fav_places = ["Mackinac Island", "Niagara Falls", "Frankenmuth", "Pictured Rocks"]

for place in fav_places:
    print(place + " is a nice place to visit.")

#Problem 4-2
print("\nProblem 4-2\n")
#creates a list of numbers from 90 to 100 and prints them using a loop
numbers = list(range(90,101))

for number in numbers:
    print(number)

#Problem 4-3
print("\nProblem 4-3\n")
#creates a list of numbers from 100,000 to 1,000,000 and prints the sum
numbers = list(range(100000, 1000001))

print(sum(numbers))

#Problem 4-4
print("\nProblem 4-4\n")
#creates a list of random numbers and prints the highest and lowest
random_numbers = [5, 8, 12, 68, 1, 42, 528, 101, 23, 304, 512, 689, 16, 61, 601, 15, 35, 85, 3, 97]

print(max(random_numbers))
print(min(random_numbers))

#Problem 4-5
print("\nProblem 4-5\n")
#Creates a list of numbers from 1 to 100 with multiples of 5
numbers = list(range(5,101,5))

print(numbers)

#Problem 4-6
print("\nProblem 4-6\n")
#Creates a list of numbers from 20 to 30, then creates another list with all of those numbers doubled and prints it
numbers = list(range(20,31))

print(numbers)

doubled_numbers = []
for number in numbers:
    doubled_numbers.append(number*2)

print(doubled_numbers)

#Problem 4-7
print("\nProblem 4-7\n")
#Uses the random number list from 4-4 and pulls specific numbers
random_numbers = [5, 8, 12, 68, 1, 42, 528, 101, 23, 304, 512, 689, 16, 61, 601, 15, 35, 85, 3, 97]

#first 3 numbers
print(random_numbers[0:3])

#numbers 5 through 10
print(random_numbers[5:11])

#last 4 numbers
print(random_numbers[-4:])

#Problem 4-8
print("\nProblem 4-8\n")
#Creates a list of favorite musicians, makes a copy of it, adds a musician to the original list, and prints both lists
fav_musicians = ["Elton John", "Metallica", "Daft Punk"]
fav_musicians_copy = fav_musicians[:]

fav_musicians.append("Black Sabbath")

print(fav_musicians)
print(fav_musicians_copy)

#Problem 4-9
print("\nProblem 4-9\n")
#Creates a tuple with a list of school grades and attempts to modify it
school_grades = ("1st", "2nd", "3rd", "4th", "5th")

school_grades[4] = "6th"
#Tuples cannot be modified, so attempting to change index 4 will result in an error