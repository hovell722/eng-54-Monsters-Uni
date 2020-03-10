from monster_class import *
from teacher_class import *
from student_class import *
from workshop_class import *

# 1. As a receptionist of the University, I should be able to create a Student, with only first name and last name
print("1. Students created: First Name, Last Name")
student1 = Student('Danielle', 'Daniels', 1)
student2 = Student('Nick', 'Nicholson', 2)
student3 = Student('Bob', 'Bobford', 3)

list_students_created = []
list_students_created.append(student1)
list_students_created.append(student2)
list_students_created.append(student3)

for student in list_students_created:
    print(student.f_name, student.l_name)
print(" ")

# 2. As a receptionist of the University, I should be able to create a Teacher
print("2. Teachers created: First Name, Last Name")
teacher1 = Teacher('Derrick', 'Derrickson', 1)
teacher2 = Teacher('Nigel', 'Nigelos', 2)
teacher3 = Teacher('Barry','Barrihno', 3)

list_teachers_created = []
list_teachers_created.append(teacher1)
list_teachers_created.append(teacher2)
list_teachers_created.append(teacher3)

for teacher in list_teachers_created:
    print(teacher.f_name, teacher.l_name)
print(" ")

# 3. As a receptionist of the University, I should be able to list all workshops
# 4. As a receptionist of the University, I should be able to create a workshop

print("4. Workshops created: Subject, Teacher")
workshop1 = Workshop('Digital Dance', 'Derrick')
workshop2 = Workshop('Natural Neuroscience', 'Nigel')
workshop3 = Workshop('Business Businessment', 'Barry')

print("Workshop 1: ", workshop1.subject + ",", workshop1.teacher)
print("Workshop 2: ", workshop2.subject + ",", workshop2.teacher)
print("Workshop 3: ", workshop3.subject + ",", workshop3.teacher)
print(" ")
list_workshops_created = []
list_workshops_created.append(workshop1)
list_workshops_created.append(workshop2)
list_workshops_created.append(workshop3)

print("3. List of all workshops")
for workshop in list_workshops_created:
    print(workshop.subject + ",", workshop.teacher)
print(" ")


# 5. As a receptionist of the University, I should be able to add skills to a student object

print("5. Skills added to students")
student1.skills.extend(['Good with swords', 'Loud roar', 'Freezes time'])
student2.skills.extend(['Travels in shadows', 'Silent at all times', 'Turns people into stone'])
student3.skills.extend(['Absorbs others strengths', 'Mind reader', 'Can fly'])

print("Student 1 skills: ", student1.skills)
print("Student 2 skills: ", student2.skills)
print("Student 3 skills: ", student3.skills)
print(" ")

# 6. As a receptionist of the University, I should be able to list all of the students skills

print("6. List of all skills printed")
for student in list_students_created:
    print(student.skills)