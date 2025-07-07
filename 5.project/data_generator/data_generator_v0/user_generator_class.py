import random
import uuid
from datetime import datetime
import csv


class User_generator:
    # def __init__(self):
        

    def generate_uuid(self):
        u_id = uuid.uuid4()
        return u_id

    def generate_name(self):
        with open('lastname_data.csv','r',encoding='utf-8') as f:
            surnames = f.read().splitlines()
            last_name = random.choice(surnames)

        with open('firstname_data.csv','r',encoding='utf-8') as f:
            names = f.read().splitlines()
            first_name = random.choice(names)

        u_name = last_name + first_name
        return u_name
    
    def generate_bday(self):
        year = random.randint(1960, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        bday = f'{year}-{month:02d}-{day:02d}'

        b_year = datetime.strptime(bday,'%Y-%m-%d').year

        age = datetime.now().year - b_year
        return bday, age

    def generate_gender(self):
        gender = random.choice(['Female','Male'])
        return gender
    
    def generate_address(self):
        with open('address_sample.csv','r',encoding='utf-8') as f:
            address_list = f.read().splitlines()
        address = random.choice(address_list[1:]).replace(',',' ')
        num = str(random.randint(1,100))
        u_address = address+num+'길'
        return u_address
    
    def generate_user(self):
        u_id = self.generate_uuid()
        u_name = self.generate_name()
        birthdate, age = self.generate_bday()
        gender = self.generate_gender()
        u_address = self.generate_address()
        return (str(u_id), u_name, birthdate, age, gender, u_address)

    def generate_user_dataset(self, n:int):
        with open('user_dataset.csv','w',encoding='utf-8',newline='') as f: # 데이터셋 처음 만들때 필드 제목 생성. 이후 데이터 추가할 땐 비활성화. 기존 데이터에 새로운 필드를 추가? -> pandas 이용?
            csv_writer = csv.writer(f)
            csv_writer.writerow(['user_id','user_name','birthdate','age','gender','user_address'])
        for _ in range(n):
            user = self.generate_user()
            with open('user_dataset.csv', 'a', encoding='utf-8',newline='') as f:
                csv_writer = csv.writer(f)
                csv_writer.writerow(user)


if __name__=='__main__':
    user_gen = User_generator()
    user_gen.generate_user_dataset(1000)
        









