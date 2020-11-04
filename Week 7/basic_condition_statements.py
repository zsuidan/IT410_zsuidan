variable1 = 24
variable2 = "string value of some sort"
variable3 = 3.14159

if variable1 >= 23:
    print("Variable 1 is greater than or equal to 23")

if type(variable3) is int:
    print("The variable is an integer.")
elif type(variable3) is str:
    print("The variable is a string.")
elif type(variable3) is float:
    print("The variable is a floating point type.")
else:
    print("The variable is something else.")