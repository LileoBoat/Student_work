#lets create a student class and give certain attributes
class Student:
    valedictorian = None #This  is the class variable to store the valedictorian

    def __init__(self, name, student_id, major, gpa, is_on_probation):
        self.name = name
        self.student_id = student_id
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation 
        
    def good_student(self):
        if self.gpa > 3.0:
            return f"You will be part oof the good student list"
        
        else:
            return f"You will not be part of the good student list"

#now lets find sudent who can be eligible to be a software engineer
#They mus satisfy two conditions, gpa > 3.0 and must be in the fields of mathematics computer science and software engineering     
    def software_engineer(self):
        if self.gpa >= 3.0 and self.major in ["Mathematics", "Computer science", "Statistics", "Computer engineering"]:
            return f"You can be a software engineer"
        else:
            return f"You cannot be software engineer"
        

    def graduation(self):
        if self.gpa < 1.5:
            return f"You are on probation, you might not graduate"
        else:
            return f"you are good to graduate"
        
    #Now lets create a valedictorian for this school system
    #Check if the student has the highest GPA and update valedictorian
    
        
