from datetime import datetime
from generator import *

class User_generator(Generator):
    output_file_path = '../output/'
    file_path_name = '../data_sample/name_sample.json'
    file_path_address = '../data_sample/address_sample.json'

    def generate_user_name(self):
        name_sample = read_json(self.file_path_name)
        last_name = random.choice(name_sample['lastname'])
        first_name = random.choice(name_sample['firstname'])
        user_name = last_name + first_name
        logging.debug(user_name)
        return user_name
    
    def generate_bday(self):
        year = random.randint(1960, 2010)
        month = random.randint(1, 12)
        day = random.randint(1, 28)
        bday = f'{year}-{month:02d}-{day:02d}'
        b_year = datetime.strptime(bday,'%Y-%m-%d').year
        age = datetime.now().year - b_year
        return bday, age

  
    def generate_address(self):
        address_list = read_json(self.file_path_address)
        logging.debug(list(address_list))
        city = random.choice(list(address_list))
        logging.debug(f'랜덤으로 뽑은 주소: {city}')
        district = random.choice(list(address_list[city]))
        logging.debug(list(address_list[city]))
        logging.debug(district)
        road = random.choice(list(address_list[city][district]))
        logging.debug(list(address_list[city][district]))
        logging.debug(road)
        num = str(random.randint(1,100))
        u_address = city + ' ' + district + ' ' + road + ' ' + num +'길'
        logging.debug(u_address)
        return u_address
    
    def generate_data(self):
        user_id = self.generate_uuid()
        user_name = self.generate_user_name()
        birthdate, age = self.generate_bday()
        gender = random.choice(['Female','Male'])
        u_address = self.generate_address()
        user = {'user_id':  user_id,
                'user_name': user_name,
                'birthdate': birthdate,
                'age': age,
                'gender': gender,
                'user_address': u_address }
        return user

    def generate_dataset(self, n:int):
        user_dataset = []
        for _ in range(n):
            user = self.generate_data()
            user_dataset.append(user)
            print(user_dataset)
        return user_dataset

        # 출력 형태에 따라 저장 -> 다른 모듈로 만들기...?
        # self.write_csv(self.output_file_path, field)
        # for _ in range(n):
        #     user = self.generate_data()
        #     self.append_csv(self.dataset_file_path_user, user)
        # print(f'사용자 데이터 {n}가 생성되었습니다.')


if __name__=='__main__':


    if len(sys.argv) > 1:
        data_num = int(sys.argv[1])
    else:
        data_num = int(input('생성할 데이터의 개수를 입력하세요: '))

    user_gen = User_generator()
    user_gen.generate_dataset(data_num)

    # user_gen.generate_user_name(file_path_name)    
    #  
    








