from monster import *


# charcteristics
# - student_no
# - skill_test
class Student(Monster):
    def __init__(self, __name, __tax_number, __fur, student_no, skill_list=None):
        super().__init__(__name, __tax_number, __fur)
        if skill_list is None:
            skill_list = []
        self.__student_no = student_no
        self.skill_list = skill_list


# write setters and getters
    def set_student_number(self, student_no):
        self.__student_no = student_no
        return student_no

    def get_student_number(self):
        return "Student Number: " + self.__student_no

    def add_skill(self, skill):
        self.skill_list.append(skill)
        return "Skills Added\n"

    def get_skills_list(self):
        return ', '.join(self.skill_list)
