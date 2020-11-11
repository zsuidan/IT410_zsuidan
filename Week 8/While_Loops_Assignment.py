correct_info = True

employee_info = []

while correct_info:
    employee_id = input("Enter your employee ID: ")

    if employee_id.isdigit() and len(employee_id) == 7:
        correct_info = True
    else:
        break

    employee_name = input("Enter your name: ")

    if employee_name.replace(' ', '').isalpha():
        correct_info = True
    else:
        break

    employee_email = input("Enter your email address: ")

    banned_email_characters = ["!", '"', "'", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"]
    
    for character in employee_email:
        if character in banned_email_characters:
            correct_info = False

    if not correct_info:
        break

    employee_address = input("You may input your address or leave this blank: ")

    banned_address_characters = ["!", '"', "'", "@", "$", "%", "^", "&", "*", "_", "=", "+", "<", ">", "?", ";", ":", "[", "]", "{", "}"]

    for character in employee_address:
        if character in banned_address_characters:
            correct_info = False
    
    if not correct_info:
        break
    
    if employee_address:
        print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". You did not provide an address.")
    else:
        print("Hello, " + employee_name + ". Your Employee ID is " + employee_id + ", and your email address is " + employee_email + ". Your address is " + employee_address + ".")

    employee_info.append({'employee_id': employee_id, 'employee_name': employee_name, 'employee_email': employee_email, 'employee_address': employee_address})

    add_more = input("Would you like to add another employee? (Y/N): ")

    if add_more.upper() == "Y":
        continue
    else:
        break

for employee in employee_info:
    print(employee)