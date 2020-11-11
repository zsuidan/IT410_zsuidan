#1. Create a single list that contains the following collection of data in the order provided:
employee_info = [1121, "Jackie Grainger", 22.22,
 1122, "Jignesh Thrakkar", 25.25,
 1127, "Dion Green", 28.75, False,
 24.32, 1132, "Jacob Gerber",
 "Sarah Sanderson", 23.45, 1137, True,
 "Brandon Heck", 1138, 25.84, True,
 1152, "David Toma", 22.65,
 23.75, 1157, "Charles King", False,
 "Jackie Grainger", 1121, 22.22, False,
 22.65, 1152, "David Toma"]

#2 & 3. Assume that the above information is a small sample of the company's data. Programmatically sort the information into three different lists: 
# one for employee numbers, one for employee names, and one for employee salary information. No duplicate data should make its way into the new lists.
employee_numbers = []
employee_names = []
employee_salaries = []

for value in employee_info:
    if value not in employee_numbers and value not in employee_names and value not in employee_salaries:
        if type(value) is int:
            employee_numbers.append(value)
        elif type(value) is str:
            employee_names.append(value)
        elif type(value) is float:
            employee_salaries.append(value)

#4. For each value in the list containing hourly wage information, multiply the current value by 1.3 (since benefits are about 30% of a person's salary) 
# and store each value in a list called total_hourly_rate. Programmatically determine the maximum value in the list and if it's over over 37.30, throw a 
# warning message that someone's salary may be a budget concern.
total_hourly_rate = []

for wage in employee_salaries:
    total_hourly_rate.append(wage * 1.3)

highest_rate = max(total_hourly_rate)

if highest_rate > 37.30:
    print("WARNING: Someone's salary may be a budget concern.")

#5. Determine if anyone's total hourly rate is between 28.15 and 30.65. If they are, add the hourly rate a new list called underpaid_salaries.
underpaid_salaries = []

for rate in total_hourly_rate:
    if rate >= 28.15 and rate <= 30.65:
        underpaid_salaries.append(rate)

#6. For each value in the list that contains unmodified salary information, calculate a raise in dollars according to the following rules:
# If the hourly rate is between 22 and 24 dollars per hour, apply a 5% raise to the current rate. If the hourly rate is between 24 and 26 dollars per hour, 
# apply a 4% raise to the current rate. If the hourly rate is between 26 and 28 dollars per hour, apply a 3% raise to the current rate. All other salary ranges 
# should get a standard 2% raise to the current rate. Add each new value you calculate to a new list called company_raises.
company_raises = []

for wage in employee_salaries:
    if wage >= 22 and wage < 24:
        company_raises.append(wage * 1.05)
    elif wage >= 24 and wage < 26:
        company_raises.append(wage * 1.04)
    elif wage >= 26 and wage < 28:
        company_raises.append(wage * 1.03)
    else: 
        company_raises.append(wage * 1.02)

#7. Design your own complex condition with no fewer than four different truth tests in it (all conditions must be on one line, in other words). 
# Above your condition, write out in comments the exact behavior you are implementing with Python.

#Tests if a given employee's information is correct and determines if they are paid above or below average, recommending 
# to give them a raise if their performance is excellent and they receive below average pay
employee_num = 1121
employee_name = "Jackie Grainger"
employee_salary = 22.22
employee_performance = "excellent"
average_salary = sum(employee_salaries)/len(employee_salaries)

if employee_num in employee_numbers and employee_name in employee_names and employee_salary in employee_salaries and employee_salary <= average_salary and employee_performance == "excellent":
    print(employee_name + " exists and is paid less than average, they should receive a raise.")
elif employee_num in employee_numbers and employee_name in employee_names and employee_salary in employee_salaries and employee_salary <= average_salary and employee_performance != "excellent":
    print(employee_name + " exists and is paid less than average.")
elif employee_num in employee_numbers and employee_name in employee_names and employee_salary in employee_salaries and employee_salary > average_salary:
    print(employee_name + " exists and is paid more than average.")
else: 
    print(employee_name + " does not exist, or the information given is incorrect.")