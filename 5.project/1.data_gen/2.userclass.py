import random

class NameGenerator:
    # def __init__(self):
        # self.names = ['John','Jane','Michael','Emily','William','Olivia']
        # 기존 하드코딩 되어있는 것을 파일을 통해서 ㅇ릭는 방식으로 변경

    def __init__(self, file_path):
        self.names = self.load_data_from_file(file_path)

    def load_data_from_file(self, file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read().splitlines()
        return data

    
    def generate_name(self):
        return random.choice(self.names)
    

class BirthdateGenerator:
    def generate_bday(self):
        year = random.randint(1990, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        return f'{year}-{month:02d}-{day:02d}'
    
class GenderGenerator:
    def generate_gender(self):
        return random.choice(['Female','Male'])

class AddressGenerator:
    def __init__(self, file_path):
        self.city = self.load_from_data_file(file_path)

    def load_from_data_file(self,file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            city = f.read().splitlines()
        return city
    
    def generate_address(self):
        city = random.choice(self.city)
        street_num = random.randint(1,100)
        return f'{street_num} {city}'
    


class UserGenerator:
    def __init__(self):
        self.name = NameGenerator('names.txt')
        self.address = AddressGenerator('cities.txt')
        self.gender = GenderGenerator()
        self.bday = BirthdateGenerator()

    def generate_user(self, count):
        users = []
        for _ in range(count):
            name = self.name.generate_name()
            bday = self.bday.generate_bday()
            gender = self.gender.generate_gender()
            address = self.address.generate_address()
            users.append((name,bday,gender,address))
        return users
    
class DisplayData(UserGenerator):
    def print_data(self, count):
        data = self.generate_user(count)
        for name, bday, gender, address in data:
            print(f'Name: {name}\nBrithdate: {bday}\nGender: {gender}\nAddress: {address}\n')


# 최종 실행
my_data = DisplayData()
my_data.print_data(10)