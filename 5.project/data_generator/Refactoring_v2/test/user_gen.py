import random
import uuid
from datetime import datetime


# user.csv 만들기
# uuid, name, birthdate, age, address
# uuid -> 라이브러리

# uuid 
u_id = uuid.uuid4()
print(u_id)
print(type(u_id))

# name 성 + 이름 랜덤 조합

with open('lastname_data.csv','r',encoding='utf-8') as f:
    surnames = f.read().splitlines()
last_name = random.choice(surnames)

with open('firstname_data.csv','r',encoding='utf-8') as f:
    names = f.read().splitlines()
# print(names)
first_name = random.choice(names)

u_name = last_name + first_name
print(u_name)

# 생일 및 나이

def generate_birthdate():
    year = random.randint(1960, 2010)
    month = random.randint(1, 12)
    day = random.randint(1, 28)

    return f'{year}-{month:02d}-{day:02d}'

bday = generate_birthdate() # str 타입
print(bday)

b_year = datetime.strptime(bday,'%Y-%m-%d').year
print(b_year)
# print(datetime.now().year)
# print(datetime.today().year)
# this_year = datetime.now().strftime('%Y')  # 얘도 str타입...
# this_year = datetime.strptime(this_year, '%Y')
# print(this_year)



age = datetime.now().year - b_year
print(age)



def generate_gender():
    return random.choice(['Female','Male'])
print(generate_gender())
gender = generate_gender()



with open('address_sample.csv','r',encoding='utf-8') as f:
    address_list = f.read().splitlines()
# print(address_list)
address = random.choice(address_list).replace(',',' ')
# print(address)
num = str(random.randint(1,100))
u_address = address+num+'길'
print(address+num+'길')



print((str(u_id), u_name, bday, age, gender, u_address))