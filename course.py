from student_monster import *

class Course:
    def __init__(self, module_name, start_date, list_of_students=[]):
        self.module_name = module_name
        self.list_of_students = list_of_students
        self.start_date = start_date

    def set_module_name(self, module_name):
        self.module_name = module_name
        return module_name

    def get_module_name(self):
        return "Module Name : " + self.module_name.title()

    def add_student(self, student):
        self.list_of_students.append(student)
        return "Skills Added"

    def get_student(self):
        return ', '.join(self.__get_names())

    def __get_names(self):
        all_students = []
        for student in self.list_of_students:
            all_students.append(student.get_name())

        return all_students

    def set_start_date(self, start_date):
        self.start_date = start_date
        return start_date

    def get_start_date(self):
        return "Start Date: " + self.start_date.title
