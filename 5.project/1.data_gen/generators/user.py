from generators.name import *
from generators.address import *
from generators.birthdate import *
from generators.gender import *


class UserGenerator:
    def __init__(self):
        self.name = NameGenerator('names.txt')
        self.bday = BirthdateGenerator()
        self.gender = GenderGenerator()
        self.address = AddressGenerator('cities.txt')

    def generate_user(self, count):
        users = []
        for _ in range(count):
            name = self.name.generate_name()
            bday = self.bday.generate_bday()
            gender = self.gender.generate_gender()
            address = self.address.generate_address()
            users.append((name,bday,gender,address))
        return users