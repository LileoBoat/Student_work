from student_db import Student


student1 = Student("Joseph", 109731, "Biochemistry", 3.50, True)
student2 = Student("Benji", 123456, "Computer engineering", 2.74, True)
student3 = Student("Eben", 246822, "Statistics", 3.40, False)
student4 = Student("Berry", 987654, "Accounting", 3.0, True)
student5 = Student("Edem", 135791, "Accounting", 2.34, False)
student6 = Student("George", 222222, "Mathematics", 4.2, False)
student7 = Student("Mussa", 000000, "Mathematics", 1.2, False)
student8 = Student("Rexford", 333333, "Food Science", 3.45, True)

print(student1.good_student())
print(student2.good_student())
print(student3.good_student())
print(student4.good_student())
print(student5.good_student())
print(student6.good_student())
print(student7.good_student())
print(student8.good_student())

print(student1.software_engineer())
print(student2.software_engineer())
print(student3.software_engineer())
print(student4.software_engineer())
print(student5.software_engineer())
print(student6.software_engineer())
print(student7.software_engineer())
print(student8.software_engineer())

print(student1.graduation())
print(student2.graduation())
print(student3.graduation())
print(student4.graduation())
print(student5.graduation())
print(student6.graduation())
print(student7.graduation())
print(student8.graduation())





