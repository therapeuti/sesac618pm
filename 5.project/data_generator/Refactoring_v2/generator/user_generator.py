from datetime import datetime
from generator import *

class User_generator(Generator):
    file_path_lastname = 'lastname_data.csv'
    file_path_firstname = 'firstname_data.csv'

    def generate_name(self):
        last_name = random.choice(self.read_csv(self.file_path_lastname))[0]
        first_name = random.choice(self.read_csv(self.file_path_firstname))[0]
        # print(last_name) # 로깅모듈 알아볼 것. 
        # print(first_name)
        u_name = last_name + first_name
        # print(u_name)
        return u_name
    
    def generate_bday(self):
        year = random.randint(1960, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        bday = f'{year}-{month:02d}-{day:02d}'

        b_year = datetime.strptime(bday,'%Y-%m-%d').year
        age = datetime.now().year - b_year
        return bday, age

  
    def generate_address(self):
        address_list = self.read_csv(Generator.file_path_address)
        # print(address_list)
        address = ' '.join(random.choice(address_list))
        # print(address)
        num = str(random.randint(1,100))
        u_address = address+num+'길'
        return u_address
    
    def generate_data(self):
        u_id = self.generate_uuid()
        u_name = self.generate_name()
        birthdate, age = self.generate_bday()
        gender = random.choice(['Female','Male'])
        u_address = self.generate_address()
        return (u_id, u_name, birthdate, age, gender, u_address)

    def generate_dataset(self, n:int):
        field = ['user_id','user_name','birthdate','age','gender','user_address']
        self.write_csv(Generator.dataset_file_path_user, field)
        for _ in range(n):
            user = self.generate_data()
            self.append_csv(Generator.dataset_file_path_user, user)
        print(f'사용자 데이터 {n}가 생성되었습니다.')


if __name__=='__main__':
    # if len(sys.argv) > 1:
    #     data_num = int(sys.argv[1])
    # else:
    #     data_num = int(input('생성할 데이터의 개수를 입력하세요: '))

    user_gen = User_generator()
    # user_gen.generate_dataset(data_num)
    file_path = 'name_sample.json'
    user_gen.generate_person_name(file_path)    
    








