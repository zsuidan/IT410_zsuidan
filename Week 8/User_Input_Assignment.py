correct_info = True

#Creates a loop which is broken any time information is entered incorrectly
while correct_info:
    #Prompts user to input their Employee ID then checks if it is composed of only numbers and the length is 7
    employee_id = input("Enter your employee ID: ")

    if employee_id.isdigit() and len(employee_id) <= 7:
        correct_info = True
    else:
        break
    
    #Prompts user to enter their name, if any banned characters are used or nothing was entered the loop ends 
    employee_name = input("Enter your name: ")

    banned_name_characters = ["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]

    for character in employee_name:
        if character in banned_name_characters:
            correct_info = False

    if not correct_info or not employee_name:
        break

    #Prompts user to enter their email, if any banned characters are used or nothing was entered the loop ends
    employee_email = input("Enter your email address: ")

    banned_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
    
    for character in employee_email:
        if character in banned_email_characters:
            correct_info = False

    if not correct_info or not employee_email:
        break

    #Prompts user to input their address, if the address contains any banned characters it ends the program
    employee_address = input("You may input your address or leave this blank: ")

    banned_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

    for character in employee_address:
        if character in banned_address_characters:
            correct_info = False
    
    if not correct_info:
        break
    
    #Prints a message with the employee's information, the message changes depending on if an address was provided or not
    if employee_address:
        print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". Your address is " + employee_address + ".")
    else:
        print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". You did not provide an address.")

    #Ends the loop since all data has been entered
    break