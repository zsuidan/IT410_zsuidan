#1. Creates a list of all classes I have taken at Walsh
classes = ["it 402", "it 410", "mgt 201", "qm 202", "mdl 101"]

#2. Sorts the class list and prints a statement using them in uppercase
classes.sort()

for item in classes:
    print("I have taken " + item.upper() + " at Walsh College.")

#3. Adds courses I will take next semester and sorts again
classes.append("com 320")
classes.append("it 405")
classes.append("it 408")

classes.sort()

print("This is my course of study with upcoming courses added:")

for item in classes:
    print(item.upper())

#4. Removes courses taken already from the list
classes.remove("it 402")
classes.remove("it 410")
classes.remove("mgt 201")
classes.remove("qm 202")
classes.remove("mdl 101")

print("I do not have to take these courses:" + "\nIT 402\nIT 410\nMGT 201\nQM 202\nMDL 101")

#5. Prints remaining items in list 
print("I plan to take the following courses next term:")

for item in classes:
    print(item.upper())

#6. Creates a list of numbers from 1 to 1000 which are divisible by 6
num_list = list(range(6,1000,6))

#7. Prints first 20 numbers in the number list
print("Here are 20 numbers divisible by 6:")

print(num_list[0:20])

#8. Calculates and stores maximum number on the list
max_num = max(num_list)

#9. Prints the maximum value
print("The maximum value in the list is: " + str(max_num))

#10. Calculates, stores, and prints the sum of the 10th through the 50th variables in the list 
list_sum = sum(num_list[9:50])

print("Here is the sum of several values in the list: " + str(list_sum))

#11. Overwrites the list of classes with the list of numbers
classes = num_list