
class Monster():
    def __init__(self, name, tax_number, fur):
        self.__name = name
        self.__tax_number = tax_number
        self.__fur = fur


    def set_name(self, name):
        self.__name = name
        return "Name: " + self.__name

    def get_name(self):
        return self.__name

    def set_tax_number(self, tax_number):
        # password = ''
        # user_input = ''
        # if
        # else:
        #     return 'Incorrect Password'

        self.__tax_number = tax_number
        return self.__tax_number

    def get_tax_number(self):
        return "Tax Number : " + self.__tax_number

    def set_fur(self, fur):
        self.__fur = fur
        return self.__fur

    def get_fur(self):
        return "Fur : " + self.__fur

