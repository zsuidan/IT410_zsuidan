generic_list = [1,2,3,4,5,6,7,8,9,10]
odd_numbers = []
even_numbers = []

for generic_value in generic_list:
    if generic_value % 2 == 1:
        print(str(generic_value) + " is odd")
        odd_numbers.append(generic_value)
    elif generic_value % 2 == 0:
        print(str(generic_value) + " is even")
        even_numbers.append(generic_value)

print("The list of odd numbers is: ")
print(odd_numbers)

print("The list of even numbers is: ")
print(even_numbers)

#% calculates the remainder when dividing by a number, any odd number divided by 2 has a remainder of 1 while an even number has a remainder of 0 

generic_list = [1,2,3,4,4,5,6,7,7,8,9,9,10]
odd_numbers = []
even_numbers = []

for generic_value in generic_list:
    if generic_value not in odd_numbers and generic_value not in even_numbers:
        if generic_value % 2 == 1:
            print(str(generic_value) + " is odd")
            odd_numbers.append(generic_value)
        elif generic_value % 2 == 0:
            print(str(generic_value) + " is even")
            even_numbers.append(generic_value)

print("The list of odd numbers is: ")
print(odd_numbers)

print("The list of even numbers is: ")
print(even_numbers)

#Nested if statements can be used to remove duplicates by checking if they already were added to the other lists