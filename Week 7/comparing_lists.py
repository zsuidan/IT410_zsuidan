list1 = ["one", "two", "three"]
list2 = ["one", "apple", "three", "four"]

#list1 = [1, 2, 3]
#list2 = ["1", "2", "3"]

if list1 > list2:
    print("List 1 is greater than list 2")

#Compares lists value by value, once it finds a different value it detemines if its less than and stops checking other values. 
#Letters later in the alphabet are considered greater than those early in the alphabet.

if len(list1) < len(list2):
    print("List 2 is bigger in terms of number of values than list 1")

#If you want to compare lists by size, you need to use len()