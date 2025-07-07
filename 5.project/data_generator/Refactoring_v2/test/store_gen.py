import random
import uuid
import csv
# store id, store type, store name, store address

# store id
s_id = uuid.uuid4()
print(s_id)


# store address
# s_address 
address_list=[]
with open('address_sample.csv','r',encoding='utf-8') as f:
    csv_reader = csv.reader(f)
    next(csv_reader) # header 건너뜀
    # print(csv_reader)
    for row in csv_reader:
        address_list.append(row) # csv_reader 사용하는 경우, 리스트 안에 리스트로 담김.
# print(address_list)
address_pick = random.choice(address_list)
road_name = address_pick[2]
print(road_name)
address = ' '.join(address_pick)
s_address = address + str(random.randint(1,50)) + '길 ' + str(random.randint(1,100))
print(s_address)

# with open('address_sample.csv','r',encoding='utf-8') as f:
#     address_list = f.read().splitlines()
# print(address_list)
# address = random.choice(address_list).replace(',',' ')
# # print(address)


# store type
store_type = ['폴바셋','투썸플레이스','블루보틀','컴포즈커피','매머드커피','이디야커피','커피빈','할리스커피','스타벅스','메가커피']
store = random.choice(store_type)
print(store)



# store name
road_name = road_name.replace('대로','')
road_name = road_name.replace('로','')
store_name = store + ' ' + road_name + '점'
print(store_name)