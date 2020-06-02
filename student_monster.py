from monster import  *


# charcteristics
# - student_no
# - skill_test
class Students(Monster):
    def __init__(self, student_no, skill_list):
        # super().__init__(self, name, tax_number, fur)
        self.student_no = student_no
        self.skill_list = skill_list