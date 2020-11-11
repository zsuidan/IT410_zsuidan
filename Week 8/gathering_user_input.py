area_code = input("Please enter your area code: ")

if area_code:
    #tests if the input is an integer, then tests if the length of the input is 3
    try:
        int(area_code)
        if len(area_code) == 3:
            print("Your area code is " + area_code)
        else: 
            print("Your inputted area code isn't 3 digits.")
    except:
        print("You did not provide a valid area code.")
#if nothing was provided, this message is displayed
else:
    print("You did not enter an area code.")