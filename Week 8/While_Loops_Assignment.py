program_running = True

#Creates an empty list to store dictionaries of employee information later
employee_info = []

#Creates a loop which has several prompts for users to fill in information
while program_running:

    #Prompts user to input an employee ID
    employee_id = input("Enter your employee ID: ")

    #Checks if the ID is properly formatted, prompting the user to input again if not
    correct_id = False

    while not correct_id:
        if len(employee_id) == 7 and employee_id.isdigit():
            correct_id = True
        else: 
            correct_id = False

        if not correct_id:
            employee_id = input("Employee ID was not properly formatted. Please try again: ")

    #Prompts user to input a name
    employee_name = input("Enter your name: ")

    #Checks if the name is properly formatted, prompting the user to input again if not
    correct_name = False

    while not correct_name:
        if employee_name.replace(" ", "").isalpha():
            correct_name = True
        else: 
            correct_name = False

        if not correct_name:
            employee_name = input("Employee name was not properly formatted. Please try again: ")

    #Prompts user to input an email
    employee_email = input("Enter your email address: ")

    #Checks if the email is properly formatted, prompting the user to input again if not
    correct_email = False

    banned_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
    
    while not correct_email:
        correct_email = True

        for character in employee_email:
            if character in banned_email_characters:
                correct_email = False
        
        if not correct_email:
            employee_email = input("Employee email was not properly formatted. Please try again: ")
        
    #Prompts user to enter an address or leave the address blank
    employee_address = input("You may input your address or leave this blank: ")

    #Checks if the address is properly formatted, prompting the user to input again if not
    correct_address = False

    banned_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

    while not correct_address:
        correct_address = True

        for character in employee_address:
            if character in banned_address_characters:
                correct_address = False
        
        if not correct_address:
            employee_address = input("Employee address was not properly formatted. Please try again: ")

    #Adds all inputs into the employee info list as a dictionary
    employee_info.append({'employee_id': employee_id, 'employee_name': employee_name, 'employee_email': employee_email, 'employee_address': employee_address})

    #Asks user if they would like to input another employee
    add_more = input("Would you like to add another employee? (Y/N): ")

    #Checks if Y or N was entered, prompting user to enter again if not
    correct_letter = False

    while not correct_letter:
        if add_more.upper() == "Y" or add_more.upper() == "N":
            correct_letter = True
        else:
            add_more = input("Invalid response. Answer with either Y or N: ")

    #If user entered Y and have under 5 employees entered, the loop will restart and more employee information will be added, otherwise the loop is terminated
    if add_more.upper() == "Y":
        if len(employee_info) < 5:
            continue
        else:
            print("You may only store 5 employees.")
            break
    else:
        break
        
#Prints out each employee within the list on their own line 
for employee in employee_info:
    print(employee)