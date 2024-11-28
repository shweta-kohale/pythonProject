# Task 1 - Create a Class PyATB , 5 Attributes, 3 Functions/Methods
#
# Use PC - to set the value of the attributes
#
# create a Print student information method/function

class PyATB:
    name : None
    email_address : None
    skill : None
    experience : None
    location : None

    def __init__(self,name,email_address,skill,experience,location):
        self.name = name
        self.email_address = email_address
        self.skill = skill
        self.experience = experience
        self.location = location

    def print_student_info(self):
        print(f"Name is {self.name}", f"email address is {self.email_address}", f"skill is {self.skill}"
              , f"experience is {self.experience}", f"location is {self.location}")



student1 = PyATB("Shweta", "shweta.kohale@gmail.com", "Manual Testing", "9 years",
                 "Pune")
student2 = PyATB("Ananya", "an@gmail.com", "Developer", "2 years",
                 "Mumbai")
student3 = PyATB("Sanvi", "sn@gmail.com", "SDET", "5 years",
                 "Pune")

student1.print_student_info()
student2.print_student_info()
student3.print_student_info()