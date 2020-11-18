program_running = True

def get_id():
    """Obtain Employee ID from the user"""

    returned_id = input("Enter your employee ID: ")

    correct_id = False

    while not correct_id:
        if len(returned_id) <= 7 and returned_id.isdigit():
            correct_id = True
        else: 
            correct_id = False

        if not correct_id:
            returned_id = input("Employee ID was not properly formatted. Please try again: ")
    
    return returned_id

def get_info(passed_info_name, passed_info_needed):
    """Obtain a piece of information from the user"""

    if passed_info_needed:
        returned_info = input("Please enter your " + passed_info_name + ": ")
    else:
        returned_info = input("Please enter your " + passed_info_name + ". You may also leave this blank: ")

    return returned_info

def check_characters(passed_field_name, passed_value_needed, passed_field_value, passed_banned_characters):
    """Check to ensure that the value entered for a certain field was correct, prompting the user to re-enter until it is correct"""

    correct_field = False

    if passed_value_needed:
        while not passed_field_value:
            passed_field_value = input(passed_field_name + " was not entered. Please enter a value: ")

    while not correct_field:
        correct_field = True

        for character in passed_field_value:
            if character in passed_banned_characters:
                correct_field = False
        
        if not correct_field:
            passed_field_value = input(passed_field_name + " was not properly formatted. Please try again: ")

    return passed_field_value

def add_another(passed_variable):
    """Asks user if they would like to continue adding more of a certain variable"""

    add_more = input("Would you like to add another " + passed_variable + "? (Y/N): ")

    #Checks if Y or N was entered, prompting user to enter again if not
    correct_letter = False

    while not correct_letter:
        if add_more.upper() == "Y" or add_more.upper() == "N":
            correct_letter = True
        else:
            add_more = input("Invalid response. Answer with either Y or N: ")
    
    #Returns true if Y is entered and false is N is entered
    if add_more.upper() == "Y":
        return True
    elif add_more.upper() == "N":
        return False


#Creates an empty list to store dictionaries of employee information later
employee_info = []

#Creates a loop which has several prompts for users to fill in information
while program_running:

    #Obtains ID input from user and checks if it is valid, prompting them to input again if not
    employee_id = get_id()
  
    #Prompts user to enter their name
    employee_name = get_info("name", True)

    #Checks the name for banned characters, if any are detected the user will be asked to input until it is correct
    banned_name_characters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]

    employee_name = check_characters("Employee name", True, employee_name, banned_name_characters)

    #Prompts user to input an email
    employee_email = get_info("email", True)

    #Checks the email for banned characters, if any are detected the user will be asked to input until it is correct
    banned_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
    
    employee_email = check_characters("Employee email", True, employee_email, banned_email_characters)
        
    #Prompts user to enter an address or leave the address blank
    employee_address = get_info("address", False)

    #Checks if the address is properly formatted, prompting the user to input again if not
    banned_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

    employee_address = check_characters("Employee address", False, employee_address, banned_address_characters)

    #Adds all inputs into the employee info list as a dictionary
    employee_info.append({'employee_id': employee_id, 'employee_name': employee_name, 'employee_email': employee_email, 'employee_address': employee_address})

    #If there are 5 employees, the loop ends, otherwise the user is asked if they would like to add more
    if len(employee_info) >= 5:
        print("You may only store 5 employees.")
        break
    else:
        continue_adding = add_another("employee")
        if continue_adding:
            continue
        else:
            break
        
#Prints out each employee within the list on their own line 
for employee in employee_info:
    print(employee)