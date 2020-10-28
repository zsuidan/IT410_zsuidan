#makes a list with the numbers 1 through 10
numbers = list(range(1,11))

print(numbers)

#makes a list that counts up by 2 until it reaches 11
numbers = list(range(1,11,2))

print(numbers)

#uses a loop to divide each value from 945
numbers = list(range(1,11,2))

for number in numbers:
    print(945/number)

#prints minimum, maximum, and sum of numbers in the list
numbers = list(range(1,11,2))

print(min(numbers))
print(max(numbers))
print(sum(numbers))