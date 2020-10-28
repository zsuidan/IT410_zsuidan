#Problem 3-1
print("Problem 3-1:\n")

#Creates a list of the last 4 books read and prints each individually in title case
books_read = ["Systems Analysis and Design", "Fundamentals of Management", "Statistics for Business & Economics", "Python Crash Course"]
print(books_read[0].title())
print(books_read[1].title())
print(books_read[2].title())
print(books_read[3].title())

#Problem 3-2
print("\nProblem 3-2:\n")

#creates a list of favorite TV shows
fav_shows = ["Jeopardy", "Wheel of Fortune", "The Boys", "South Park"]

#wheel of fortune cancelled and replaced
fav_shows[1] = "Family Feud"

#adds two more shows, one at the end and one at a specific index in the middle
fav_shows.append("Family Guy")
fav_shows.insert(1, "The Office")

#pops last show and prints it
popped_show = fav_shows.pop()
print(popped_show)

#deletes first three shows and prints remaining
del fav_shows[0:3]
print(fav_shows)

#Problem 3-3 
print("\nProblem 3-3\n")

#creates list of classes for this semester and prints it
class_list = ["IT 402", "IT 410", "MGT 201", "QM 202", "MDL 101"]
print(class_list)

#prints how many classes are in the list
print("I have " + str(len(class_list)) + " classes.")

#prints a sorted class list without changing the list
print(sorted(class_list))

#sorts the classes and prints the list
class_list.sort()
print(class_list)

#reverses the order of the list and prints the list
class_list.reverse()
print(class_list)

#Problem 3-4
print("\nProblem 3-4\n")

#code attempting to print the 10th number in the list, but the index starts counting from 0 so index 10 does not exist
num_list = list(range(1,11))
print(num_list[10])

#print(num_list[9]) should be used if you want the 10th index 