class Person():
    """A simple class for representing a person"""
    def __init__(self, name, email):
        self.name = name
        self.email = email

class Student(Person):
    """A simple class for representing a student"""
    def __init__(self, name, email, student_id, program_of_study):
        super().__init__(name, email)
        self.student_id = student_id
        self.program_of_study = program_of_study

    def showStudentInformation(self):
        """Prints out all information for a certain student"""
        print("Name: " + self.name.title() + " | Email: " + self.email + " | Student ID: " + self.student_id + " | Program of study: " + self.program_of_study.title())
        
class Instructor(Person):
    """A simple class for representing an instructor"""
    def __init__(self, name, email, instructor_id, institution_graduated_from, highest_degree_earned):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution_graduated_from = institution_graduated_from
        self.highest_degree_earned = highest_degree_earned

    def showInstructorInformation(self):
        """Prints out all information for a certain instructor"""
        print("Name: " + self.name.title() + " | Email: " + self.email + " | Instructor ID: " + self.instructor_id + " | Graduated from: " + self.institution_graduated_from.title() + " | Degree earned: " + self.highest_degree_earned.title())

class Validator():
    """A class for representing a list of banned characters"""
    def __init__(self, banned_characters):
        self.banned_characters = banned_characters

    def checkCharacters(self, information):
        """Checks entered information to see if it contains any banned characters"""
        correct_characters = True

        for character in information:
            if character in self.banned_characters:
                correct_characters = False
        
        return correct_characters

def displayInformation(individuals):
    """Determines the type of each object in a list and obtains information based on the type"""
    for individual in individuals:
        if type(individual) == Student:
            individual.showStudentInformation()
        elif type(individual) == Instructor:
            individual.showInstructorInformation()

#Creates an empty list to store students and instructors
college_records = []

program_running = True

while program_running:

    #Asks user if they would like to enter an instructor or a student 
    input_type = input("What type of person do you want to add? (Instructor/Student): ")

    input_correct = False

    while not input_correct:
        if input_type.lower() == "instructor":
            input_correct = True

        elif input_type.lower() == "student":
            input_correct = True

        else:
            input_type = input("Incorrect type entered. Please enter either \"Instructor\" or \"Student\": ")

    #Obtains name information from user
    name = input("Please enter their name: ")

    #Checks name input to ensure it is valid, asking user to input again if not
    alpha_Checker = Validator(["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", 
                               "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"])

    while not alpha_Checker.checkCharacters(name) or not name:
        name = input("Name entered incorrectly. Please try again: ")

    #Asks user to input the email
    email = input("Please enter their email: ")

    #Checks email input to ensure it is valid, asking user to input again if not
    email_Checker = Validator(["!", '"', "`", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", " "])

    while not email_Checker.checkCharacters(email) or not email:
        email = input("Email entered incorrectly. Please try again: ")

    #Asks user for either student or instructor information depending on input type entered earlier
    if input_type.lower() == "student":
        #Asks user for a student ID
        student_id = input("Please enter the student ID: ")

        #Verifies student ID, prompting user to enter again if invalid
        correct_student_id = False
        while not correct_student_id:
            if len(student_id) <= 7 and student_id.isdigit():
                correct_student_id = True
            else:
                student_id = input("Student ID entered incorrectly. Please try again: ")

        #Asks user for program of study
        program_of_study = input("Please enter the student's program of study: ")

        #Verifies program of study, rompting user to enter again if invalid
        while not alpha_Checker.checkCharacters(program_of_study) or not program_of_study:
            program_of_study = input("Program of study entered incorrectly. Please try again: ")

        #Creates a new student using the student class
        new_student = Student(name, email, student_id, program_of_study)

        #Adds the new student to the college records list
        college_records.append(new_student)

    else:
        #Asks user for an instructor ID
        instructor_id = input("Please enter the instructor ID: ")

        #Verifies the instructor ID, prompting user to enter again if invalid
        correct_instructor_id = False
        while not correct_instructor_id:
            if len(instructor_id) <= 5 and instructor_id.isdigit():
                correct_instructor_id = True
            else:
                instructor_id = input("Instructor ID entered incorrectly. Please try again: ")
        
        #Asks user for the last institution the instructor graduated from
        institution_graduated_from = input("Please enter the last instutition the instructor graduated from: ")

        #Verifies institution, prompting user to enter again if invalid
        while not alpha_Checker.checkCharacters(institution_graduated_from) or not institution_graduated_from:
            institution_graduated_from = input("Institution entered incorrectly. Please try again: ")
        
        #Asks user for the highest degree earned by the instructor
        highest_degree_earned = input("Please enter their highest degree earned: ")

        #Verifies degree earned, prompting user to enter again if invalid
        while not alpha_Checker.checkCharacters(highest_degree_earned) or not highest_degree_earned:
            highest_degree_earned = input("Degree entered incorrectly. Please try again: ")
        
        #Creates a new instructor using the instructor class
        new_instructor = Instructor(name, email, instructor_id, institution_graduated_from, highest_degree_earned)

        #Adds the new instructor to the college records list
        college_records.append(new_instructor)

    #Asks user if they would like to continue adding more instructors/students
    continue_adding = input("Would you like to add another? (Y/N): ")

    #Verifies that the input is either Y or N, prompting user to enter again if not
    correct_input = False
    while not correct_input:
        if continue_adding.lower() == "y" or continue_adding.lower() == "n":
            correct_input = True
        else:
            continue_adding = input("Incorrect value entered. Please enter either \"Y\" or \"N\": ")

    #If the user entered Y, the loop continues, otherwise the loop breaks
    if continue_adding.lower() == "y":
        continue
    else:
        break

#Displays all the information for the students and instructors in the college records list
displayInformation(college_records)