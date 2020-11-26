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
        print("Name: " + self.name + " | Email: " + self.email + " | Student ID: " + self.student_id + " | Program of study: " + self.program_of_study)
        
class Instructor(Person):
    """A simple class for representing an instructor"""
    def __init__(self, name, email, instructor_id, institution_graduated_from, highest_degree_earned):
        super().__init__(name, email)
        self.instructor_id = instructor_id
        self.institution_graduated_from = institution_graduated_from
        self.highest_degree_earned = highest_degree_earned

    def showInstructorInformation(self):
        """Prints out all information for a certain instructor"""
        print("Name: " + self.name + " | Email: " + self.email + " | Instructor ID: " + self.instructor_id + " | Graduated from: " + self.institution_graduated_from + " | Degree earned: " + self.highest_degree_earned)

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

program_running = True

college_records = []

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
    name_Checker = Validator(["!", '"', "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"])

    while not name_Checker.checkCharacters(name):
        name = input("Name entered incorrectly. Please try again: ")

    #Asks user to input the email
    email = input("Please enter their email: ")

    #Checks email input to ensure it is valid, asking user to input again if not
    email_Checker = Validator(["!", '"', "`", "#", "$", "%", "^", "&", "*", "(", ")", "=", "+", ",", "<", ">", "/", "?", ";", ":", "[", "]", "{", "}", "\\"])

    while not email_Checker.checkCharacters(email):
        email = input("Email entered incorrectly. Please try again: ")

    #Asks user for either student or instructor information depending on input type entered earlier
    if input_type.lower() == "student":
        student_id = input("Please enter the student ID: ")

        correct_student_id = False
        while not correct_student_id:
            if len(student_id) <= 7 and student_id.isdigit():
                correct_student_id = True
            else:
                student_id = input("Student ID entered incorrectly. Please try again: ")

        program_of_study = input("Please enter the student's program of study: ")

        correct_program = False
        while not correct_program:
            if program_of_study.isalpha():
                correct_program = True
            else:
                program_of_study = input("Program of study entered incorrectly. Please try again: ")

        #Creates a new student using the student class
        new_student = Student(name, email, student_id, program_of_study)

        #Adds the new student to the college records list
        college_records.append(new_student)

    else:
        instructor_id = input("Please enter the instructor ID: ")

        correct_instructor_id = False
        while not correct_instructor_id:
            if len(instructor_id) <= 5 and instructor_id.isdigit():
                correct_instructor_id = True
            else:
                instructor_id = input("Instructor ID entered incorrectly. Please try again: ")
        
        institution_graduated_from = input("Please enter the last instutition the instructor graduated from: ")

        correct_institution = False
        while not correct_institution:
            if institution_graduated_from.isalpha():
                correct_institution = True
            else:
                institution_graduated_from = input("Institution entered incorrectly. Please try again: ")

        highest_degree_earned = input("Please enter their highest degree earned: ")

        correct_degree = False
        while not correct_degree:
            if highest_degree_earned.isalpha():
                correct_degree = True
            else:
                highest_degree_earned = input("Degree entered incorrectly. Please try again: ")
        
        #Creates a new instructor using the instructor class
        new_instructor = Instructor(name, email, instructor_id, institution_graduated_from, highest_degree_earned)

        #Adds the new instructor to the college records list
        college_records.append(new_instructor)

    conitnue_adding = input("Would you like to add another? (Y/N): ")

    correct_input = False
    while not correct_input:
        if conitnue_adding.lower() == "y" or conitnue_adding.lower() == "n":
            correct_input = True
        else:
            conitnue_adding = input("Incorrect value entered. Please enter either \"Y\" or \"N\": ")

    if conitnue_adding.lower() == "y":
        continue
    else:
        break

displayInformation(college_records)