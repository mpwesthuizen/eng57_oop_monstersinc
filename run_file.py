from monster import *
from student_monster import *
from course import *

# Create two student object
mike = Student('Mike', '0235', 'green', '66', ['funny', 'smart'])
sully = Student('Sully', '9934', 'blue', '02', ['strength', 'roar'])

# add a skill to each of the students
mike.add_skill('python')
sully.add_skill('C#')

# initialise a course
course1 = Course('Nightmares', '02/06/2020')

# Append student object / instances to list of student attributes in one of the courses
course1.add_student(mike)
course1.add_student(sully)

print(course1.get_student())


# extra: get the list of students, iterate over it and print each of the students name
