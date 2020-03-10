from monster_class import *
from teacher_class import *
from student_class import *
from workshop_class import *


# As a receptionist of the University, I should be able to create a Student, with only first name and last name
# student1 = Student('James', 'Hovell', 1)
# student2 = Student('Dave', 'Jackson', 2)
# student3 = Student('George', 'Delph', 3)
#
# list_students_created = []
# list_students_created.append(student1)
# list_students_created.append(student2)
# list_students_created.append(student3)
#
# for student in list_students_created:
#     print(student.f_name, student.l_name)


# Create empty list called list_students_created
list_students_created = []
# Have a student_id_counter
student_id = 0
# With every iteration of the while loop:
# while True:
#     # increment the student_id_counter
#     student_id += 1
#     # ask for user input (names)
#     f_name = input('Enter first name: ')
#     l_name = input('Enter last name: ')
#     # create a student from those inputs
#     student = Student(f_name, l_name, student_id)
#     # add that student to the list of students
#     list_students_created.append(student)
#     print(f"Student name: {f_name} {l_name}, {student_id}")
#     print("Number of students in list:", str(len(list_students_created)))


# do same for teacher

# teacher1 = Teacher('Derrick', 'Derrickson', 1)
# teacher2 = Teacher('Nigel', 'Nigelos', 2)
# teacher3 = Teacher('Barry','Barrihno', 3)
#
# list_teachers_created = []
# list_teachers_created.append(teacher1)
# list_teachers_created.append(teacher2)
# list_teachers_created.append(teacher3)
#
# for teacher in list_teachers_created:
#     print(teacher.f_name, teacher.l_name)

# Declare a list of teachers
list_teachers_created = []
# Teacher_id_count variable
staff_id = 0
# save user input so you can test the while condition
user_input = ' '
# Create the while loop:
while user_input != 'quit':
    # increment the counter
    staff_id += 1
    # ask for name
    f_name = input("Enter first name: ")
    l_name = input("Enter last name: ")
    # if user input is 'quit':
    if f_name == 'quit' or l_name == 'quit':
        # quit the loop
        break
    # create teacher object from inputs
    teacher = Teacher(f_name, l_name, staff_id)
    # add teacher to list
    list_teachers_created.append(teacher)
    print(f"Teachers name: {f_name} {l_name}, {staff_id}")
    print("Number of students in list:", str(len(list_teachers_created)))



# do the same for workshops

workshop1 = Workshop('Digital Dance', 'Derrick')
workshop2 = Workshop('Natural Neuroscience', 'Nigel')
workshop3 = Workshop('Business Businessment', 'Barry' )

list_workshops_created = []
list_workshops_created.append(workshop1)
list_workshops_created.append(workshop2)
list_workshops_created.append(workshop3)

for workshop in list_workshops_created:
    print(workshop.subject, workshop.teacher)


# call method